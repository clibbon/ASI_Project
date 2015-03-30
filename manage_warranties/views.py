from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the index") 

def importer_page(request):
    return HttpResponse("Welcome to the importers page")

def information_page(request):
    return HttpResponse("Welcome to the information page")