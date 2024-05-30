from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Marca)
admin.site.register(GeneroMusical)
admin.site.register(TipoInstrumento)
admin.site.register(Artista)
admin.site.register(Cancion)
admin.site.register(Instrumento)
admin.site.register(DetalleInstrumento)
admin.site.register(Disco)
admin.site.register(DetalleDisco)
# admin.site.register(Usuario)
admin.site.register(Producto)