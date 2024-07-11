from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home page '),
    path('about/',views.about,name='about page '),
]