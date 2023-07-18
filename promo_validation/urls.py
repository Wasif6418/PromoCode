from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CouponListAPIView, CouponDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    # ... other URL patterns ...
    path('api/coupons/', CouponListAPIView.as_view(), name='coupon-list'),
    path('api/coupons/<int:pk>/', CouponDetailAPIView.as_view(), name='coupon-detail'),
    path('api/products/', ProductListAPIView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/coupons/', CouponListAPIView.as_view(), name='coupon-list'),
    #path('api/coupons/<int:pk>/', CouponDetailAPIView.as_view(), name='coupon-detail'),

]
