from django.shortcuts import render
from django.http import JsonResponse
from .models import *



# Create your views here.
def store(request):
    products = Product.objects.all()  # all the items in db
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    # two cases , when user is logged in and not logged in. we'll start with the first one.
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all
    else:  # second one.
        items = []
        order = {'get_cart_total=0, get_cart_item=0'}
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all
    else:  # second one.
        items = []
        order = {'get_cart_total=0, get_cart_item=0'}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    return JsonResponse('item was added!', safe=False)
