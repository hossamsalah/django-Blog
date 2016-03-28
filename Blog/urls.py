from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^create', views.create, name='create'),
    url(r'comments(?P<blog_id>[0-9]+)/$', views.addcomment, name='comments'),
    url(r'newcomment(?P<blog_id>[0-9]+)/$', views.newcomment, name='newcomment'),
    url(r'^add', views.add, name='add'),
    url(r'register', views.register, name='register'),
    url(r'login', views.user_login, name='login'),
    url(r'logout', views.user_logout, name='logout'),
    url(r'category(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'about(?P<author_id>[0-9]+)/$', views.about, name='about'),



]