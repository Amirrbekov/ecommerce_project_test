from django.db import models
from django.urls import reverse
from .helper import seo

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="Category")
    descriptions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Category,self).save(*args, **kwargs)
        self.slug = seo(self.title)
        super(Category,self).save(*args, **kwargs)

    def get_url(self):
        return reverse("shop:product_by_category", args=[self.slug])

    class Meta:

        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("-created_at",)
    
class Brand(models.Model):

    name = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="Brand")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Brand,self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(Brand,self).save(*args, **kwargs)

    def get_url(self):
        return reverse("shop:brand_list", kwargs={"slug": self.slug})

    class Meta:

        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ("-created_at",)
    
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(editable=False, unique=True)
    name = models.CharField(max_length=25, verbose_name="Name")
    descriptions = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="Product")
    product_max_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("shop:product_detail", args=[ self.category.slug, self.slug])

    def save(self, *args, **kwargs):
        super(Product,self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(Product,self).save(*args, **kwargs)
    
    class Meta:
        
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)

class Card(models.Model):

    card_id = models.CharField(max_length=255, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("added_at",)
        db_table = "Card"

    def __str__(self):
        return self.card_id

class CardItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carditem_product")
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "CardItem"

    def sub_total(self):
        return self.product.product_max_price * self.quantity

    def __str__(self):
        return self.product

