from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products$', views.products, name='products'),
    url(r'^news$', views.news, name='news'),
    url(r'^about-company$', views.about, name='about'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^news_detail_(?P<idnews>\d+)$', views.news_detail, name='news_detail'),
    url(r'^type-(?P<idtype>\d+)$', views.list_product, name='list_product'),
    url(r'^product-(?P<idproduct>\d+)$', views.product_detail, name='product_detail')
]

