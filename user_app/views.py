from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views.generic import View

from .models import Profile


class LoginView(View):

    def post(self, request):
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")

    def get(self, request):
        return render(request, "login.html")

class SignupView(View):

    def post(self, request):
        user_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if user_password != confirm_password:
            messages.error(request, "Password doesn't match")
            return render(request, "signup.html")

        hashed_password = make_password(user_password)

        user = Profile(
            full_name=request.POST.get("full_name"),
            username=request.POST.get("name"),
            email=request.POST.get("email"),
            password=hashed_password,
            user_gender=request.POST.get("gender"),
            user_DOB=request.POST.get("DOB"),
            user_phone_no=request.POST.get("phone_no"),
            user_cnic=request.POST.get("CNIC"),
            user_designation=request.POST.get("designation"),
            user_address=request.POST.get("user_address")
        )
        user.save()

        # Log the user in
        login(request, user)
        return redirect("profile")

    def get(self, request):
        return render(request, "signup.html")

class ResetPasswordView(View):

    def post(self, request):
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
        return render(request, "reset_password.html")


class ProfileView(View):

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            context = {
                'profile': user.profile
            }
            return render(request, "profile.html", context=context)

        return render(request, "login.html")


class LogoutView(View):

    def post(self, request):
        logout(request)
        messages.success(request, "Signed out!")
        return render(request, "login.html")


def error_404(request, exception):
    """Returns the error page for 404 error if the page is not found"""
    response = render(request, "404.html")
    return response
