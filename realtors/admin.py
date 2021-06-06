from django.contrib import admin

# Register your models here. realtor model..
from .models import Realtor

#make class
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id', 'name')

#calling
admin.site.register(Realtor,RealtorAdmin)
