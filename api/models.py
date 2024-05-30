from django.db import models

# Sello discográfico
class SelloDiscografico(models.Model):
    id_sello_discografico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Género musical
class GeneroMusical(models.Model):
    id_genero_musical = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Artista
class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Detalle del disco
class DetalleDisco(models.Model):
    id_detalle_disco = models.AutoField(primary_key=True)
    sello_discografico = models.ForeignKey(SelloDiscografico, on_delete=models.CASCADE)
    genero_musical = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

# Canción
class Cancion(models.Model):
    id_cancion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    genero_musical = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)
    disco = models.ForeignKey('Disco', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo

# Disco
class Disco(models.Model):
    id_disco = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    detalle_disco = models.ForeignKey(DetalleDisco, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

# Tipo de instrumento
class TipoInstrumento(models.Model):
    id_tipo_instrumento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

# Marca
class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Detalle del instrumento
class DetalleInstrumento(models.Model):
    id_detalle_instrumento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, default='')
    tipo_instrumento = models.ForeignKey(TipoInstrumento, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

# Instrumento
class Instrumento(models.Model):
    id_instrumento = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    detalle_instrumento = models.ForeignKey(DetalleInstrumento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.modelo

# Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    disco = models.ForeignKey(Disco, null=True, blank=True, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, null=True, blank=True, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

