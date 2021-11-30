from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    type = (
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('comedy', 'Comedy')
    )
    # type = models.CharField(max_length=200, null=True, choices=type)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    moviename = models.ForeignKey(
        Movie, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.moviename


class ServerLink(models.Model):
    moviename = models.ForeignKey(
        Movie, null=True, on_delete=models.SET_NULL)
    linkUrl = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.moviename.name
