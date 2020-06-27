from django.urls import path
from .views import *
from django.views.generic import View

urlpatterns = [
    path('', IndexView.as_view(), name ="index" ),
    path('productdetail/<slug>', ProductDetail.as_view(), name ="product-detail" ),
    path('about', about),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('decrease-from-cart/<slug>', decrease_from_cart, name="decrease-from-cart"),
    path('remove-item/<slug>', remove_item, name="remove-item"),
    # path('cart', CartViews.as_view(), name="cart"),
    path('login', userlogin, name="login"),
    path('logout', LogoutUser, name="logout"),
    path('register', UserRegister, name="register"),
    path('cart', CartViews.as_view(), name ="cart" ),
]
