from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('backend/', views.backend, name='backend'),
    path('researchopinion/', views.researchopinion, name='researchopinion'),
    path('machinelearning/', views.machinelearning, name='machinelearning'),
    path('representationlearning/', views.representationlearning, name='representationlearning'),
    path('contact/', views.contact, name='contact'),

]