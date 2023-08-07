from django.urls import path, include
from apps.users.views import *

urlpatterns = [
    path("users/", include("django.contrib.auth.urls")),
    path('users/register/', RegisterView.as_view(), name='register'),
]


  
