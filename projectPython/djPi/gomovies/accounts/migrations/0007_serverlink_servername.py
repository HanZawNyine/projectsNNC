# Generated by Django 3.2.9 on 2021-11-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_serverlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverlink',
            name='serverName',
            field=models.CharField(choices=[('googledrive', 'Google Drive'), ('mega', 'Mega Cloud')], max_length=200, null=True),
        ),
    ]