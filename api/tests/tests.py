import requests
import pytest
from django.test import TestCase
from api.models import Producto, Disco, Instrumento

ENDPOINT = "https://gmad.up.railway.app"
# ENDPOINT = "http://127.0.0.1:8000/api"

def test_endpoint():
    response = requests.get(f"{ENDPOINT}/api/public/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_productos_aprobados():    
    response = requests.get(f"{ENDPOINT}/api/public/productos/?estado=true")
    
    assert response.status_code == 200


# Importa el decorador pytest.mark.django_db y la clase TestCase de Django
@pytest.mark.django_db
class TestDiscoModel(TestCase):

    # Método setUp: Se ejecuta antes de cada prueba
    def setUp(self):
        # Crea datos de prueba para el modelo Disco
        Disco.objects.create(titulo="Disco 1", tipo_disco="CD", sello_discografico="Sello A", 
                            genero_musical="Rock", artista="Artista 1")
        Disco.objects.create(titulo="Disco 2", tipo_disco="Vinilo", sello_discografico="Sello B", 
                            genero_musical="Pop", artista="Artista 2")

    # Método de prueba: Crea un nuevo disco y verifica sus atributos
    def test_crear_disco(self):
        Disco.objects.create(titulo="Nuevo Disco", tipo_disco="Digital", 
                sello_discografico="Sello C", genero_musical="Electrónica", artista="Artista 3")
        nuevo_disco = Disco.objects.get(titulo="Nuevo Disco")
        
        # Verifica que el tipo de disco del nuevo disco sea "Digital"
        assert nuevo_disco.tipo_disco == "Digital"

    # Método de prueba: Obtiene un disco existente y verifica uno de sus atributos
    def test_obtener_disco(self):
        disco = Disco.objects.get(titulo="Disco 1")
        
        # Verifica que el artista del disco obtenido sea "Artista 1"
        assert disco.artista == "Artista 1"

    # Método de prueba: Actualiza un disco existente y verifica el cambio
    def test_actualizar_disco(self):
        disco = Disco.objects.get(titulo="Disco 1")
        disco.artista = "Artista Actualizado"
        disco.save()
        disco_actualizado = Disco.objects.get(id_disco=disco.id_disco)
        
        # Verifica que el artista del disco actualizado sea "Artista Actualizado"
        assert disco_actualizado.artista == "Artista Actualizado"

    # Método de prueba: Elimina un disco y verifica que no se pueda encontrar más tarde
    def test_eliminar_disco(self):
        disco = Disco.objects.get(titulo="Disco 2")
        disco.delete()
        
        # Verifica que al intentar obtener el disco eliminado lance una excepción Disco.DoesNotExist
        with pytest.raises(Disco.DoesNotExist):
            Disco.objects.get(titulo="Disco 2")

    # Método de prueba: Verifica que el método __str__ de Disco funcione correctamente
    def test_str_method(self):
        disco = Disco.objects.get(titulo="Disco 1")
        
        # Verifica que la representación en cadena del disco coincida con su título
        assert str(disco) == "Disco 1"


# Importa el decorador pytest.mark.django_db y la clase TestCase de Django
@pytest.mark.django_db
class TestInstrumentoModel(TestCase):

    # Método setUp: Se ejecuta antes de cada prueba
    def setUp(self):
        # Crea datos de prueba para el modelo Instrumento
        Instrumento.objects.create(modelo="Instrumento 1", tipo_instrumento="Guitarra", 
                                marca="Fender", especie="Eléctrica")
        Instrumento.objects.create(modelo="Instrumento 2", tipo_instrumento="Piano", 
                                marca="Yamaha", especie="Acústica")

    # Método de prueba: Crea un nuevo instrumento y verifica sus atributos
    def test_crear_instrumento(self):
        Instrumento.objects.create(modelo="Nuevo Instrumento", tipo_instrumento="Violín", marca="Stradivarius", especie="Clásica")
        nuevo_instrumento = Instrumento.objects.get(modelo="Nuevo Instrumento")
        
        # Verifica que el tipo de instrumento del nuevo instrumento sea "Violín"
        assert nuevo_instrumento.tipo_instrumento == "Violín"

    # Método de prueba: Obtiene un instrumento existente y verifica uno de sus atributos
    def test_obtener_instrumento(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 1")
        
        # Verifica que la marca del instrumento obtenido sea "Fender"
        assert instrumento.marca == "Fender"

    # Método de prueba: Actualiza un instrumento existente y verifica el cambio
    def test_actualizar_instrumento(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 1")
        instrumento.marca = "Fender Modificado"
        instrumento.save()
        instrumento_actualizado = Instrumento.objects.get(id_instrumento=instrumento.id_instrumento)
        
        # Verifica que la marca del instrumento actualizado sea "Fender Modificado"
        assert instrumento_actualizado.marca == "Fender Modificado"

    # Método de prueba: Elimina un instrumento y verifica que no se pueda encontrar más tarde
    def test_eliminar_instrumento(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 2")
        instrumento.delete()
        
        # Verifica que al intentar obtener el instrumento eliminado lance una excepción Instrumento.DoesNotExist
        with pytest.raises(Instrumento.DoesNotExist):
            Instrumento.objects.get(modelo="Instrumento 2")

    # Método de prueba: Verifica que el método __str__ de Instrumento funcione correctamente
    def test_str_method(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 1")
        
        # Verifica que la representación en cadena del instrumento coincida con su modelo
        assert str(instrumento) == "Instrumento 1"


# Importa el decorador pytest.mark.django_db y la clase TestCase de Django
@pytest.mark.django_db
class TestProductoModel(TestCase):

    # Método setUp: Se ejecuta antes de cada prueba
    def setUp(self):
        # Datos de prueba para Disco y Instrumento
        disco_1 = Disco.objects.create(titulo="Disco 1", tipo_disco="CD", 
                        sello_discografico="Sello A", genero_musical="Rock", artista="Artista 1")
        instrumento_1 = Instrumento.objects.create(modelo="Instrumento 1", 
                                tipo_instrumento="Guitarra", marca="Fender", especie="Eléctrica")
        
        # Creación de productos relacionados con Disco e Instrumento
        Producto.objects.create(disco=disco_1, precio=100, stock=10, estado=True)
        Producto.objects.create(instrumento=instrumento_1, precio=500, stock=5, estado=False)

    # Método de prueba: Crea un producto relacionado con Disco
    def test_crear_producto_disco(self):
        nuevo_disco = Disco.objects.create(titulo="Nuevo Disco", tipo_disco="Digital", 
                sello_discografico="Sello C", genero_musical="Electrónica", artista="Artista 3")
        Producto.objects.create(disco=nuevo_disco, precio=200, stock=20, estado=True)
        producto_creado = Producto.objects.get(disco=nuevo_disco)
        
        # Verifica que el precio del producto creado coincida con 200
        assert producto_creado.precio == 200

    # Método de prueba: Crea un producto relacionado con Instrumento
    def test_crear_producto_instrumento(self):
        nuevo_instrumento = Instrumento.objects.create(modelo="Nuevo Instrumento", 
                                tipo_instrumento="Violín", marca="Stradivarius", especie="Clásica")
        Producto.objects.create(instrumento=nuevo_instrumento, precio=1000, stock=3, estado=False)
        producto_creado = Producto.objects.get(instrumento=nuevo_instrumento)
        
        # Verifica que el precio del producto creado coincida con 1000
        assert producto_creado.precio == 1000

    # Método de prueba: Obtiene un producto por su precio y verifica el stock
    def test_obtener_producto(self):
        producto = Producto.objects.get(precio=100)
        
        # Verifica que el stock del producto obtenido sea 10
        assert producto.stock == 10

    # Método de prueba: Actualiza el stock de un producto y verifica el cambio
    def test_actualizar_producto(self):
        producto = Producto.objects.get(precio=500)
        producto.stock = 6
        producto.save()
        producto_actualizado = Producto.objects.get(id_producto=producto.id_producto)
        
        # Verifica que el stock del producto actualizado sea 6
        assert producto_actualizado.stock == 6

    # Método de prueba: Elimina un producto y verifica que no se pueda encontrar
    def test_eliminar_producto(self):
        producto = Producto.objects.get(precio=500)
        producto.delete()
        
        # Verifica que al intentar obtener el producto eliminado lance una excepción
        with pytest.raises(Producto.DoesNotExist):
            Producto.objects.get(precio=500)

    # Método de prueba: Verifica que el método __str__ de Producto funcione correctamente
    def test_str_method(self):
        producto = Producto.objects.get(precio=100)
        
        # Verifica que la representación en cadena del producto coincida con el formato esperado
        assert str(producto) == f"Producto #{producto.id_producto}"







