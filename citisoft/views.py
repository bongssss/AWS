from django.shortcuts import render

# Create your views here.
# Function-based view for index page
def index(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render index.html with context
   return render(request, 'citisoft/index.html', context)

# Function-based view for settings page
def settings(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render settings.html with context
   return render(request, 'citisoft/settings.html', context)

# Function-based view for products page
def products(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render products.html with context
   return render(request, 'citisoft/products.html', context)

# Function-based view for home page
def home(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render home.html with context
   return render(request, 'citisoft/home.html', context)

# Function-based view for choice page
def choice(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render choice.html with context
   return render(request, 'citisoft/choice.html', context)

# Function-based view for cart page
def cart(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render cart.html with context
   return render(request, 'cart.html', context)


