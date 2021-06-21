from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#import models here
from .models import Listing
# Create your views here.
def index(request):

    #set variable to show the listings
    listings = Listing.objects.all()
    # pagination coding
    paginator = Paginator(listings, 3) # pagging 3 per page
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)   
    context = {
        'listings': paged_listings#listings
    } 
    return render(request, 'listings/listings.html',context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')