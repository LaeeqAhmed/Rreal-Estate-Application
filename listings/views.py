from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#import models here
from .models import Listing

from listings.choices import bedroom_choices, price_choices, state_choices
# Create your views here.
def index(request):

    #set variable to show the listings
    #so set the lsitings to show on front page order by the date so the last enter show first in the database
    #listings = Listing.objects.all()if filter is_published is false then not show on frontend
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # pagination coding
    paginator = Paginator(listings, 3) # pagging 3 per page
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)   
    context = {
        'listings': paged_listings#listings
    } 
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    query_list = Listing.objects.order_by('-list_date')
    #working on keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

    #working on city search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    #working on state search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

    #working on bedrooms search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)
    #WORKING ON PRICE SEARCH
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'query_list': query_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)