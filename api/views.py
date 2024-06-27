from rest_framework import viewsets


from .models import *
from .serializer import *

from functools import wraps
from django.core.exceptions import PermissionDenied

def login_required_api(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Acceso denegado. Debes iniciar sesión.")
        return view_func(self, request, *args, **kwargs)
    return wrapped_view

#ONLY LOGIN REQURED API

class DiscoViewSet(viewsets.ModelViewSet):
    queryset = Disco.objects.all()
    serializer_class = DiscoSerializer

    @login_required_api
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class InstrumentoViewSet(viewsets.ModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

    @login_required_api
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    @login_required_api
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer

    @login_required_api
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#Aparte ONLY GET 

class ArtistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class SelloDiscograficoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SelloDiscografico.objects.all()
    serializer_class = SelloDiscograficoSerializer

class GeneroMusicalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GeneroMusical.objects.all()
    serializer_class = GeneroMusicalSerializer

class TipoDiscoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoDisco.objects.all()
    serializer_class = TipoDiscoSerializer

class PresupuestoReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer

class TipoInstrumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoInstrumento.objects.all()
    serializer_class = TipoInstrumentoSerializer

class EspecieInstrumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EspecieInstrumento.objects.all()
    serializer_class = EspecieInstrumentoSerializer

class MarcaInstrumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarcaInstrumento.objects.all()
    serializer_class = MarcaInstrumentoSerializer

class BoletaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class DetalleBoletaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleBoleta.objects.all()
    serializer_class = DetalleBoletaSerializer

class DiscoReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Disco.objects.all()
    serializer_class = DiscoSerializer

class InstrumentoReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

class ProductoReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer