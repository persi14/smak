from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
	fields = ['title', 'text']
	list_display = ('title', 'date')

admin.site.register(News, NewsAdmin)

# Register your models here.
