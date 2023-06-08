"""
login views
"""
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


class IsLoggedInView(APIView):
    """
    Determine whether the user is logged in
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return JsonResponse(
                {"status": "success", "message": "The user is authenticated."},
                status=200,
            )

        return JsonResponse(
            {
                "status": "failure",
                "message": "The user is NOT authenticated.",
            },
            status=403,
        )


class LoginRedirectView(APIView):
    """
    Redirect to the identity provider's login page
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse("oidc_authentication_init"))


class LogoutView(APIView):
    """
    Log the user out
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse(
            {"status": "success", "message": "The user is logged out."},
            status=200,
        )
