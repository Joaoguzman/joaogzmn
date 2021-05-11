from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('backend/', views.backend, name='backend'),
    path('research&opinion/', views.researchandopinion, name='researchandopinion'),
    path('spatial_datascience/', views.spatial_datascience, name='spatial_datascience'),
    path('devops/', views.devops, name='devops'),
    path('contact/', views.contact, name='contact'),

]