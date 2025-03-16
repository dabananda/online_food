from django.shortcuts import render, HttpResponse
from django.template import loader
from food.models import Item

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {}
    return HttpResponse(template.render(context, request))