from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryForm(admin.ModelAdmin):

    list_display = ("title", "created_at", "slug")

"""    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False"""

@admin.register(Brand)
class BrandForm(admin.ModelAdmin):

    list_display = ("name", "slug")

@admin.register(Product)
class ProductForm(admin.ModelAdmin):

    list_display = ("name", "slug", "created_at")