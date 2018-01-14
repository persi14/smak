from django.shortcuts import render, HttpResponse, redirect

from .models import News

def index(request):
	return render(request, 'index.html')

def contacts(request):
	return render(request, 'contacts.html')

def about(request):
	return render(request, 'about.html')

def news(request):
	news = News.objects.all().order_by('idnews').reverse()
	return render(request, 'news.html', {'news':news})

def products(request):
	return render(request, 'products.html')

def news_detail(request, idnews):
	news = News.objects.get(idnews=idnews)
	return render(request, 'news_detail.html', {'news':news})

# Create your views here.
