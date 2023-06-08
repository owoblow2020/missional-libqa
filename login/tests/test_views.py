"""
Tests of session-related views
"""
from django.contrib.auth import get_user_model, SESSION_KEY
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from login.views import IsLoggedInView, LoginRedirectView


class IsLoggedInViewTest(TestCase):
    """
    Test IsLoggedInView
    """

    def setUp(self):
        self.request = RequestFactory().get("/api/session/islogged_in")
        self.user = get_user_model().objects.create()

    def test_user_is_not_authenticated(self):
        """
        Test that an HTTP 403 is returned if the user is not authenticated
        """
        response = IsLoggedInView.as_view()(self.request)

        self.assertEqual(
            response.status_code,
            403,
            "An HTTP 403 status code should have been returned",
        )

    def test_user_is_authenticated(self):
        """
        Test that an HTTP 200 is returned if the user is authenticated
        """
        self.request.user = self.user
        response = IsLoggedInView.as_view()(self.request)

        self.assertEqual(
            response.status_code,
            200,
            "An HTTP 200 status code should have been returned",
        )


class LoginRedirectViewTest(TestCase):
    """
    Test the login redirect view
    """

    def test_redirects_to_idp(self):
        """
        Test that the redirect view redirects to the IdP's login page
        """
        request = RequestFactory().get("/api/session/login")
        response = LoginRedirectView.as_view()(request)

        self.assertEqual(
            response.status_code, 302, "A redirect should have been returned."
        )

        self.assertEqual(
            response.url,
            reverse("oidc_authentication_init"),
            "The user should be redirected to the IdP login page.",
        )


class LogoutViewTest(TestCase):
    """
    Test the logout view
    """

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create()

    def _user_is_authenticated(self):
        return SESSION_KEY in self.client.session

    def test_that_a_user_can_log_out(self):
        """
        Test that an authenticated user can log out
        """
        self.client.force_login(self.user)
        response = self.client.post("/api/session/logout")

        self.assertFalse(
            self._user_is_authenticated(), "The user should no longer be authenticated."
        )

        self.assertEqual(
            response.status_code,
            200,
            "An HTTP 200 status code should have been returned",
        )
