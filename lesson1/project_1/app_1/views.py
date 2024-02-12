from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Mebel
from .forms import UpdateItemForm


def show_all(request):
    mebels = Mebel.objects.all().order_by("-price")
    return render(
        request,
        'app_1/show_all.html',
        {
            'form': form,
            'mebels': mebels
        }
    )

def show_all_admin(request):
    form = UpdateItemForm()
    mebels = Mebel.objects.all().order_by("-parse_datetime")
    return render(
        request,
        'app_1/show_admin_item.html',
        {'mebels': mebels}
    )

def show_item(request, item_id):
    item = Mebel.objects.get(pk=item_id)
    return render(
        request,
        'app_1/show_item.html',
        {'item': item}
    )

def main(request):
    return redirect('main')

def page_not_found(request, exception):
    return redirect('main')