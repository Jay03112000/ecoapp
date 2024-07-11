from django.urls import path,include
from ecoapp.jay import urls as jay_urls
from ecoapp.virag import urls as virag_urls

urlpatterns = [

    path('',include(virag_urls)),
    path('',include(jay_urls)),


]