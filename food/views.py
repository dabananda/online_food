from django.shortcuts import render, redirect
from food.models import Item
from food.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        "form": form,
    }

    return render(request, 'food/item_form.html', context)


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        "form": form,
        "item": item,
    }

    return render(request, 'food/item_form.html', context)


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    context = {
        "item": item,
    }

    return render(request, 'food/item_delete.html', context)
