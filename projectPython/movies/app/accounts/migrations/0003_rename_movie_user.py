# Generated by Django 3.2.9 on 2021-11-25 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='User',
        ),
    ]