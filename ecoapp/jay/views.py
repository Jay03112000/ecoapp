from django.shortcuts import render

def contact(request):
    return render(request,'jay/contact.html')

def review(request):
    return render(request, 'jay/review.html' )