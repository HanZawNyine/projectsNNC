from django.contrib import admin
from django.db.models.base import ModelBase
from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Movie)
admin.site.register(models.Tag)
admin.site.register(models.Serverlink)
