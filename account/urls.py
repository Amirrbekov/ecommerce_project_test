from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('register/', signupuser_view, name='signupuser'),
    path('login/', signinuser_view, name="signinuser"),
    path("logout/", logoutuser_view, name="logout"),
]