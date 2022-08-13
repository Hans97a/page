from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.views.generic import FormView
from users import forms
from django.urls import reverse_lazy
# Create your views here.


class login_view(FormView):
    form_class = forms.LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('board:index')

    def form_valid(self, form):
        personal_id = form.cleaned_data.get('personal_id')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=personal_id,password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect(resolve_url('board:index'))


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('users:login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)