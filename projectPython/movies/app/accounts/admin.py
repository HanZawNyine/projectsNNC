from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Movie)
admin.site.register(models.Favorite)
admin.site.register(models.ServerLink)
admin.site.register(models.Tag)
