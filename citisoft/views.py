from django.shortcuts import render

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
   context = {}   # Initialize context dictionary
   # Render products.html with context
   return render(request, 'citisoft/user/products.html', context)

# Function-based view for home page
def home(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render home.html with context
   return render(request, 'citisoft/user/home.html', context)

# Function-based view for choice page
def choice(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render choice.html with context
   return render(request, 'citisoft/user/choice.html', context)

# Function-based view for cart page
def cart(request):   # Request handler
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
   return render(request, 'delete.html', context)

