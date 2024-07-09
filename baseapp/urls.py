from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_account, name="login"),
    path('logout/', views.logout_account, name="logout"),
    path('forgot-password/', views.forgot_password, name="forgot-password"),
    path('reset-password-token/', views.password_reset_token, name='reset-password-token'),
]
