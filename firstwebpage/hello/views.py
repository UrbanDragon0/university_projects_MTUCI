from django.shortcuts import render

def index(request):
    return render(request, 'Hello/index.html')

def static_handler(request):
    return render(request, 'Hello/static_handler.html')
