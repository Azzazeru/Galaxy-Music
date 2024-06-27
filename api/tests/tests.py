import pytest
from django.test import TestCase
from api.models import *

# Para disco

@pytest.mark.django_db
class TestArtistaModel(TestCase):

    def setUp(self):
        # Datos de prueba
        Artista.objects.create(nombre="Artista 1")
        Artista.objects.create(nombre="Artista 2")

    def test_crear_artista(self):
        Artista.objects.create(nombre="Nuevo Artista")
        nuevo_artista = Artista.objects.get(nombre="Nuevo Artista")
        assert nuevo_artista.nombre == "Nuevo Artista"

    def test_obtener_artista(self):
        artista = Artista.objects.get(nombre="Artista 1")
        assert artista.nombre == "Artista 1"

    def test_actualizar_artista(self):
        artista = Artista.objects.get(nombre="Artista 1")
        artista.nombre = "Artista Modificado"
        artista.save()
        artista_actualizado = Artista.objects.get(id_artista=artista.id_artista)
        assert artista_actualizado.nombre == "Artista Modificado"

    def test_eliminar_artista(self):
        artista = Artista.objects.get(nombre="Artista 2")
        artista.delete()
        with pytest.raises(Artista.DoesNotExist):
            Artista.objects.get(nombre="Artista 2")

    def test_str_method(self):
        artista = Artista.objects.get(nombre="Artista 1")
        assert str(artista) == "Artista 1"

@pytest.mark.django_db
class TestSelloDiscograficoModel(TestCase):
    def setUp(self):
        # Datos de prueba
        SelloDiscografico.objects.create(nombre="Sello 1")
        SelloDiscografico.objects.create(nombre="Sello 2")

    def test_crear_sello_discografico(self):
        SelloDiscografico.objects.create(nombre="Nuevo Sello")
        nuevo_sello = SelloDiscografico.objects.get(nombre="Nuevo Sello")
        assert nuevo_sello.nombre == "Nuevo Sello"

    def test_obtener_sello_discografico(self):
        sello = SelloDiscografico.objects.get(nombre="Sello 1")
        assert sello.nombre == "Sello 1"

    def test_actualizar_sello_discografico(self):
        sello = SelloDiscografico.objects.get(nombre="Sello 1")
        sello.nombre = "Sello Modificado"
        sello.save()
        sello_actualizado = SelloDiscografico.objects.get(id_sello_discografico=sello.id_sello_discografico)
        assert sello_actualizado.nombre == "Sello Modificado"

    def test_eliminar_sello_discografico(self):
        sello = SelloDiscografico.objects.get(nombre="Sello 2")
        sello.delete()
        with pytest.raises(SelloDiscografico.DoesNotExist):
            SelloDiscografico.objects.get(nombre="Sello 2")

    def test_str_method(self):
        sello = SelloDiscografico.objects.get(nombre="Sello 1")
        assert str(sello) == "Sello 1"

@pytest.mark.django_db
class TestTipoDiscoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        TipoDisco.objects.create(nombre="CD")
        TipoDisco.objects.create(nombre="Vinilo")

    def test_crear_tipo_disco(self):
        TipoDisco.objects.create(nombre="Digital")
        nuevo_tipo = TipoDisco.objects.get(nombre="Digital")
        assert nuevo_tipo.nombre == "Digital"

    def test_obtener_tipo_disco(self):
        tipo = TipoDisco.objects.get(nombre="CD")
        assert tipo.nombre == "CD"

    def test_actualizar_tipo_disco(self):
        tipo = TipoDisco.objects.get(nombre="CD")
        tipo.nombre = "CD Modificado"
        tipo.save()
        tipo_actualizado = TipoDisco.objects.get(id_tipo_disco=tipo.id_tipo_disco)
        assert tipo_actualizado.nombre == "CD Modificado"

    def test_eliminar_tipo_disco(self):
        tipo = TipoDisco.objects.get(nombre="Vinilo")
        tipo.delete()
        with pytest.raises(TipoDisco.DoesNotExist):
            TipoDisco.objects.get(nombre="Vinilo")

    def test_str_method(self):
        tipo = TipoDisco.objects.get(nombre="CD")
        assert str(tipo) == "CD"

