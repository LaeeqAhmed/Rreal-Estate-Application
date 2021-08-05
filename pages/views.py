from django.shortcuts import render
from django.http import HttpResponse
# importing models
from listings.models import Listing
from realtors.models import Realtor

# import all the choices here for search form

from listings.choices import bedroom_choices, state_choices, price_choices

'''
method bellow
templates rendering
'''


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,

    }
    return render(request, 'pages/index.html', context)


# about method
def about(request):
    # get all realtors
    get_all_realtors = Realtor.objects.order_by('-hire_date')
    # seller of the month
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'get_all_realtors': get_all_realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
