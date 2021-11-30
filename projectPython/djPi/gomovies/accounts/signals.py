from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from accounts import models

def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        gp = Group.objects.get(name="customer")
        instance.groups.add(gp)
        models.Customer.objects.create(user=instance)


post_save.connect(create_customer_profile, sender=User)
