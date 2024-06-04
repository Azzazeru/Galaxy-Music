from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User

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
    sello_discografico_id = serializers.PrimaryKeyRelatedField(queryset=SelloDiscografico.objects.all(), source='sello_discografico', write_only=True)
    genero_musical_id = serializers.PrimaryKeyRelatedField(queryset=GeneroMusical.objects.all(), source='genero_musical', write_only=True)
    artista_id = serializers.PrimaryKeyRelatedField(queryset=Artista.objects.all(), source='artista', write_only=True)
    
    sello_discografico = SelloDiscograficoSerializer(read_only=True)
    genero_musical = GeneroMusicalSerializer(read_only=True)
    artista = ArtistaSerializer(read_only=True)

    class Meta:
        model = DetalleDisco
        fields = [
            'id_detalle_disco',
            'sello_discografico', 'sello_discografico_id',
            'genero_musical', 'genero_musical_id',
            'artista', 'artista_id'
        ]

class DiscoSerializer(serializers.ModelSerializer):
    detalle_disco_id = serializers.PrimaryKeyRelatedField(queryset=DetalleDisco.objects.all(), source='detalle_disco', write_only=True)
    detalle_disco = DetalleDiscoSerializer(read_only=True)

    class Meta:
        model = Disco
        fields = ['id_disco', 'titulo', 'detalle_disco', 'detalle_disco_id']

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
    tipo_instrumento_id = serializers.PrimaryKeyRelatedField(queryset=TipoInstrumento.objects.all(), source='tipo_instrumento', write_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source='marca', write_only=True)
    
    tipo_instrumento = TipoInstrumentoSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)

    class Meta:
        model = DetalleInstrumento
        fields = [
            'id_detalle_instrumento',
            'descripcion',
            'tipo_instrumento', 'tipo_instrumento_id',
            'marca', 'marca_id'
        ]

class InstrumentoSerializer(serializers.ModelSerializer):
    detalle_instrumento_id = serializers.PrimaryKeyRelatedField(queryset=DetalleInstrumento.objects.all(), source='detalle_instrumento', write_only=True)
    detalle_instrumento = DetalleInstrumentoSerializer(read_only=True)

    class Meta:
        model = Instrumento
        fields = ['id_instrumento', 'modelo', 'detalle_instrumento', 'detalle_instrumento_id']

class ProductoSerializer(serializers.ModelSerializer):
    disco_id = serializers.PrimaryKeyRelatedField(queryset=Disco.objects.all(), source='disco', write_only=True, allow_null=True, required=False)
    instrumento_id = serializers.PrimaryKeyRelatedField(queryset=Instrumento.objects.all(), source='instrumento', write_only=True, allow_null=True, required=False)
    disco = DiscoSerializer(read_only=True)
    instrumento = InstrumentoSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']