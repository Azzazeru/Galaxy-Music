from django.db import models

# Disco
class Disco(models.Model):
    id_disco = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, unique=True)

    fecha_lanzamiento = models.DateField(null=True)
    tipo_disco = models.CharField(max_length=100, default='')

    sello_discografico = models.CharField(max_length=100, default='')
    genero_musical = models.CharField(max_length=100, default='')
    artista = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.titulo
    
# Instrumento
class Instrumento(models.Model):
    id_instrumento = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100, unique=True)

    descripcion = models.CharField(max_length=100, default='')
    tipo_instrumento = models.CharField(max_length=100, default='')
    marca = models.CharField(max_length=100, default='')
    especie = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.modelo

# Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    disco = models.OneToOneField(Disco, null=True, blank=True, on_delete=models.CASCADE)
    instrumento = models.OneToOneField(Instrumento, null=True, blank=True, on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    estado = models.BooleanField(default=False)

# Usuario

# class Usuario(models.Model):
#     id_usuario = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     contrasenia = models.CharField(max_length=100)

## Aparte Disco

# Artista

class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class SelloDiscografico(models.Model):
    id_sello_discografico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class GeneroMusical(models.Model):
    id_genero_musical = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class TipoDisco(models.Model):
    id_tipo_disco = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

## Aparte Instrumento

class TipoInstrumento(models.Model):
    id_tipo_instrumento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)

class EspecieInstrumento(models.Model):
    id_especie_instrumento = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=100)

class MarcaInstrumento(models.Model):
    id_marca_instrumento = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)

class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    presupuesto = models.IntegerField()

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    productos = models.ManyToManyField(Producto, through='DetalleBoleta')
    fecha_venta = models.DateField(auto_now_add=True)
    total = models.PositiveIntegerField(default=0)

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
