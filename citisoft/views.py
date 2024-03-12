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

def cart(request, vendor_id):   # Request handler
      vendor_id= Vendor.vendorId
      if request.user.is_authenticated:
         client = request.user.client
         saveorder, created = SaveOrder.objects.get_or_create(client=client)
         items = saveorder.saveorderitem_set.all()
      else:
         #Create empty cart for now for non-logged in user
         items = []
      context = {'items':items} 
      
      return render(request, 'citisoft/user/cart.html', context)



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
   context = {}   # Initialize context dictionary
   # Render delete.html with context
   return render(request, 'citisoft/user/delete.html', context)


def userlogin(request):
   if request.method == 'POST':
       email = request.POST["email"]
       password = request.POST['password']
       client = authenticateClient(email, password)
       print("client.id",client.pk)
       if client is not None:
          request.session['clientId'] = client.pk
          return redirect('home')
       else:
          messages.error(request,"Invalid Email or Password")
       return render(request, 'citisoft/user/userlogin.html')
    
   else:
     return render(request, 'citisoft/user/userlogin.html')  
       
       
       



def usersignup(request):   # Request handler
   countries = Country.objects.all()
   
   if request.method == 'POST':
       email = request.POST["email"]
       password = request.POST['password']
       fullname = request.POST['fullname']
       client = authenticateClientSignIn(email, password, fullname)
       context = {'countries':countries}
       print("client.id",client.pk)
       if client is not None:
          request.session['clientId'] = client.pk
          return redirect('home')
       else:
          messages.error(request,"Invalid Email or Password")
       return render(request, 'citisoft/user/usersignup.html')
    
   else:
    
    return render(request, 'citisoft/user/usersignup.html', context)


def vendor_home(request):   # Request handler
      if 'vendorId'  in request.session:  
         vendorId = request.session['vendorId'] 
         print("vendorId",vendorId)  
         vendor = Vendor.objects.get(pk=vendorId)
         context = {'vendor':vendor}   
         return render(request, 'citisoft/vendor/vendor_home.html', context)
      else:
        return redirect('vendorlogin')

def vendorsignup(request):   # Request handler
   countries = Country.objects.all()
   
   if request.method == 'POST':
       email = request.POST["email"]
       password = request.POST['password']
       name = request.POST['vendorname']
       vendor = authenticateVendorSignIn(email, password, name)
       context = {'countries':countries}
       print("vendor.vendorId",vendor.pk)
       
       if vendor is not None:
          request.session['vendorId'] = vendor.pk
          return redirect('vendor_home')
       else:
          messages.error(request,"Invalid Email or Password")
       return render(request, 'citisoft/user/usersignup.html')
    
   else:
      return render(request, 'citisoft/vendor/vendorsignup.html', context)


def vendorlogin(request):   # Request handler
   if request.method == 'POST':
       email = request.POST["email"]
       password = request.POST['password']
       vendor = authenticateVendor(email, password)
       print("vendor.vendorId",vendor.pk)
       if vendor is not None:
          request.session['vendorId'] = vendor.pk
          return redirect('vendor_home')
       else:
          messages.error(request,"Invalid Email or Password")
       return render(request, 'citisoft/vendor/vendorlogin.html')
    
   else:
     return render(request, 'citisoft/vendor/vendorlogin.html')  


def edits(request):   # Request handler
      if 'vendorId'  in request.session:  
         vendorId = request.session['vendorId'] 
         print("vendorId",vendorId)  
         vendor = Vendor.objects.get(pk=vendorId)
         
         context = {'vendor':vendor}   
         return render(request, 'citisoft/vendor/edits.html', context)
      else:
        return redirect('vendorlogin')
   


def view(request):   # Request handler
   
      if 'vendorId'  in request.session:  
         vendorId = request.session['vendorId'] 
         print("vendorId",vendorId)  
         vendor = Vendor.objects.get(pk=vendorId)
         context = {'vendor':vendor}   
         return render(request, 'citisoft/vendor/view.html', context)
      else:
        return redirect('vendorlogin')
   

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
   
   
def authenticateClientSignIn(email,password, fullname):
   try:
      client = Client.objects.get(email=email)
      if client.password == password and  client.fullName == fullname:
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
         
         
         
def authenticateVendorSignIn(email,password, name):
   try:
      vendor = Vendor.objects.get(email=email)
      if vendor.password == password and  vendor.vendorName == name:
         return vendor
   except Client.DoesNotExist:
      return None