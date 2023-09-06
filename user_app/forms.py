from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class SignupForm(UserCreationForm):
    # Add any additional fields if needed
    class Meta:
        model = Profile  # Use your custom user model if applicable
        fields = ["username", "email", "password1", "password2"]
