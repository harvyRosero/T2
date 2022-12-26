from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Size(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    size = models.ManyToManyField(Size)
    
    def __str__(self):
        return self.name
    
    def get_price(self):
        return "{:.2f}".format(self.price/100) 
    
    def get_absolute_url(self): 
        return reverse("cart:product-detail", kwargs={"slug": self.slug})
    
class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    imagen = models.ImageField(upload_to='images_adicionales')
    
    def __str__(self):
        return self.product
    
def pre_save_product_receiver(sender, instance, *args, **kwargs):
    
    if not instance.slug:
        instance.slug = slugify(instance.title)
        
pre_save.connect(pre_save_product_receiver, sender=Product)
