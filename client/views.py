from django.shortcuts import render
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib.auth import logout
# Create your views here.

def boss_required(user):
    return user.is_staff

boss_required = user_passes_test(boss_required)

def render_login(request):
    return render(request, 'login.html')

def render_admin(request):
    return render(request, 'admin.html')

@login_required
def render_disco(request):
    return render(request, 'disco.html')

def render_grafico(request):
    return render(request, 'grafico.html')

@login_required
def render_instrumento(request):
    return render(request, 'instrumento.html')

@boss_required
def render_aprobar_productos(request):
    

    return render(request, 'aprobar_productos.html')

def exit_page(request):
    logout(request)
    return render(request, 'admin.html')
