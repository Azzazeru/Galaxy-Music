from rest_framework import viewsets , generics

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import *


class SelloDiscograficoViewSet(viewsets.ModelViewSet):
    queryset = SelloDiscografico.objects.all()
    serializer_class = SelloDiscograficoSerializer

class GeneroMusicalViewSet(viewsets.ModelViewSet):
    queryset = GeneroMusical.objects.all()
    serializer_class = GeneroMusicalSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class DetalleDiscoViewSet(viewsets.ModelViewSet):
    queryset = DetalleDisco.objects.all()
    serializer_class = DetalleDiscoSerializer

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

class DiscoViewSet(viewsets.ModelViewSet):
    queryset = Disco.objects.all()
    serializer_class = DiscoSerializer

class TipoInstrumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoInstrumento.objects.all()
    serializer_class = TipoInstrumentoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class DetalleInstrumentoViewSet(viewsets.ModelViewSet):
    queryset = DetalleInstrumento.objects.all()
    serializer_class = DetalleInstrumentoSerializer

class InstrumentoViewSet(viewsets.ModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        instrumento_id = self.request.query_params.get('instrumento')
        disco_id = self.request.query_params.get('disco')

        detalle_instrumento_id = self.request.query_params.get('detalle_instrumento')

        
        if instrumento_id is not None:
            queryset = queryset.filter(instrumento_id=instrumento_id)
        elif disco_id is not None:
            queryset = queryset.filter(disco_id=disco_id)

        if detalle_instrumento_id is not None:
            queryset = queryset.filter(instrumento__detalle_instrumento_id=detalle_instrumento_id)

        return queryset
    
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer