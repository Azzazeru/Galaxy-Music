from rest_framework import serializers
from .models import *



class DiscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disco
        fields = '__all__'

class InstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    disco_id = serializers.PrimaryKeyRelatedField(queryset=Disco.objects.all(), source='disco', write_only=True, allow_null=True, required=False)
    instrumento_id = serializers.PrimaryKeyRelatedField(queryset=Instrumento.objects.all(), source='instrumento', write_only=True, allow_null=True, required=False)
    disco = DiscoSerializer(read_only=True)
    instrumento = InstrumentoSerializer(read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

## Aparte

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class SelloDiscograficoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelloDiscografico
        fields = '__all__'

class GeneroMusicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroMusical
        fields = '__all__'

class TipoDiscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDisco
        fields = '__all__'

class TipoInstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInstrumento
        fields = '__all__'

class EspecieInstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspecieInstrumento
        fields = '__all__'

class PresupuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuesto
        fields = '__all__'

class MarcaInstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaInstrumento
        fields = '__all__'

class DetalleBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleBoleta
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    detalles = DetalleBoletaSerializer(many=True, read_only=True)

    class Meta:
        model = Boleta
        fields = '__all__'