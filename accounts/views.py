from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm


def home(request):
    return render(request, "accounts/home.html")


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True


def register_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 註冊後自動登入
            messages.success(request, "註冊成功，歡迎加入！")
            return redirect("accounts:home")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    # 登出需用 POST（避免 CSRF 登出攻擊）；GET 只顯示頁面
    if request.method == "POST":
        logout(request)
        messages.info(request, "你已成功登出")
        return redirect("accounts:logout")
    return render(request, "accounts/logout.html")

class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = "accounts/password_change.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:home")
    success_message = "密碼已成功修改"