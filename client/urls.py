from django.urls import path
from client import views

urlpatterns = [
    path('', views.render_home, name='home'),
    path('home', views.render_home, name='home'),
    path('admin', views.render_admin, name='admin'),
    path('disco', views.render_disco, name='disco'),
    path('instrumento', views.render_instrumento, name='instrumento'),
    path('grafico', views.render_grafico, name='grafico'),
    path('aprobar_productos', views.render_aprobar_productos, name='aprobar_productos'),
]