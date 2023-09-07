""" Views for user app """
import os
from pathlib import Path

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views.generic import View

from .models import Profile


class LoginView(View):
    """
    View for handling user login.
    """

    def post(self, request):
        """
        Handles POST requests for user login.
        """
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")

    def get(self, request):
        """
        Handles GET requests for displaying the login form.
        """
        return render(request, "login.html")


class SignupView(View):
    """
    View for handling user registration (signup).
    """

    def post(self, request):
        """
        Handles POST requests for user registration.
        """
        username = request.POST.get("name")
        user_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if user_password != confirm_password:
            messages.error(request, "Password doesn't match")
            return render(request, "signup.html")

        file = request.POST.get("user_image")
        if user_image:
            user_image = f"../media/uploads/{username}.png"
            if Path(user_image).is_file():
                os.remove(user_image)
        else:
            user_image = "../media/uploads/empty.png"
        file.save(user_image)

        hashed_password = make_password(user_password)
        user = Profile(
            full_name=request.POST.get("full_name"),
            username=username,
            email=request.POST.get("email"),
            password=hashed_password,
            user_gender=request.POST.get("gender"),
            user_DOB=request.POST.get("DOB"),
            user_phone_no=request.POST.get("phone_no"),
            user_cnic=request.POST.get("CNIC"),
            user_designation=request.POST.get("designation"),
            user_address=request.POST.get("user_address"),
            user_image="/Users/ayshasiddique/Documents/User_authentication_app/user_authentication_app/user_app/media/uploads/empty.png",
        )
        user.save()

        # Log the user in
        login(request, user)
        return redirect("profile")

    def get(self, request):
        """
        Handles GET requests for displaying the signup form.
        """
        return render(request, "signup.html")


class ResetPasswordView(View):
    """
    View for handling user password reset.
    """

    def post(self, request):
        """
        Handles POST requests for resetting user password.
        """
        username = request.POST.get("username")
        user_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not Profile.objects.filter(username=username).exists():
            messages.error(request, "User does not exist")
            return render(request, "reset_password.html")

        if user_password != confirm_password:
            messages.error(request, "Password doesn't match")
            return render(request, "reset_password.html")

        hashed_password = make_password(user_password)
        user = Profile.objects.get(username=username)
        user.password = hashed_password
        user.save()
        return render(request, "login.html")

    def get(self, request):
        """
        Handles GET requests for displaying the password reset form.
        """
        return render(request, "reset_password.html")


class ProfileView(View):
    """
    View for displaying user profile.
    """

    def get(self, request):
        """
        Handles GET requests for displaying the user profile page.
        """
        if request.user.is_authenticated:
            user = request.user
            context = {"profile": user.profile}
            print(context.get("user_image"))
            return render(request, "profile.html", context=context)

        return render(request, "login.html")


class EditProfileView(View):
    """
    View for displaying user profile.
    """

    def get(self, request):
        """
        Handles GET requests for displaying the user edit profile page.
        """
        if request.user.is_authenticated:
            user = request.user
            context = {"profile": user.profile}
            return render(request, "edit_profile.html", context=context)

        return render(request, "login.html")

    def post(self, request):
        """
        Handles POST requests for editing user profile.
        """
        # username = request.POST.get("name")
        # print(username)
        user = Profile.objects.get(username=request.user.username)
        print(user.full_name)
        user.full_name = request.POST.get("full_name")
        user.email = request.POST.get("email")
        user.user_gender = request.POST.get("gender")
        user.user_DOB = request.POST.get("DOB")
        user.user_phone_no = request.POST.get("phone_no")
        user.user_cnic = request.POST.get("CNIC")
        user.user_designation = request.POST.get("designation")
        user.user_address = request.POST.get("user_address")
        user.save()
        messages.success(request, "Updated")
        return redirect("profile")


class LogoutView(View):
    """
    View for handling user logout.
    """

    def post(self, request):
        """
        Handles POST requests for user logout.
        """
        logout(request)
        messages.success(request, "Signed out!")
        return render(request, "login.html")


def error_404(request, exception):
    """
    Returns the error page for 404 error if the page is not found.
    """
    response = render(request, "404.html")
    return response
