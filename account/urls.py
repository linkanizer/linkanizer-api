from django.conf.urls import url

from .views import request_login_email

urlpatterns = [url("request-login-email", request_login_email)]
