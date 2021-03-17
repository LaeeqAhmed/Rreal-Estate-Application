from django.shortcuts import render
from django.http import HttpResponse
'''
method bellow
templates rendering
'''
def index(request):
    return HttpResponse('<h1>first effort result</h1>')
