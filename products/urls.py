from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name ="index" ),
    path('productdetail/<slug>', ProductDetail.as_view(), name ="product-detail" ),
    path('about', about),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('remove-item/<slug>', remove_item, name="remove-item"),
    path('cart', CartView, name="cart" ),
    path('login', userlogin, name="login"),
]