# Generated by Django 4.1.7 on 2023-07-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0002_remove_product_suggestions_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suggestions',
            field=models.ManyToManyField(blank=True, to='suggestions.product'),
        ),
        migrations.DeleteModel(
            name='Suggestion',
        ),
    ]