@pytest.mark.django_db
class TestGeneroMusicalModel(TestCase):

    def setUp(self):
        # Datos de prueba
        GeneroMusical.objects.create(nombre="Rock")
        GeneroMusical.objects.create(nombre="Pop")

    def test_crear_genero_musical(self):
        GeneroMusical.objects.create(nombre="Electrónica")
        nuevo_genero = GeneroMusical.objects.get(nombre="Electrónica")
        assert nuevo_genero.nombre == "Electrónica"

    def test_obtener_genero_musical(self):
        genero = GeneroMusical.objects.get(nombre="Rock")
        assert genero.nombre == "Rock"

    def test_actualizar_genero_musical(self):
        genero = GeneroMusical.objects.get(nombre="Rock")
        genero.nombre = "Rock Alternativo"
        genero.save()
        genero_actualizado = GeneroMusical.objects.get(id_genero_musical=genero.id_genero_musical)
        assert genero_actualizado.nombre == "Rock Alternativo"

    def test_eliminar_genero_musical(self):
        genero = GeneroMusical.objects.get(nombre="Pop")
        genero.delete()
        with pytest.raises(GeneroMusical.DoesNotExist):
            GeneroMusical.objects.get(nombre="Pop")

    def test_str_method(self):
        genero = GeneroMusical.objects.get(nombre="Rock")
        assert str(genero) == "Rock"

# Para Instrumento

@pytest.mark.django_db
class TestTipoInstrumentoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        TipoInstrumento.objects.create(tipo="Guitarra")
        TipoInstrumento.objects.create(tipo="Piano")

    def test_crear_tipo_instrumento(self):
        TipoInstrumento.objects.create(tipo="Violín")
        nuevo_tipo = TipoInstrumento.objects.get(tipo="Violín")
        assert nuevo_tipo.tipo == "Violín"

    def test_obtener_tipo_instrumento(self):
        tipo = TipoInstrumento.objects.get(tipo="Guitarra")
        assert tipo.tipo == "Guitarra"

    def test_actualizar_tipo_instrumento(self):
        tipo = TipoInstrumento.objects.get(tipo="Guitarra")
        tipo.tipo = "Guitarra Eléctrica"
        tipo.save()
        tipo_actualizado = TipoInstrumento.objects.get(id_tipo_instrumento=tipo.id_tipo_instrumento)
        assert tipo_actualizado.tipo == "Guitarra Eléctrica"

    def test_eliminar_tipo_instrumento(self):
        tipo = TipoInstrumento.objects.get(tipo="Piano")
        tipo.delete()
        with pytest.raises(TipoInstrumento.DoesNotExist):
            TipoInstrumento.objects.get(tipo="Piano")

    def test_str_method(self):
        tipo = TipoInstrumento.objects.get(tipo="Guitarra")
        assert str(tipo) == "Guitarra"

@pytest.mark.django_db
class TestEspecieInstrumentoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        EspecieInstrumento.objects.create(especie="Acústica")
        EspecieInstrumento.objects.create(especie="Eléctrica")

    def test_crear_especie_instrumento(self):
        EspecieInstrumento.objects.create(especie="Clásica")
        nueva_especie = EspecieInstrumento.objects.get(especie="Clásica")
        assert nueva_especie.especie == "Clásica"

    def test_obtener_especie_instrumento(self):
        especie = EspecieInstrumento.objects.get(especie="Acústica")
        assert especie.especie == "Acústica"

    def test_actualizar_especie_instrumento(self):
        especie = EspecieInstrumento.objects.get(especie="Acústica")
        especie.especie = "Acústica Modificada"
        especie.save()
        especie_actualizada = EspecieInstrumento.objects.get(id_especie_instrumento=especie.id_especie_instrumento)
        assert especie_actualizada.especie == "Acústica Modificada"

    def test_eliminar_especie_instrumento(self):
        especie = EspecieInstrumento.objects.get(especie="Eléctrica")
        especie.delete()
        with pytest.raises(EspecieInstrumento.DoesNotExist):
            EspecieInstrumento.objects.get(especie="Eléctrica")

    def test_str_method(self):
        especie = EspecieInstrumento.objects.get(especie="Acústica")
        assert str(especie) == "Acústica"

