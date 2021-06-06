from django.contrib import admin

# Register your models here. to manipulate with respect to the admin area
#import first models here
from .models import Listing

#make class
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','price','zipcode','state')
    list_per_page = 25 #pagination
#calling
admin.site.register(Listing, ListingAdmin)
