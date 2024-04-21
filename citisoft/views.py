from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.template import loader
from .models import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter  # Assuming letter size for the PDF
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from django.contrib import messages
import json
from django.http import JsonResponse
#import weasyprint
#from weasyprint import HTML

# Create your views here.
# Function-based view for index page
def index(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render index.html with context
   return render(request, 'citisoft/user/index.html', context)

# Function-based view for settings page
def settings(request):  
   if 'clientId'  in request.session:  
      clientId = request.session['clientId'] 
      print("clientId",clientId)  
      client_info = Client.objects.get(pk=clientId)
      
      if request.method == "POST":    
         email =  request.POST["email"]
         password = request.POST['password']
         fullname = request.POST['fullname']
         confirm_password = request.POST['confirm_password']
         if password == confirm_password:
            client_info.email=email
            client_info.fullName=  fullname
            client_info.password = password
            client_info.save() 
            print("clientId","success") 
            messages.success(request,"Settings")
         else: 
            print("clientId","failed") 
            messages.warning(request,"Passwords do not match.")
      context =  {'client':client_info}
   else:
      print("clientId","Nothing")   
   return render(request, 'citisoft/user/settings.html', context)


def vendorSettings(request):  
   if 'vendorId'  in request.session:  
      vendorId = request.session['vendorId'] 
      print("vendorId",vendorId)  
      vendor_info = Vendor.objects.get(pk=vendorId)
      
      if request.method == "POST":    
         email =  request.POST["email"]
         password = request.POST['password']
         vendorname = request.POST['vendorname']
         confirm_password = request.POST['confirm_password']
         if password == confirm_password:
            vendor_info.email=email
            vendor_info.vendorName=  vendorname
            vendor_info.password = password
            vendor_info.save() 
            print("clientId","success") 
            messages.success(request,"Settings")
         else: 
            print("clientId","failed") 
            messages.warning(request,"Passwords do not match.")
      context =  {'client':vendor_info}
   else:
      print("clientId","Nothing")   
   return render(request, 'citisoft/vendor/vendorsettings.html')

# Function-based view for products page
def products(request,categoryId):   # Request handler
   print("categoryId",categoryId)
   category = Categories.objects.get(categoryId=categoryId)
   vendorCategories = VendorCategories.objects.filter(category=category)
   print("vendorCategories",vendorCategories)
   context = {'vendorCategories': vendorCategories}  
   return render(request, 'citisoft/user/products.html', context)

# Function-based view for home page
def home(request):   # Request handler
   categories = Categories.objects.all()
   context = {'categories': categories}   # Initialize context dictionary
   # Render home.html with context
   return render(request, 'citisoft/user/home.html', context)

# Function-based view for choice page
def choice(request, vendorCategoriesId):   # Request handler
      vendorCategory = VendorCategories.objects.get(vendorCategoriesId=vendorCategoriesId)
      context = {'vendorCategory': vendorCategory}   
      return render(request, 'citisoft/user/choice.html', context)

# Function-based view for cart page
def cartOperation(request, vendor_id):  
   company = Vendor.objects.get(vendorId=vendor_id)
   
   return redirect('choice', company) 

def cart(request):   # Request handler
     vendors = []
     if 'cart' in request.session:
        carts = request.session['cart']
        for cart in carts:
          print(cart)
          vendor =  Vendor.objects.get(pk=int(cart))
          vendors.append(vendor)
          if request.method == "POST" and 'clientId' in request.session:
             clientId = request.session['clientId']
             client = Client.objects.get(pk=clientId)
             for vendor in vendors:
                SavedVendors.objects.create(vendor=vendor, client=client,savedVendorsId=vendor.vendorId)
                
             del request.session['cart']
             return redirect('home')
          else:
            return render(request, 'citisoft/user/cart.html', {"vendors":vendors})
     else:
       return render(request, 'citisoft/user/cart.html', {"vendors":vendors}) 
   
   
      
def clientinfo(request):
    clients = []
    vendorId = request.session['vendorId']    
    savedVendors = SavedVendors.objects.all()
    for savedVendor in savedVendors:
       if savedVendor.vendor.vendorId == vendorId:
          clients.append(savedVendor.client)
          
    return render(request,'citisoft/vendor/clientinfo.html',{"clients":clients})
          
          
    



def pdf_view(request, vendor_id):
    # Retrieve the vendor object from the database
    company = get_object_or_404(Vendor, vendorId=vendor_id)

    # Create a PDF document using ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{company.vendorName}_details.pdf"'

    p = canvas.Canvas(response, pagesize=landscape(letter))

    # Set initial y-position and line height
    x_position = 10
    y_position = 550
    line_height = 25

    # Define paragraph style for multiline text
    paragraph_style = ParagraphStyle(name='Normal', fontSize= 8.5 , leading=12)

    # Write company details to PDF
    p.drawString(50, y_position, f"Company Name: {company.vendorName}")
    y_position -= line_height

    # Wrap and draw description
    description_text = Paragraph(company.description, paragraph_style)
    description_text.wrapOn(p, 700, 850)
    description_text.drawOn(p, x_position, y_position)
    y_position -= description_text.height
    # Write other company details
    details = [
        ("Email", company.email),
        ("Date Established", company.date_est),
        ("Location", company.location),
        ("Address", company.address),
        ("Contact Telephone", company.contact_tel),
        ("Number of Employees", company.num_of_eployees),
        ("International Professional Services", company.Int_pro_services),
        ("Business Areas", company.business_areas),
        ("Client Types", company.client_types),
        ("Cloud or Native", company.cloud_or_native),
        ("Additional Information", company.added_info),
    ]

    for detail_name, detail_value in details:
        detail_text = Paragraph( f"{detail_name}: {detail_value}", paragraph_style)
        detail_text.wrapOn(p, 700, 800)
        detail_text.drawOn(p, x_position, y_position)
        y_position -= detail_text.height
        y_position -= line_height

    p.showPage()
    p.save()

    return response

   #return render(request, 'citisoft/user/category.html', context)


def delete(request):   # Request handler
   context = {}
   if request.method == 'POST':
      if 'clientId' in request.session:
         clientId =  request.session['clientId']
         client = Client.objects.get(pk=clientId)
         client.delete()
         return redirect('index')
      else:
               # Neither client nor vendor found with provided credentials
               return HttpResponse("Invalid email or password.")
            
   return render(request, 'citisoft/user/delete.html', context)


def deleteVendor(request):   # Request handler
   context = {}
   if request.method == 'POST':
      if 'vendorId' in request.session:
         vendorId =  request.session['vendorId']
         vendor = Vendor.objects.get(pk=vendorId)
         vendor.delete()
         return redirect('index')
      else:
               # Neither client nor vendor found with provided credentials
               return HttpResponse("Invalid email or password.")
            
   return render(request, 'citisoft/vendor/vendordelete.html', context)


def userlogin(request):
   # Check if the request method is POST
   if request.method == 'POST':   
      # Extract email and password from the POST data
       email = request.POST["email"]
       password = request.POST['password']
        # Authenticate the client using the provided email and password
       client = authenticateClient(email, password)
       #if authentication is sucessful, print("client.id",client.pk) and redirect to home page 
       if client is not None:
          request.session['clientId'] = client.pk
          return redirect('home')
       #if auth fail display error message
       elif client is None:
          messages.error(request,"Invalid Email or Password")
          # Render the login page again
       return render(request, 'citisoft/user/userlogin.html')
    
   else:
     return render(request, 'citisoft/user/userlogin.html')  
       
     
          
          
       
       



def usersignup(request):   # Request handler
   countries = Country.objects.all() # Retrieve all countries from the database
   context = {'countries':countries}  # Create a context dictionary with countries data
   if request.method == 'POST':   # Check if the request method is POST
       print("signup1") # Print a message indicating the sign-up process has begun
       email = request.POST["email"] # Extract email from the POST data
       password = request.POST['password'] # Extract password from the POST data
       confirmPassword = request.POST['confirmPassword'] 
       name = request.POST['fullname']
       countrySelect = request.POST['countrySelect']
       country = Country.objects.get(pk=int(countrySelect))
       
        # Create a new Client object with the extracted data and save it to the database
       Client.objects.create(email=email, password=password, fullName=name,country=country)
       # Authenticate the client using the provided email and password
       client = authenticateClientSignIn(email, password,confirmPassword)
       #print("client.clientId",client.pk)
       if client is not None:
          print("signup2")
          request.session['clientId'] = client.pk
          return redirect('home') # Redirect the user to the home page
       else:
          print("signup3")
          messages.error(request,"Invalid Email or Password")
       return render(request, 'citisoft/user/usersignup.html')
     # If the request method is not POST, render the sign-up page with country data
   else:
      return render(request, 'citisoft/user/usersignup.html', context)


def vendor_home(request):   # Request handler
      if 'vendorId'  in request.session:  
         vendorId = request.session['vendorId'] 
         #print("vendorId",vendorId)  
         vendor = Vendor.objects.get(pk=vendorId)
         context = {'vendor':vendor}   
         return render(request, 'citisoft/vendor/vendor_home.html', context)
      else:
        return redirect('vendorlogin')

def vendorsignup(request):   # Request handler
   countries = Country.objects.all() # Retrieve all countries from the database
   context = {'countries':countries} # Create a context dictionary with countries data
   if request.method == 'POST':   # Check if the request method is POST
       print("signup1")   # Print a message for debugging
       email = request.POST["email"]
       password = request.POST['password']
       name = request.POST['vendorname']
       Vendor.objects.create(email=email, password=password, vendorName=name)
       vendor = authenticateVendorSignIn(email, password)
       #print("vendor.vendorId",vendor.pk)
       if vendor is not None:
          #print("signup2")
          request.session['vendorId'] = vendor.pk # Store the vendor ID in the session
          return redirect('vendor_home') # Redirect the vendor to the vendor home page
       else:
          #print("signup3")
          messages.error(request,"Invalid Email or Password")  # Display an error message
       return render(request, 'citisoft/vendor/vendorsignup.html') # Render the vendor sign-up page
    
   else:
      return render(request, 'citisoft/vendor/vendorsignup.html', context) # Render the vendor sign-up page with country data


def vendorlogin(request):   # Request handler
   if request.method == 'POST':   # Check if the request method is POST
       email = request.POST["email"]  # Extract email from the POST data
       password = request.POST['password'] # Extract password from the POST data
       vendor = authenticateVendor(email, password) # Authenticate the vendor using the provided email and password
       #print("vendor.vendorId",vendor.pk)
       if vendor is not None:
          request.session['vendorId'] = vendor.pk  # Store the vendor ID in the session
          return redirect('vendor_home')  # Redirect the vendor to the vendor home page
       else:
          messages.error(request,"Invalid Email or Password")  # Display an error message
       return render(request, 'citisoft/vendor/vendorlogin.html')  # Render the vendor login page
    
   else:
     return render(request, 'citisoft/vendor/vendorlogin.html')  # Render the vendor login page


def edits(request):   # Request handler
      if 'vendorId'  in request.session:  
         vendorId = request.session['vendorId'] 
        # print("vendorId",vendorId)  
         vendor = Vendor.objects.get(pk=vendorId)

         if request.method == "POST":    
            email =  request.POST["email"]
            confirm_email = request.POST["confirm_email"]
            description = request.POST['description']
            address = request.POST['address']
            contact = request.POST['contact_telephone']
            employees = request.POST['no_of_employees']
            int_pro_services = request.POST['int_pro_services']
            client_types = request.POST['client_types']
            cloud_or_native = request.POST['cloud_or_native']
            additional_information = request.POST['additional_information']
            business_areas = request.POST['business_areas']
            
            if email == confirm_email:
               vendor.description=description
               vendor.address=address
               vendor.contact_tel=contact
               vendor.num_of_eployees=employees
               vendor.Int_pro_services=int_pro_services
               vendor.client_types=client_types
               vendor.cloud_or_native=cloud_or_native
               vendor.added_info=additional_information
               vendor.business_areas=business_areas
               vendor.save() 
               print("vendorId","success") 
               messages.success(request,"edits")
            else: 
               print("vendorId","failed") 
               messages.warning(request,"emails do not match.")
         context =  {'vendor':vendor}
      else:
         print("clientId","Nothing") 
      return render(request, 'citisoft/vendor/edits.html', context)
   
      


def view(request):   # Request handler
   
      if 'vendorId'  in request.session:  
         vendorId = request.session['vendorId'] 
         print("vendorId",vendorId)  
         vendor = Vendor.objects.get(pk=vendorId)
         context = {'vendor':vendor}   
         return render(request, 'citisoft/vendor/view.html', context)
      else:
        return redirect('vendorlogin')
   




def vendorlogout(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render vendorlogout.html with context
   if 'vendorId' in request.session:
      del request.session['vendorId'] 
      
   return redirect("vendorlogin")
   #return render(request, 'citisoft/vendor/vendorlogout.html', context)


def logout(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render v.html with context
   if 'clientId' in request.session:
      del request.session['clientId'] 
      
   return redirect("index")


def authenticateClient(email,password):
   try:
      client = Client.objects.get(email=email)
      if client.password == password:
         return client
   except Client.DoesNotExist:
      return None
   
   
def authenticateClientSignIn(email,password,confirmPassword):
   try:
      client = Client.objects.get(email=email)
      if client.password == password and password == confirmPassword:
         return client
   except Client.DoesNotExist:
      return None
   

def authenticateVendor(email,password):
   try:
      vendor = Vendor.objects.get(email=email)
      if vendor.password == password:
         return vendor
   except Vendor.DoesNotExist:
      return None   
         
         
         
def authenticateVendorSignIn(email,password):
   try:
      vendor = Vendor.objects.get(email=email)
      if vendor.password == password :
         return vendor
   except Vendor.DoesNotExist:
      return None
   

def update_cart(request):
   print("ubon")
   request.session.modified = True
   data = json.loads(request.body)
   print('data', data)
   vendor_id = data['vendorId']
   vendor= Vendor.objects.get(pk=vendor_id)
   action =data['action']
   print('Action', action)
   print('vendor', vendor)
   cart =request.session.get('cart', {})  # get the cart dictionary from session or set it to an empty dict
   saved_item= cart.get(vendor.vendorId, {'amount':0})
   if action == 'add':
      saved_item['amount'] +=1
   elif action =='remove':
      saved_item['amount'] -=1
   cart[vendor.vendorId] =saved_item
   request.session['cart'] = cart
   if  saved_item['amount'] <= 0:
      del request.session['cart'][vendor.vendorId]
      del request.session['cart'][str(vendor.vendorId)]
      print('cart'.request.session['cart'])
   return JsonResponse('Added sucessfully', safe=False)

def saveVendor(request, vendor_id):
    # Retrieve the vendor object from the database
    company = get_object_or_404(Vendor, vendorId=vendor_id)
    
    
def search_Form(request, vendorName=None):
   #vendor = get_object_or_404(Vendor, vendorName=vendorName)
   vendors = Vendor.objects.all()
   #category = Categories.objects.get(categoryId=categoryId)
   #vendorCategories = VendorCategories.objects.filter(category=category)
   context = {'categories': vendors} 
   if request.method == 'POST': 
      search = request.POST['search_query']
     
      # Perform search in the "vendor" field
      matching_vendor = authSearch(search)
      print("vendor.vendorId", matching_vendor.vendorName)
      if matching_vendor is not None:
         return redirect( 'product',vendorName=matching_vendor.vendorName)
      else:
          messages.error(request,"vendor does not exist, try again")
      return render(request, 'citisoft/user/product.html', context)
   else:
      return render(request, 'citisoft/user/product.html', context)
   
   
   
   
   
   
def authSearch(search_query):
   try:
     vendor = Vendor.objects.get(vendorName=search_query) 
     if vendor.vendorName == search_query:
        return vendor
   except vendor.DoesNotExist:
      return None


def product(request,vendorName):   # Request handler
   print("categoryId",vendorName)
   category = Vendor.objects.get(vendorName=vendorName)
   vendorCategories = Vendor.objects.filter(vendorName=category)
   print("vendorCategories",vendorCategories)
   context = {'vendorCategories': category}  
   return render(request, 'citisoft/user/choice.html', context)

def cat(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render index.html with context
   
   return render(request, 'citisoft/user/category.html', context)


def search_vendors(request):
    # Check if the request method is POST
    if request.method == 'POST':
           # Extract the search query from the POST data
        search_query = request.POST.get('search_query')
          # If a search query is provided, filter vendors based on the query and render search results
        if search_query:
            vendors = Vendor.objects.filter(vendorName__icontains=search_query)
            return render(request, 'citisoft/user/search_results.html', {'vendors': vendors})
         # If request method is not POST or no search query provided, redirect to a predefined category page
    return redirect('category')
 
 
 
def vendor_info(request, vendorId):
    vendor = Vendor.objects.get(vendorId=vendorId)
    return render(request, 'citisoft/user/vendor_info.html', {'vendor': vendor})