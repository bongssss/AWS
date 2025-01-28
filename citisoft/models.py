from django.db import models
from django.contrib.auth.models import User
#from .models import Vendor
# Create your models here.



class Vendor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    vendorName = models.CharField(max_length=200, null=True,default="")
    email = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True)
    date_est = models.DateTimeField(auto_now_add=True)
    location= models.CharField(max_length=1250, null=True)
    address =  models.CharField(max_length=3000, null=True)
    contact_tel = models.CharField(max_length=2500, null=True)
    num_of_eployees = models.IntegerField( null=True)
    Int_pro_services=models.CharField(max_length=400, null=True)
    business_areas=models.CharField(max_length=400, null=True)
    client_types=models.CharField(max_length=400, null=True)
    cloud_or_native=models.CharField(max_length=100, null=True)
    added_info=models.CharField(max_length=600, null=True)
    vendorId = models.AutoField(primary_key=True)
    password = models.CharField(max_length=200,null=True)
    website = models.URLField(null=True)
    da
 

    def __str__(self):
	    return self.vendorName


class Country(models.Model):
    countryName = models.CharField(max_length=200, null=True)
    countryId = models.AutoField(primary_key=True)
    def __str__(self):
        return self.countryName 


class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=200, null=True,default="")
    email = models.CharField(max_length=200)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    password = models.CharField(max_length=200,null=True)
   
 

    def __str__(self):
	    return self.fullName

 

class Categories(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    categoryId = models.AutoField(primary_key=True)
    def __str__(self):
        return self.categoryName
    
   

class VendorRating(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    review = models.CharField(max_length=200, null=True)
    rating = models.FloatField(max_length=200)
    vendorRatingId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.vendor.vendorName
 
class VendorCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendorCategoriesId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.vendor.vendorName


class SavedVendors(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    savedVendorsId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.vendor.vendorName
    
    
    
class SaveOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    saveOrderId = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

 
 
 
class SaveOrderItem(models.Model):
    saveorder = models.ForeignKey(SaveOrder, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    