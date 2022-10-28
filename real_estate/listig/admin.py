from django.contrib import admin
from .models import *
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'num_bedrooms','num_bathrooms','square_footage','address')

admin.site.register(Listing)
