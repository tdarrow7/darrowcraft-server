# Generated by Django 4.2.13 on 2024-06-14 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_remove_brand_coffee_coffee_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='brand',
        ),
    ]