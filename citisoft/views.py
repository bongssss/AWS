from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import loader
from .models import *
from .models import Vendorr

# Create your views here.
# Function-based view for index page
def index(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render index.html with context
   return render(request, 'citisoft/user/index.html', context)

# Function-based view for settings page
def settings(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render settings.html with context
   return render(request, 'citisoft/user/settings.html', context)

# Function-based view for products page
def products(request):   # Request handler
   vendor = Vendorr.objects.all()
   context = {'Vendors': vendor}   # Initialize context dictionary
   # Render products.html with context
   return render(request, 'citisoft/user/products.html', context)

# Function-based view for home page
def home(request):   # Request handler
   vendor = Vendorr.objects.all()
   context = {'Vendors': vendor}   # Initialize context dictionary
   # Render home.html with context
   return render(request, 'citisoft/user/home.html', context)

# Function-based view for choice page
def choice(request, vendor_id):   # Request handler
      vendor = get_object_or_404(Vendorr, pk=vendor_id)  # Get the requested product or display a 404 error if it
      context = {'VENDOR': vendor}   # Initialize context dictionary
   # Render choice.html with context
      return render(request, 'citisoft/user/choice.html', context)

# Function-based view for cart page
def cart(request):   # Request handler
  # if request.user.is_authenticated:  # If user is
   #   client = request.user.client  # authenticated, get the corresponding Client object
   #   vendor, created = Vendorr.objects.get_or_create(client=client, complete = False)  # and create a new Vendor associated to this Client
       
   context = {}   # Initialize context dictionary
   # Render cart.html with context
   return render(request, 'citisoft/user/cart.html', context)


def category(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render category.html with context
   return render(request, 'citisoft/user/category.html', context)


def delete(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render delete.html with context
   return render(request, 'citisoft/user/delete.html', context)


def userlogin(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render userlogin.html with context
   return render(request, 'citisoft/user/userlogin.html', context)


def usersignup(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render usersignup.html with context
   return render(request, 'citisoft/user/usersignup.html', context)


def vendor_home(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render vendor_home.html with context
   return render(request, 'citisoft/vendor/vendor_home.html', context)


def vendorsignup(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render vendorsignup.html with context
   return render(request, 'citisoft/vendor/vendorsignup.html', context)


def vendorlogin(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render vendorlogin.html with context
   return render(request, 'citisoft/vendor/vendorlogin.html', context)


def edits(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render vendorlogin.html with context
   return render(request, 'citisoft/vendor/edits.html', context)


def view(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render view.html with context
   return render(request, 'citisoft/vendor/view.html', context)

def clientinfo(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render clientinfo.html with context
   return render(request, 'citisoft/vendor/clientinfo.html', context)


def vendorsettings(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render vendorsettings.html with context
   return render(request, 'citisoft/vendor/vendorsettings.html', context)


def vendorlogout(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render vendorlogout.html with context
   return render(request, 'citisoft/vendor/vendorlogout.html', context)


def logout(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render v.html with context
   return render(request, 'citisoft/user/logout.html', context)