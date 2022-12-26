from django.shortcuts import render
from django.views import generic
from .models import Product, Category


class ProductListView(generic.ListView):
    
    template_name = 'cart/product_list.html' 
    queryset = Product.objects.all()
    
    
    def get_context_data(self, **kwargs):
        opcion = self.request.GET.get('opcion', '')
        
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        context['titulo'] = opcion
        
        if opcion== '':
            context['productos'] = Product.objects.all()
        elif opcion== 'Todo':
            context['productos'] = Product.objects.all()
        else :
            context['productos'] = Product.objects.filter(category__name=opcion)
            
        return context
    

class ProductDetailView(generic.DetailView):
    template_name= 'cart/product_detail.html'
    queryset = Product.objects.all()
    
    