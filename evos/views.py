from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Product
from django.shortcuts import get_object_or_404
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        categories = Category.objects.all()
        new_products = Product.objects.order_by('-id')[:10]
        context = {
            'products': products,
            'categories': categories,
            'new_products': new_products
        }
        return context
    



class ProductVew(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        product = get_object_or_404(Product, id=kwargs['id'])

        context = {
            'product': product,
        }
        return context

