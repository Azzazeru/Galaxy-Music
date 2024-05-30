from django.shortcuts import render

# Create your views here.

def render_home(request):
    return render(request, 'home.html')

def render_admin(request):
    return render(request, 'admin.html')

def render_disco(request):
    return render(request, 'disco.html')

def render_grafico(request):
    return render(request, 'grafico.html')