from django.conf.urls import url

from .views import request_login_email, current_user

urlpatterns = [
    url("request-login-email", request_login_email),
    url("users/current", current_user),
]
