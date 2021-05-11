from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('research&opinion/', views.researchandopinion, name='researchandopinion'),
    path('profile/', views.profile, name='profile'),
]