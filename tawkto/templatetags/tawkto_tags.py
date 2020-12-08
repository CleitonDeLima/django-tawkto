import hashlib
import hmac

from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("tawkto/templatetags/tawkto_script.html")
def tawkto_script(**kwargs):
    default_id_site = getattr(settings, "TAWKTO_ID_SITE")
    default_api_key = getattr(settings, "TAWKTO_API_KEY", None)
    is_secure = getattr(settings, "TAWKTO_IS_SECURE", False)

    user_email = kwargs.pop("user_email", "")
    user_name = kwargs.pop("user_name", "")
    widget_id = kwargs.pop("widget_id", "default")
    id_site = kwargs.pop("id_site", default_id_site)
    api_key = kwargs.pop("api_key", default_api_key)

    data = {
        "id_site": id_site,
        "api_key": api_key,
        "is_secure": is_secure,
        "user_email": user_email,
        "user_name": user_name,
        "widget_id": widget_id,
    }

    if is_secure and user_email:
        hash_hmac = hmac.new(
            key=api_key.encode(), msg=user_email.encode(), digestmod=hashlib.sha256
        ).hexdigest()

        data.update(hash=hash_hmac)

    return data
