from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.template import loader
from .models import *
from .models import Vendorr
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter  # Assuming letter size for the PDF
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph

#import weasyprint
#from weasyprint import HTML

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
      vendor = get_object_or_404(Vendorr, id=vendor_id)  # Get the requested product or display a 404 error if it
      context = {'VENDOR': vendor}   # Initialize context dictionary
   # Render choice.html with context
      return render(request, 'citisoft/user/choice.html', context)

# Function-based view for cart page
def cartOperation(request, vendor_id):   # Request handler
   company = Vendorr.objects.get(id=vendor_id)
   # Save the company name to the database
   Saved_vendor.objects.create(name=company.name)    
   #context = {}   # Initialize context dictionary
   # Render cart.html with context
   return redirect('choice', vendor_id=vendor_id) 

def cart(request):   # Request handler
   vendor = Vendorr.objects.all()
   saved =  Saved_vendor.objects.all()
   context = {'Vendors': vendor, 'saved_vend': saved}   # Initialize context dictionary
   # Render products.html with context
   return render(request, 'citisoft/user/cart.html', context)



def pdf_view(request, vendor_id):
    # Retrieve the vendor object from the database
    company = get_object_or_404(Vendorr, id=vendor_id)

    # Create a PDF document using ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{company.name}_details.pdf"'

    p = canvas.Canvas(response, pagesize=landscape(letter))

    # Set initial y-position and line height
    x_position = 10
    y_position = 550
    line_height = 25

    # Define paragraph style for multiline text
    paragraph_style = ParagraphStyle(name='Normal', fontSize= 8.5 , leading=12)

    # Write company details to PDF
    p.drawString(50, y_position, f"Company Name: {company.name}")
    y_position -= line_height

    # Wrap and draw description
    description_text = Paragraph(company.description, paragraph_style)
    description_text.wrapOn(p, 700, 850)
    description_text.drawOn(p, x_position, y_position)
    y_position -= description_text.height
    # Write other company details
    details = [
        ("Email", company.email),
        ("Genre", company.genre),
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