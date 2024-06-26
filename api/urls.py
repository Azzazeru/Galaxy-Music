from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()
router.register(r'discos', DiscoViewSet)
router.register(r'instrumentos', InstrumentoViewSet)
router.register(r'productos', ProductoViewSet)

router.register(r'usuarios', UsuarioViewSet)
router.register(r'artistas', ArtistaViewSet)
router.register(r'sellos', SelloDiscograficoViewSet)
router.register(r'generos', GeneroMusicalViewSet)
router.register(r'tipodiscos', TipoDiscoViewSet)
router.register(r'tipoinstrumento', TipoInstrumentoViewSet)
router.register(r'especieinstrumento', EspecieInstrumentoViewSet)
router.register(r'marcainstrumento', MarcaInstrumentoViewSet)

router.register(r'boleta', BoletaViewSet)
router.register(r'detalleboleta', DetalleBoletaViewSet)

router.register(r'presupuesto', PresupuestoViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
