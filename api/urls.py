from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import *

public_router = routers.DefaultRouter()
public_router.register(r'discos', DiscoReadViewSet)
public_router.register(r'instrumentos', InstrumentoReadViewSet)
public_router.register(r'productos', ProductoReadViewSet)
public_router.register(r'artistas', ArtistaViewSet)
public_router.register(r'sellos', SelloDiscograficoViewSet)
public_router.register(r'generos', GeneroMusicalViewSet)
public_router.register(r'tipodiscos', TipoDiscoViewSet)
public_router.register(r'tipoinstrumento', TipoInstrumentoViewSet)
public_router.register(r'especieinstrumento', EspecieInstrumentoViewSet)
public_router.register(r'marcainstrumento', MarcaInstrumentoViewSet)
public_router.register(r'boleta', BoletaViewSet)
public_router.register(r'detalleboleta', DetalleBoletaViewSet)
public_router.register(r'presupuesto', PresupuestoReadViewSet)

hidden_router = routers.DefaultRouter()
hidden_router.register(r'discos', DiscoViewSet)
hidden_router.register(r'instrumentos', InstrumentoViewSet)
hidden_router.register(r'productos', ProductoViewSet)
hidden_router.register(r'presupuesto', PresupuestoViewSet)

urlpatterns = [
    path('hidden/', include(hidden_router.urls)),
    path('public/', include(public_router.urls)),
]
