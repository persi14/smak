from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products$', views.products, name='products'),
    url(r'^news$', views.news, name='news'),
    url(r'^about-company$', views.about, name='about'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^news_detail_(?P<idnews>\d+)$', views.news_detail, name='news_detail'),
    #url(r'^login/', "django.contribauth.views.login", {"template_name"="login.html"} name="login"),
]