from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    details = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={
            'slug': self.slug
        })
    def get_add_to_cart_url(self):
         return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })
    def get_remove_item_url(self):
         return reverse("remove-item", kwargs={
            'slug': self.slug
        })


class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_price(self):
        return self.quantity * self.product.price    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    