from django.urls import path
# now second thing is to import views
from . import views
#path(firstparam='path define in this case is root or home',method,method name)
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
