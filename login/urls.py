"""
login URL Configuration
"""
from django.urls import path

from .views import IsLoggedInView, LoginRedirectView, LogoutView

urlpatterns = [
    path("is_loggedin", IsLoggedInView.as_view()),
    path("login", LoginRedirectView.as_view()),
    path("logout", LogoutView.as_view()),
]
