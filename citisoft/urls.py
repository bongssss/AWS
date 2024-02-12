from django.urls import path 
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('products/', views.products, name="products"),
	path('cart/', views.cart, name="cart"),
	path('choice/', views.choice, name="choice"),
    path('settings/', views.settings, name="settings"),
 
]
