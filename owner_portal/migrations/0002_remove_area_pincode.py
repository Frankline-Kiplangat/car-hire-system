# Generated by Django 4.1.3 on 2022-11-26 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner_portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='pincode',
        ),
    ]
