from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profilePic = models.ImageField(
        blank=True, upload_to='static/profiles')
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200, null=True)
    imageurl = models.CharField(max_length=200, null=True)
    desription = models.CharField(max_length=200, null=True)
    type = (
        ('movie', 'Movies'),
        ('series', 'Series')
    )
    type = models.CharField(max_length=200, null=True, choices=type)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Serverlink(models.Model):
    name = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
    serverurl = models.CharField(max_length=200, null=True)
    serverName = models.CharField(max_length=200, null=True)
    resolution = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name.name
