# Generated by Django 3.2.9 on 2021-11-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customer_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/static/accounts/profiles'),
        ),
    ]