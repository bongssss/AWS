from django.urls import path 
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('products/', views.products, name="products"),
	path('cart/', views.cart, name="cart"),
    path('cartOperation/<int:vendor_id>/', views.cartOperation, name='cartOperation'),
	path('choice/<int:vendor_id>/', views.choice, name="choice"),
    path('settings/', views.settings, name="settings"),
    path('pdf/<int:vendor_id>/', views.pdf_view, name="pdf"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('vendor_home/', views.vendor_home, name="vendor_home"),
    path('delete/', views.delete, name="delete"),
    path('vendorlogin/', views.vendorlogin, name="vendorlogin"),
    path('vendorsettings/', views.vendorsettings, name="vendorsettings"),
    path('vendorsignup/', views.vendorsignup, name="vendorsignup"),
    path('edits/', views.edits, name="edits"),
    path('view/', views.view, name="view"),
    path('clientinfo/', views.clientinfo, name="clientinfo"),
    path('logout/', views.logout, name="logout"),
    path('vendorlogout/', views.vendorlogout, name="vendorlogout"),
 
]
