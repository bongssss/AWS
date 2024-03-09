from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Vendor)
admin.site.register(Client)
admin.site.register(Categories)
admin.site.register(VendorCategories)
admin.site.register(SavedVendors)
admin.site.register(Country)
admin.site.register(SaveOrder)
admin.site.register(SaveOrderItem)