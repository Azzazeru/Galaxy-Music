from django.urls import path
from client import views

urlpatterns = [
    path('', views.render_home, name='home'),
]