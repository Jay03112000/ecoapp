from django.shortcuts import render


def home(request):
    return render(request, 'virag/home.html')

def about(request):
    return render(request, 'about.html')
