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
    path('settings/', views.category, name="category"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('vendor_home/', views.vendor_home, name="vendor_home"),
    path('delete/', views.delete, name="delete"),
    path('vendorsignup/', views.vendorlogin, name="Vendorlogin"),
    path('settings/', views.vendorsignup, name="vendorsignup"),
    path('edits/', views.edits, name="edits"),
    path('view/', views.view, name="view"),
    path('clientinfo/', views.clientinfo, name="clientinfo"),
 
]
