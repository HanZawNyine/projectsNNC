from django.urls import path
from . import views


urlpatterns = [
    path('', views.Product),
    path('dashboard', views.Dashboard),
    path('customer', views.Customers),
    path('product', views.Product),
]
