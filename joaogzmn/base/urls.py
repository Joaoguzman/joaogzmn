from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('backend/', views.backend, name='backend'),
    path('researchopinion/', views.researchopinion, name='researchopinion'),
    path('spatial_datascience/', views.spatial_datascience, name='spatial_datascience'),
    path('devops/', views.devops, name='devops'),
    path('contact/', views.contact, name='contact'),

]