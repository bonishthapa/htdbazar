from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from .models import Product, OrderProduct, Order
from django.utils import timezone

# Create your views here.

# def index(request):
#     return render(request,'templates/index.html')

class IndexView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()

class ProductDetail(DetailView):
    template_name = 'product-detail.html'
    queryset = Product.objects.all()

def about(request):
    return render(request,'templates/about.html')    

def add_to_cart(request,slug):
    product = get_object_or_404(Product,slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        user = request.user,
        ordered = False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.product.filter(product__slug=product.slug).exists():
            order_product.quantity +=1
            order_product.save()
        else:
            order.product.add(order_product)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date = ordered_date)
        order.products.add(order_product)
    return redirect('/')

def remove_item(request,slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.product.filter(product__slug=product.slug).exists():
           order_product = OrderProduct.objects.filter(
            product=product,
            user = request.user,
            ordered = False)[0]
           order.product.remove(order_product)
        else:
            return redirect('/')

    # else:
    #     return redirect('/')


    # return redirect('/')            

# class CartView(View):
#     def get(self, *args, **kwargs):
#         try:
#             order = Order.objects.get(user=self.request.user, ordered=False)
#             context={
#                 'object': order
#             }
#             return render(self.request,'cart.html',context)  
#         except ObjectDoesNotExist:
#             messages.error(request,'error')
#             return redirect('/')
def CartView(request):
    cart = OrderProduct.objects.all()
    context={
        'cart':cart
    }
    return render(request,'cart.html',context)
         

def userlogin(request):
    return render(request,'account/login.html')         