@pytest.mark.django_db
class TestMarcaInstrumentoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        MarcaInstrumento.objects.create(marca="Fender")
        MarcaInstrumento.objects.create(marca="Gibson")

    def test_crear_marca_instrumento(self):
        MarcaInstrumento.objects.create(marca="Yamaha")
        nueva_marca = MarcaInstrumento.objects.get(marca="Yamaha")
        assert nueva_marca.marca == "Yamaha"

    def test_obtener_marca_instrumento(self):
        marca = MarcaInstrumento.objects.get(marca="Fender")
        assert marca.marca == "Fender"

    def test_actualizar_marca_instrumento(self):
        marca = MarcaInstrumento.objects.get(marca="Fender")
        marca.marca = "Fender Modificada"
        marca.save()
        marca_actualizada = MarcaInstrumento.objects.get(id_marca_instrumento=marca.id_marca_instrumento)
        assert marca_actualizada.marca == "Fender Modificada"

    def test_eliminar_marca_instrumento(self):
        marca = MarcaInstrumento.objects.get(marca="Gibson")
        marca.delete()
        with pytest.raises(MarcaInstrumento.DoesNotExist):
            MarcaInstrumento.objects.get(marca="Gibson")

    def test_str_method(self):
        marca = MarcaInstrumento.objects.get(marca="Fender")
        assert str(marca) == "Fender"

# Disco

@pytest.mark.django_db
class TestDiscoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        Disco.objects.create(titulo="Disco 1", tipo_disco="CD", sello_discografico="Sello A", genero_musical="Rock", artista="Artista 1")
        Disco.objects.create(titulo="Disco 2", tipo_disco="Vinilo", sello_discografico="Sello B", genero_musical="Pop", artista="Artista 2")

    def test_crear_disco(self):
        Disco.objects.create(titulo="Nuevo Disco", tipo_disco="Digital", sello_discografico="Sello C", genero_musical="Electrónica", artista="Artista 3")
        nuevo_disco = Disco.objects.get(titulo="Nuevo Disco")
        assert nuevo_disco.tipo_disco == "Digital"

    def test_obtener_disco(self):
        disco = Disco.objects.get(titulo="Disco 1")
        assert disco.artista == "Artista 1"

    def test_actualizar_disco(self):
        disco = Disco.objects.get(titulo="Disco 1")
        disco.artista = "Artista Actualizado"
        disco.save()
        disco_actualizado = Disco.objects.get(id_disco=disco.id_disco)
        assert disco_actualizado.artista == "Artista Actualizado"

    def test_eliminar_disco(self):
        disco = Disco.objects.get(titulo="Disco 2")
        disco.delete()
        with pytest.raises(Disco.DoesNotExist):
            Disco.objects.get(titulo="Disco 2")

    def test_str_method(self):
        disco = Disco.objects.get(titulo="Disco 1")
        assert str(disco) == "Disco 1"

# Instrumento

