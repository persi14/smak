from django.contrib import admin
from .models import News, TypeProduct, Product



class NewsAdmin(admin.ModelAdmin):
	fields = ['title', 'text']
	list_display = ('title', 'date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nameproduct', 'idtype']

admin.site.register(TypeProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(News, NewsAdmin)
# Register your models here.
