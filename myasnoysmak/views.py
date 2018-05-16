from django.shortcuts import render, HttpResponse, redirect

from .models import News, TypeProduct, Product

def index(request):
	news = News.objects.all().order_by('idnews').reverse()
	return render(request, 'index.html', {'news':news})

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

def list_product(request, idtype):
	typeproduct = TypeProduct.objects.get(idtype=idtype)
	products = Product.objects.filter(idtype=typeproduct)
	return render(request, 'list_product.html', {'products':products, 'typeproduct':typeproduct})


def product_detail(request, idproduct):
	product = Product.objects.get(idproduct=idproduct)
	return render(request, 'product_detail.html', {'product':product})



def price_list(request):
	f = open("/home/persi/smak/smak/myasnoysmak/static/Prays_Myasnoy-smak.zip", 'rb')
	return HttpResponse(f, content_type='application/zip')

def cafe(request):
    return render(request, 'cafe.html')

# Create your views here.
