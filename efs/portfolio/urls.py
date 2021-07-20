from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('investment_list', views.investment_list, name='investment_list'),
    url('investment/create', views.investment_new, name='investment_new'),
    url(r'^investment/(?P<pk>\d+)/edit/$', views.investment_edit, name='investment_edit'),
    url(r'^investment/(?P<pk>\d+)/delete/$', views.investment_delete, name='investment_delete'),
]