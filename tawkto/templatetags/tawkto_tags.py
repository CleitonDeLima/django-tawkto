import hashlib
import hmac

from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("tawkto/templatetags/tawkto_script.html")
def tawkto_script(**kwargs):
    default_id_site = getattr(settings, "TAWKTO_ID_SITE")
    default_api_key = getattr(settings, "TAWKTO_API_KEY", None)
    default_widget_id = getattr(settings, "TAWKTO_WIDGET_ID", "default")
    default_is_secure = getattr(settings, "TAWKTO_IS_SECURE", False)
    exclude_superusers = getattr(settings, "TAWKTO_EXCLUDE_SUPERUSERS", True)

    user_email = kwargs.get("user_email", "")
    user_name = kwargs.get("user_name", "")
    is_secure = kwargs.get("is_secure", default_is_secure)
    widget_id = kwargs.get("widget_id", default_widget_id)
    id_site = kwargs.get("id_site", default_id_site)
    api_key = kwargs.get("api_key", default_api_key)
    extra_attributes = kwargs.get("extra_attributes", {})

    data = {
        "id_site": id_site,
        "api_key": api_key,
        "is_secure": is_secure,
        "widget_id": widget_id,
        "url": f"https://embed.tawk.to/{id_site}/{widget_id}",
        "visitor": {
            "name": user_name,
            "email": user_email,
        },
        "extra_attributes": extra_attributes,
    }

    if is_secure and user_email:
        hash_hmac = hmac.new(
            key=api_key.encode(),
            msg=user_email.encode(),
            digestmod=hashlib.sha256,
        ).hexdigest()
        data["visitor"]["hash"] = hash_hmac

    return {
        "tawkto_data": data,
        "exclude_superusers": exclude_superusers,
    }
