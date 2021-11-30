from django.shortcuts import render
from django.http.response import HttpResponse

# from accounts.models import Products
from accounts.models import *

# Create your views here.


def Dashboard(request):
    customers = Customer.objects.all()
    order = Order.objects.all()
    totals = order.count()
    delivered = Order.objects.filter(status='delivered').count()
    pending = Order.objects.filter(status='pending').count()
    return render(request, 'accounts/dashboard.html', {
        'customers': customers, 'orders': order,
        'totals': totals, 'delivered': delivered,
        'pending': pending
    })


def Product(request):
    product = Products.objects.all()
    return render(request, 'accounts/product.html', {
        'products': product
    })


def Customers(request):
    return render(request, 'accounts/Customer.html')
