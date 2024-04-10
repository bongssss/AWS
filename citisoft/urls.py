from django.urls import path 
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('products/<int:categoryId>', views.products, name="products"),
    path('product/', views.searchForm, name='product'),  # URL without categoryId
    path('product/<str:vendorName>/', views.product, name='product'),
	path('cart/', views.cart, name="cart"),
    path('update_cart/', views.update_cart, name="update_cart"),
    path('cartOperation/<int:vendor_id>', views.cartOperation, name='cartOperation'),
	path('choice/<int:vendorCategoriesId>/', views.choice, name="choice"),
    path('settings/', views.settings, name="settings"),
    path('pdf/<int:vendor_id>/', views.pdf_view, name="pdf"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('vendor_home/', views.vendor_home, name="vendor_home"),
    path('delete/', views.delete, name="delete"),
    path('vendorlogin/', views.vendorlogin, name="vendorlogin"),
    path('vendordelete/', views.deleteVendor, name="vendordelete"),
    path('vendorsettings/', views.vendorSettings, name="vendorsettings"),
    path('vendorsignup/', views.vendorsignup, name="vendorsignup"),
    path('edits/', views.edits, name="edits"),
    path('view/', views.view, name="view"),
    path('clientinfo/', views.clientinfo, name="clientinfo"),
    path('logout/', views.logout, name="logout"),
    path('vendorlogout/', views.vendorlogout, name="vendorlogout"),
    path('category/', views.searchForm, name='category'),
 
]