@pytest.mark.django_db
class TestInstrumentoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        Instrumento.objects.create(modelo="Instrumento 1", tipo_instrumento="Guitarra", marca="Fender", especie="Eléctrica")
        Instrumento.objects.create(modelo="Instrumento 2", tipo_instrumento="Piano", marca="Yamaha", especie="Acústica")

    def test_crear_instrumento(self):
        Instrumento.objects.create(modelo="Nuevo Instrumento", tipo_instrumento="Violín", marca="Stradivarius", especie="Clásica")
        nuevo_instrumento = Instrumento.objects.get(modelo="Nuevo Instrumento")
        assert nuevo_instrumento.tipo_instrumento == "Violín"

    def test_obtener_instrumento(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 1")
        assert instrumento.marca == "Fender"

    def test_actualizar_instrumento(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 1")
        instrumento.marca = "Fender Modificado"
        instrumento.save()
        instrumento_actualizado = Instrumento.objects.get(id_instrumento=instrumento.id_instrumento)
        assert instrumento_actualizado.marca == "Fender Modificado"

    def test_eliminar_instrumento(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 2")
        instrumento.delete()
        with pytest.raises(Instrumento.DoesNotExist):
            Instrumento.objects.get(modelo="Instrumento 2")

    def test_str_method(self):
        instrumento = Instrumento.objects.get(modelo="Instrumento 1")
        assert str(instrumento) == "Instrumento 1"

# Producto

@pytest.mark.django_db
class TestProductoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        disco_1 = Disco.objects.create(titulo="Disco 1", tipo_disco="CD", sello_discografico="Sello A", genero_musical="Rock", artista="Artista 1")
        instrumento_1 = Instrumento.objects.create(modelo="Instrumento 1", tipo_instrumento="Guitarra", marca="Fender", especie="Eléctrica")
        Producto.objects.create(disco=disco_1, precio=100, stock=10, estado=True)
        Producto.objects.create(instrumento=instrumento_1, precio=500, stock=5, estado=False)

    def test_crear_producto_disco(self):
        nuevo_disco = Disco.objects.create(titulo="Nuevo Disco", tipo_disco="Digital", sello_discografico="Sello C", genero_musical="Electrónica", artista="Artista 3")
        Producto.objects.create(disco=nuevo_disco, precio=200, stock=20, estado=True)
        producto_creado = Producto.objects.get(disco=nuevo_disco)
        assert producto_creado.precio == 200

    def test_crear_producto_instrumento(self):
        nuevo_instrumento = Instrumento.objects.create(modelo="Nuevo Instrumento", tipo_instrumento="Violín", marca="Stradivarius", especie="Clásica")
        Producto.objects.create(instrumento=nuevo_instrumento, precio=1000, stock=3, estado=False)
        producto_creado = Producto.objects.get(instrumento=nuevo_instrumento)
        assert producto_creado.precio == 1000

    def test_obtener_producto(self):
        producto = Producto.objects.get(precio=100)
        assert producto.stock == 10

    def test_actualizar_producto(self):
        producto = Producto.objects.get(precio=500)
        producto.stock = 6
        producto.save()
        producto_actualizado = Producto.objects.get(id_producto=producto.id_producto)
        assert producto_actualizado.stock == 6

    def test_eliminar_producto(self):
        producto = Producto.objects.get(precio=500)
        producto.delete()
        with pytest.raises(Producto.DoesNotExist):
            Producto.objects.get(precio=500)

    def test_str_method(self):
        producto = Producto.objects.get(precio=100)
        assert str(producto) == f"Producto #{producto.id_producto}"

# Presupuesto

@pytest.mark.django_db
class TestPresupuestoModel(TestCase):

    def setUp(self):
        # Datos de prueba
        Presupuesto.objects.create(presupuesto=500)

    def test_crear_presupuesto(self):
        Presupuesto.objects.create(presupuesto=1000)
        nuevo_presupuesto = Presupuesto.objects.get(presupuesto=1000)
        assert nuevo_presupuesto.presupuesto == 1000

    def test_obtener_presupuesto(self):
        presupuesto = Presupuesto.objects.get(presupuesto=500)
        assert presupuesto.presupuesto == 500

    def test_actualizar_presupuesto(self):
        presupuesto = Presupuesto.objects.get(presupuesto=500)
        presupuesto.presupuesto = 700
        presupuesto.save()
        presupuesto_actualizado = Presupuesto.objects.get(id_presupuesto=presupuesto.id_presupuesto)
        assert presupuesto_actualizado.presupuesto == 700

    def test_eliminar_presupuesto(self):
        presupuesto = Presupuesto.objects.get(presupuesto=500)
        presupuesto.delete()
        with pytest.raises(Presupuesto.DoesNotExist):
            Presupuesto.objects.get(presupuesto=500)

    def test_str_method(self):
        presupuesto = Presupuesto.objects.get(presupuesto=500)
        assert str(presupuesto) == f"Presupuesto #{presupuesto.id_presupuesto}"

# Boleta

@pytest.mark.django_db
class TestBoletaModel(TestCase):

    def setUp(self):
        # Datos de prueba
        producto_1 = Producto.objects.create(precio=100, stock=10)
        producto_2 = Producto.objects.create(precio=200, stock=5)
        boleta = Boleta.objects.create(total=300)
        boleta.productos.add(producto_1, through_defaults={'cantidad': 2})
        boleta.productos.add(producto_2, through_defaults={'cantidad': 1})

    def test_crear_boleta(self):
        boleta = Boleta.objects.create(total=500)
        producto = Producto.objects.create(precio=300, stock=8)
        boleta.productos.add(producto, through_defaults={'cantidad': 3})
        boleta_guardada = Boleta.objects.get(id_boleta=boleta.id_boleta)
        assert boleta_guardada.total == 500

    def test_obtener_boleta(self):
        boleta = Boleta.objects.get(total=300)
        assert boleta.productos.count() == 2

    def test_actualizar_boleta(self):
        boleta = Boleta.objects.get(total=300)
        boleta.total = 400
        boleta.save()
        boleta_actualizada = Boleta.objects.get(id_boleta=boleta.id_boleta)
        assert boleta_actualizada.total == 400

    def test_eliminar_boleta(self):
        boleta = Boleta.objects.get(total=300)
        boleta.delete()
        with pytest.raises(Boleta.DoesNotExist):
            Boleta.objects.get(total=300)

    def test_str_method(self):
        boleta = Boleta.objects.get(total=300)
        assert str(boleta) == f"Boleta #{boleta.id_boleta}"

# Detalle Boleta

@pytest.mark.django_db
class TestDetalleBoletaModel(TestCase):

    def setUp(self):
        # Datos de prueba
        producto_1 = Producto.objects.create(precio=100, stock=10)
        producto_2 = Producto.objects.create(precio=200, stock=5)
        boleta = Boleta.objects.create(total=300)
        DetalleBoleta.objects.create(boleta=boleta, producto=producto_1, cantidad=2)
        DetalleBoleta.objects.create(boleta=boleta, producto=producto_2, cantidad=1)

    def test_crear_detalle_boleta(self):
        boleta = Boleta.objects.create(total=500)
        producto = Producto.objects.create(precio=300, stock=8)
        detalle_boleta = DetalleBoleta.objects.create(boleta=boleta, producto=producto, cantidad=3)
        assert detalle_boleta.cantidad == 3

    def test_obtener_detalle_boleta(self):
        detalle_boleta = DetalleBoleta.objects.get(cantidad=2)
        assert detalle_boleta.producto.stock == 10

    def test_actualizar_detalle_boleta(self):
        detalle_boleta = DetalleBoleta.objects.get(cantidad=1)
        detalle_boleta.cantidad = 2
        detalle_boleta.save()
        detalle_boleta_actualizado = DetalleBoleta.objects.get(id=detalle_boleta.id)
        assert detalle_boleta_actualizado.cantidad == 2

    def test_eliminar_detalle_boleta(self):
        detalle_boleta = DetalleBoleta.objects.get(cantidad=1)
        detalle_boleta.delete()
        with pytest.raises(DetalleBoleta.DoesNotExist):
            DetalleBoleta.objects.get(cantidad=1)