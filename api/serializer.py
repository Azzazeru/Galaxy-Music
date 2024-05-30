# myapp/serializers.py

from rest_framework import serializers
from .models import *

class SelloDiscograficoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelloDiscografico
        fields = ['id_sello_discografico', 'nombre']

class GeneroMusicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroMusical
        fields = ['id_genero_musical', 'nombre']

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['id_artista', 'nombre']

class DetalleDiscoSerializer(serializers.ModelSerializer):
    sello_discografico = SelloDiscograficoSerializer()
    genero_musical = GeneroMusicalSerializer()
    artista = ArtistaSerializer()

    class Meta:
        model = DetalleDisco
        fields = ['id_detalle_disco', 'sello_discografico', 'genero_musical', 'artista']

class DiscoSerializer(serializers.ModelSerializer):
    detalle_disco = DetalleDiscoSerializer()

    class Meta:
        model = Disco
        fields = ['id_disco', 'titulo', 'detalle_disco']

class CancionSerializer(serializers.ModelSerializer):
    artista = ArtistaSerializer()
    genero_musical = GeneroMusicalSerializer()
    disco = DiscoSerializer()

    class Meta:
        model = Cancion
        fields = ['id_cancion', 'titulo', 'artista', 'genero_musical', 'disco']

class TipoInstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInstrumento
        fields = ['id_tipo_instrumento', 'tipo']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id_marca', 'nombre']

class DetalleInstrumentoSerializer(serializers.ModelSerializer):
    tipo_instrumento = TipoInstrumentoSerializer()
    marca = MarcaSerializer()

    class Meta:
        model = DetalleInstrumento
        fields = ['id_detalle_instrumento', 'descripcion', 'tipo_instrumento', 'marca']

class InstrumentoSerializer(serializers.ModelSerializer):
    detalle_instrumento = DetalleInstrumentoSerializer()

    class Meta:
        model = Instrumento
        fields = ['id_instrumento', 'modelo', 'detalle_instrumento']

class ProductoSerializer(serializers.ModelSerializer):
    disco = DiscoSerializer()
    instrumento = InstrumentoSerializer()

    class Meta:
        model = Producto
        fields = ['id_producto', 'disco', 'instrumento', 'precio', 'stock']
