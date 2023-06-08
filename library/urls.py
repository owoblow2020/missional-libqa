"""
library URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/session/", include("login.urls")),
    path("admin/", admin.site.urls),
    path("oidc/", include("mozilla_django_oidc.urls")),
]
