""" URls for user app """
from django.urls import path

from .views import (
    EditProfileView,
    LoginView,
    LogoutView,
    ProfileView,
    ResetPasswordView,
    SignupView,
)

urlpatterns = [
    path("", LoginView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("reset_password/", ResetPasswordView.as_view(), name="reset_password"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
