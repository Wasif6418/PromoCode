from rest_framework import serializers
from .models import Coupon
from .models import Product


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'coupon_name', 'start_date', 'end_date', 'percentages', 'value']


class ProductSerializer(serializers.ModelSerializer):
    coupon_name = CouponSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'coupon_name','discount_price']
