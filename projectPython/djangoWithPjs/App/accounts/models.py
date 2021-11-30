from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    phoneNo = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = (
        ('indoor', 'In Door'),
        ('outdoor', 'Out Door')
    )
    category = models.CharField(max_length=200, null=True, choices=category)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    status = (
        ('pending', 'Pending'),
        ('out for Delivery', 'Out For Delivery'),
        ('delivered', 'Delvered')
    )
    status = models.CharField(max_length=200, null=True, choices=status)

    def __str__(self) -> str:
        return self.product.name
