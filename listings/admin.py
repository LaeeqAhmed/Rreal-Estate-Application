from django.contrib import admin

# Register your models here. to manipulate with respect to the admin area

from .models import Listing
admin.site.register(Listing)
