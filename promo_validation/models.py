from django.db import models


class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_name = models.CharField(max_length=20)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    percentages = models.IntegerField(null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    #def __str__(self):
    #   return self.coupon_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_name = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

   #def __str__(self):
    #   return self.name

    def save(self, *args, **kwargs):
        if self.coupon_name:
            coupon = self.coupon_name
            if coupon.value is not None:
                self.discount_price = self.price - coupon.value
            elif coupon.percentages is not None:
                self.discount_price = self.price * (100 - coupon.percentages) / 100
        else:
            self.discount_price = self.price

        super().save(*args, **kwargs)
