from django.shortcuts import render, HttpResponse, redirect

from .models import Review

def index(request):
	return render(request, 'index.html')

def contacts(request):
	return render(request, 'contacts.html')

def about(request):
	return render(request, 'about.html')

def reviews(request):
	reviews = Review.objects.all().order_by('idreview').reverse()
	return render(request, 'reviews.html', {'reviews':reviews})

def products(request):
	return render(request, 'products.html')

def add_review(request):
	from .forms import Add_Review
	import datetime
	if request.method == "POST":
		form = Add_Review(request.POST)
		if form.is_valid():
			reviews = Review.objects.all().order_by('idreview').reverse()
			idreview = reviews[0].idreview + 1
			today = datetime.date.today()
			fields = form.cleaned_data
			Review.objects.create(idreview=idreview, date=today, author = fields['author'], text = fields['text'])
			return redirect('reviews')
	form = Add_Review()
	return render(request, 'add_review.html', {'form':form})


# Create your views here.
