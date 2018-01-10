from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products$', views.products, name='products'),
    url(r'^reviews$', views.reviews, name='reviews'),
    url(r'^about-company$', views.about, name='about'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^add_review$', views.add_review, name='add_review'),
]