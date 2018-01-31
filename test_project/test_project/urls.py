from django.urls import path

from app.views import test_view

urlpatterns = [
    path('', test_view),
]
