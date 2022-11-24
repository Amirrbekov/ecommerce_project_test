from django import forms
from .models import *

class RegisterCustomForm(forms.ModelForm):

    class Meta:

        model = RegisterCustomer
        fields = ("fullname", "username", "email", "password", "confirm")

class LoginCustomerForm(forms.ModelForm):

    class Meta:

        model = LoginCustomer
        fields = ("username", "password")