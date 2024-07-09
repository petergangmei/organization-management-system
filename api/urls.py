from django.urls import path,include
from . import views
urlpatterns =[
    path('check-email-availability/<email>/', views.check_email_availability),
]