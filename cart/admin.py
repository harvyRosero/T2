from django.contrib import admin
from .models import Product, Size, Category, ImageProduct

admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(ImageProduct)

