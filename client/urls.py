from django.urls import path
from client import views

urlpatterns = [
    path('', views.render_home, name='home'),
    path('home', views.render_home, name='home'),
    path('crudProduct', views.render_crudProduct, name='crudProduct')
]