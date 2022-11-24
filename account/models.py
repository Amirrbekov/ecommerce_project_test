from django.db import models

# Create your models here.

class RegisterCustomer(models.Model):

    fullname = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:

        verbose_name = "Register Customer"
        verbose_name_plural = "Register Customers"
        ordering = ("-created_at",)
    
class LoginCustomer(models.Model):

    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:

        verbose_name = "Login Customer"
        verbose_name_plural = "Login Customers"