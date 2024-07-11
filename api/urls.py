from django.urls import path, include
from rest_framework import routers

from .views import DiscoViewSet, InstrumentoViewSet, ProductoViewSet, SelloDiscograficoViewSet, \
                    TipoInstrumentoViewSet, EspecieInstrumentoViewSet, MarcaInstrumentoViewSet,  \
                    TipoDiscoViewSet, DetalleBoletaViewSet, GeneroMusicalViewSet, \
                    BoletaViewSet, ArtistaViewSet, PresupuestoViewSet, \
                    PresupuestoReadViewSet, DiscoReadViewSet, InstrumentoReadViewSet, \
                    ProductoReadViewSet


public_router = routers.DefaultRouter()
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
public_router.register(r'discos', DiscoReadViewSet)
public_router.register(r'instrumentos', InstrumentoReadViewSet)
public_router.register(r'productos', ProductoReadViewSet)

hidden_router = routers.DefaultRouter()
hidden_router.register(r'productos', ProductoViewSet)
hidden_router.register(r'presupuesto', PresupuestoViewSet)
hidden_router.register(r'discos', DiscoViewSet)
hidden_router.register(r'instrumentos', InstrumentoViewSet)



urlpatterns = [
    path('hidden/', include(hidden_router.urls)),
    path('public/', include(public_router.urls)),
]
