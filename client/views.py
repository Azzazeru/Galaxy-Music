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

def render_instrumento(request):
    return render(request, 'instrumento.html')

def render_aprobar_productos(request):
    return render(request, 'aprobar_productos.html')