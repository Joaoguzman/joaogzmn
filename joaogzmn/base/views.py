from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def posts(request):
    return render(request, 'base/posts.html')

def researchandopinion(request):
    return render(request, 'base/research&opinion.html')
    
def profile(request):
    return render(request, 'base/profile.html')