from django.shortcuts import render

#import models here
from .models import Listing
# Create your views here.
def index(request):
    #set variable to show the listings
    listings = Listing.objects.all()   
    context = {
        'listings': listings
    } 
    return render(request, 'listings/listings.html',context)


def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')