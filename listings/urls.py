from django.urls import path
# now second thing is to import views
from . import views
#path(firstparam='path define in this case is root or home',method,method name)
urlpatterns = [
    path('', views.index, name='listings'), #multiple listing
    path('<int:listing_id>', views.listing, name='listing'), #single listing
    path('search', views.search, name='search')
]