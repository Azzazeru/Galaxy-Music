from rest_framework import viewsets

from .models import *
from .serializer import *

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status


class DiscoViewSet(viewsets.ModelViewSet):
    queryset = Disco.objects.all()
    serializer_class = DiscoSerializer

class InstrumentoViewSet(viewsets.ModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#Aparte

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

class PresupuestoViewSet(viewsets.ModelViewSet):
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
