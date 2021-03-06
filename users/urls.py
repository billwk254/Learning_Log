"""Defines url patterns for users"""
from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views

app_name = "users"

urlpatterns = [
    #Login Page
    path(r"^login/$",LoginView.as_view(), {"template_name": "users/login.html"},name="login"),
    path(r"^logout/$",views.logout_view,name="logout"),
    #Registration page
    path(r"^register/$",views.register,name="register")
]

