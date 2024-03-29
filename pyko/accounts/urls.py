from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path("signup/", signup, name = 'signup'),
    path("user_profile/<str:username>/", user_profile, name = 'user_profile'),
]