# Generated by Django 4.1.7 on 2023-07-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo_validation', '0008_alter_coupon_id_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
