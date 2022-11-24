from django.urls import path
from .views import *

app_name = "shop"

urlpatterns = [
    path('', homepage_view, name="homepage"),
    path('category/<slug:category_slug>/', homepage_view, name="product_by_category"),
    path('category/<slug:category_slug>/product/<slug:product_slug>/', detail_view, name="product_detail"),
    path("card/", card_detail, name="card_detail"),
    path("card/add/<int:product_id>", add_card, name="add_card"),
    path("card/remove/<int:product_id>", remove_card, name="remove_card"),
    path("card/delete/<int:product_id>", delete_card, name="delete_card"),
]