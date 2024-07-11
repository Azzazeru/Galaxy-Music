from django.db import models

# Clase Disco
class Disco(models.Model):
    id_disco = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, unique=True)
    fecha_lanzamiento = models.DateField(null=True)
    tipo_disco = models.CharField(max_length=100, default='')
    sello_discografico = models.CharField(max_length=100, default='')
    genero_musical = models.CharField(max_length=100, default='')
    artista = models.CharField(max_length=100, default='')

    objects = models.Manager() 

    def __str__(self):
        return str(self.titulo)

# Clase Instrumento
class Instrumento(models.Model):
    id_instrumento = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100, default='')
    tipo_instrumento = models.CharField(max_length=100, default='')
    marca = models.CharField(max_length=100, default='')
    especie = models.CharField(max_length=100, default='')

    objects = models.Manager() 

    def __str__(self):
        return str(self.modelo)

# Clase Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    disco = models.OneToOneField(Disco, null=True, blank=True, on_delete=models.CASCADE)
    instrumento = models.OneToOneField(Instrumento, null=True, blank=True, on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    estado = models.BooleanField(default=False)

    objects = models.Manager() 

    def __str__(self):
        return f"Producto #{str(self.id_producto)}"

# Clase Artista
class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    objects = models.Manager() 

    def __str__(self):
        return str(self.nombre)

# Clase SelloDiscografico
class SelloDiscografico(models.Model):
    id_sello_discografico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    objects = models.Manager() 

    def __str__(self):
        return str(self.nombre)

# Clase GeneroMusical
class GeneroMusical(models.Model):
    id_genero_musical = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    objects = models.Manager() 

    def __str__(self):
        return str(self.nombre)

# Clase TipoDisco
class TipoDisco(models.Model):
    id_tipo_disco = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    objects = models.Manager() 

    def __str__(self):
        return str(self.nombre)

# Clase TipoInstrumento
class TipoInstrumento(models.Model):
    id_tipo_instrumento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)

    objects = models.Manager() 

    def __str__(self):
        return str(self.tipo)

# Clase EspecieInstrumento
class EspecieInstrumento(models.Model):
    id_especie_instrumento = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=100)

    objects = models.Manager() 

    def __str__(self):
        return str(self.especie)

# Clase MarcaInstrumento
class MarcaInstrumento(models.Model):
    id_marca_instrumento = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)

    objects = models.Manager() 

    def __str__(self):
        return str(self.marca)

# Clase Presupuesto
class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    presupuesto = models.IntegerField()

    objects = models.Manager() 

    def __str__(self):
        return f"Presupuesto #{str(self.id_presupuesto)}"

# Clase Boleta
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    productos = models.ManyToManyField(Producto, through='DetalleBoleta')
    fecha_venta = models.DateField(auto_now_add=True)
    total = models.PositiveIntegerField(default=0)

    objects = models.Manager() 

    def __str__(self):
        return f"Boleta #{str(self.id_boleta)}"

# Clase DetalleBoleta
class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    objects = models.Manager() 

    def __str__(self):
        return f"Detalle de Boleta - Producto: {str(self.producto)}, Cantidad: {str(self.cantidad)}"
