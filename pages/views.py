from django.shortcuts import render
from django.http import HttpResponse
'''
method bellow
templates rendering
'''
def index(request):
    return render(request, 'pages/index.html')


#about method
def about(request):
    return render(request, 'pages/about.html')
