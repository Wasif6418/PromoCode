# Generated by Django 4.1.7 on 2023-07-22 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0006_product_suggestions_delete_suggestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Productname',
            new_name='product_name',
        ),
    ]
