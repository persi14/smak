from django.contrib import admin
from .models import News, TypeProduct, Product

admin.site.register(TypeProduct)
admin.site.register(Product)

class NewsAdmin(admin.ModelAdmin):
	fields = ['title', 'text']
	list_display = ('title', 'date')



admin.site.register(News, NewsAdmin)
# Register your models here.
