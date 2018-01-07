from django.contrib import admin

from .models import Comment, TypeProduct, Product

admin.site.register(Comment)
admin.site.register(TypeProduct)
admin.site.register(Product)

# Register your models here.
