from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def backend(request):
    return render(request, 'base/backend.html')

def researchopinion(request):
    return render(request, 'base/researchopinion.html')
    
def spatial_datascience(request):
    return render(request, 'base/spatial_datascience.html')

def devops(request):
    return render(request, 'base/devops.html')

def contact(request):
    return render(request, 'base/contact.html')