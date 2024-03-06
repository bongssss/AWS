from django.db import models
from django.contrib.auth.models import User
#from .models import Vendor
# Create your models here.



class Vendorr(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    genre= models.CharField(max_length=150, null=True)  # The category of the product 
    #client =  models.ManyToManyField(Client, related_name='client_product')
    description = models.CharField(max_length=2000, null=True)
    date_est = models.DateField()
    location= models.CharField(max_length=1250, null=True)
    address =  models.CharField(max_length=3000, null=True)
    contact_tel = models.CharField(max_length=2500, null=True)
    num_of_eployees = models.IntegerField( null=True)
    Int_pro_services=models.CharField(max_length=400, null=True)
    business_areas=models.CharField(max_length=400, null=True)
    client_types=models.CharField(max_length=400, null=True)
    cloud_or_native=models.CharField(max_length=100, null=True)
    added_info=models.CharField(max_length=600, null=True)
    
 

    def __str__(self):
	    return self.name





class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    saved_vendor = models.ManyToManyField(Vendorr, null=True, blank=True)
   
 

    def __str__(self):
	    return self.name

 




class Saved_vendor(models.Model):
   # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    #email = models.CharField(max_length=200)
    #saved_vendor = models.ManyToManyField(Vendorr, null=True, blank=True)
    

 

    def __str__(self):
	    return self.name



 
 
 
