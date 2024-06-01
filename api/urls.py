from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'sellos_discograficos', SelloDiscograficoViewSet)
router.register(r'generos_musicales', GeneroMusicalViewSet)
router.register(r'artistas', ArtistaViewSet)
router.register(r'detalles_discos', DetalleDiscoViewSet)
router.register(r'canciones', CancionViewSet)
router.register(r'discos', DiscoViewSet)
router.register(r'tipos_instrumentos', TipoInstrumentoViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'detalles_instrumentos', DetalleInstrumentoViewSet)
router.register(r'instrumentos', InstrumentoViewSet)
router.register(r'productos', ProductoViewSet)
# router.register(r'profiles', profile)


urlpatterns = [
    path('', include(router.urls)),
    re_path('login', login),
    re_path('register', register),
    re_path('profile', profile),
]
