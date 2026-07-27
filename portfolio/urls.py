
from django.contrib import admin
from django.urls import path

from .import views


urlpatterns = [
   
    path('' , views.home_view , name="home"),
    path('about/', views.about_view, name='about'),
    path('project/', views.project_view, name='project'),
    path('contact/', views.contact_view, name='contact'),
    path('competence/', views.competence_view, name='competence'),
    
    path('static/', views.static_view, name='static'),
    path('style/', views.style_view, name='css'),
    path('js/', views.js_view, name='js'),
    
   
   
]
