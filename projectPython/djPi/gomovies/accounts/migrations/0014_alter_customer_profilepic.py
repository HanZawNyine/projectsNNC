# Generated by Django 3.2.9 on 2021-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customer_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='static/accounts/profiles'),
        ),
    ]
