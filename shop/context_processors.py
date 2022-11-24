from .models import *
from .views import _card_id
from django.db.models import Q
from django.views.generic import ListView

def menu_links(request):

    context={}
    categories_links = Category.objects.all()
    context["categories_links"]=categories_links

    return context

def counter(request):
    context={}
    item_count = 0
    if "admin" in request.path:
        return {}
    else:
        try:
            card = Card.objects.filter(card_id=_card_id(request))
            card_items = CardItem.objects.all().filter(card=card[:1])
            for card_item in card_items:
                item_count += card_item.quantity
        except Card.DoesNotExist:
            item_count = 0

    context['item_count']=item_count
    return context


class SearchResultsView(ListView):
    model = Product
    template_name = "search_result.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(descriptions__icontains=query)
        )
        return object_list