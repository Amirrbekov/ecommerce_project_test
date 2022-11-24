from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.

def homepage_view(request, category_slug=None):
    
    context = {}
    category_page = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context['products']=products
    context['categories']=categories
    
    if category_slug:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category_page, available=True)
        context["products"]=products
        context['category_page']=category_page
    
    return render(request, "homepage.html", context)

def detail_view(request, category_slug, product_slug):

    context = {}
    try:
        product = Product.objects.get(category__slug=category_slug,
        slug=product_slug)
        context['product']=product

    except Exception as e:
        raise e
        
    return render(request, 'detail.html', context)

def _card_id(request):

    card = request.session.session_key
    if not card:
        card = request.session.create()
    return card

def card_detail(request, total = 0, counter = 0, card_items=None):
    context = {}
    try:
        card = Card.objects.get(card_id=_card_id(request))
        card_items = CardItem.objects.filter(card=card, active=True)

        for card_item in card_items:
            total += (card_item.product.product_max_price * card_item.quantity)
            counter += card_item.quantity

        context["card_items"]=card_items
        context["total"]=total
        context["counter"]=counter

    except ObjectDoesNotExist:
        pass

    return render(request, "card.html", context)

def add_card(request, product_id):

    product = Product.objects.get(id=product_id)
    try:
        card = Card.objects.get(card_id=_card_id(request))
    except Card.DoesNotExist:
        card = Card.objects.create(card_id=_card_id(request))
        card.save()
    try:
        card_item = CardItem.objects.get(product=product, card=card)
        if card_item.quantity < card_item.product.is_active:
            card_item.quantity +=1
        card_item.save()
    except CardItem.DoesNotExist:
        card_item = CardItem.objects.create(product=product, quantity = 1, card=card)
        card_item.save()

    return redirect('shop:card_detail')

def remove_card(request, product_id):

    card = Card.objects.get(card_id=_card_id(request))
    product = get_object_or_404(Product, id=product_id)
    card_item = CardItem.objects.get(product=product, card=card)
    if card_item.quantity > 1:
        card_item.quantity -= 1
        card_item.save()
    else:
        card_item.delete()

    return redirect("shop:card_detail")

def delete_card(request, product_id):

    card = Card.objects.get(card_id=_card_id(request))
    product = get_object_or_404(Product, id=product_id)
    card_item = CardItem.objects.get(product=product, card=card)
    card_item.delete()

    return redirect("shop:card_detail")