from django.shortcuts import render, redirect 
from shop.models.customer import Customer
from django.views import View 
from shop.models.product import Products

class Cart(View):
    def get(self, request):
        if request.user.is_authenticated:
            ids = list(request.session.get('cart').keys())
            products = Products.get_products_by_id(ids)
            return render(request, 'cart.html', {'products': products})
        else:
            return redirect('login')

