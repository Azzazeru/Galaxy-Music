from django.shortcuts import render

# Create your views here.

def render_home(request):
    return render(request, 'home.html')

def render_crudProduct(request):
    return render(request, 'crudProduct.html')