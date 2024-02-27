from django.urls import path
from . import views
from django.contrib.auth.models import User
urlpatterns = [
    path('home/', views.homePage, name='home'),
    path('signup/', views.signupPage, name='signup'),
    path('signUpfunction/', views.signUpfunction, name='signUpfunction'),
    path('recoverpassword/', views.recoverPasswordPage, name='recoverpassword'),
    path('recoverPasswordFunction/', views.recoverPasswordFunction, name='recoverPasswordFunction'),
    path('login/', views.loginPage, name='login'),
    path('loginFunction/', views.loginFunction, name='loginFunction'),
    path('home/<str:username>/', views.homePageLogged, name='home'),
    path('logoutFunction', views.logoutFunction, name='logoutFunction'),
    path('profile/<str:username>/', views.profilePage, name='profile'),
]