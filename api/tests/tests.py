import pytest
from api.models import *

# @pytest.mark.django_db
# def test_sello_creation():
#     sello = SelloDiscografico.objects.create(
#         nombre="Sello 1"
#     )
#     assert sello.nombre == "Sello 1"

@pytest.fixture
def sello_creation():
    return SelloDiscografico.objects.create(
        id_sello_discografico=1,
        nombre="Sello 1"
    )
@pytest.mark.django_db
def test_common_sello_creation(sello_creation):
    sello_creation.save()
    assert sello_creation.nombre == "Sello 1"

@pytest.mark.django_db
def test_sello_creation_fail():
    with pytest.raises(Exception):
        SelloDiscografico.objects.create_sello(
            nombre="Sello 1"
        )

@pytest.mark.django_db
def test_update_sello(sello_creation):
    sello = sello_creation
    sello.nombre = "Nuevo nombre"
    sello.save()
    assert SelloDiscografico.objects.get(id_sello_discografico=sello.id_sello_discografico).nombre == "Nuevo nombre"

@pytest.mark.django_db
def test_delete_sello(sello_creation):
    sello_creation.delete()
    with pytest.raises(SelloDiscografico.DoesNotExist):
        SelloDiscografico.objects.get(id_sello_discografico=sello_creation.id_sello_discografico)

@pytest.mark.django_db
def test_query_sello(sello_creation):
    assert SelloDiscografico.objects.filter(nombre="Sello 1").exists()

# Creación de un artista
@pytest.fixture
def artista_creation():
    return Artista.objects.create(
        nombre="Artista 1"
    )

# Prueba de creación de un artista
@pytest.mark.django_db
def test_artista_creation(artista_creation):
    assert artista_creation.nombre == "Artista 1"

# Prueba de actualización de un artista
@pytest.mark.django_db
def test_update_artista(artista_creation):
    artista = artista_creation
    artista.nombre = "Nuevo nombre"
    artista.save()
    assert Artista.objects.get(id_artista=artista.id_artista).nombre == "Nuevo nombre"

# Prueba de eliminación de un artista
@pytest.mark.django_db
def test_delete_artista(artista_creation):
    artista_creation.delete()
    with pytest.raises(Artista.DoesNotExist):
        Artista.objects.get(id_artista=artista_creation.id_artista)

# Prueba de consulta de un artista
@pytest.mark.django_db
def test_query_artista(artista_creation):
    assert Artista.objects.filter(nombre="Artista 1").exists()

##

# Creación de un sello discográfico
@pytest.fixture
def sello_discografico_creation():
    return SelloDiscografico.objects.create(
        nombre="Sello Discográfico 1"
    )

# Prueba de creación de un sello discográfico
@pytest.mark.django_db
def test_sello_discografico_creation(sello_discografico_creation):
    assert sello_discografico_creation.nombre == "Sello Discográfico 1"

# Prueba de actualización de un sello discográfico
@pytest.mark.django_db
def test_update_sello_discografico(sello_discografico_creation):
    sello = sello_discografico_creation
    sello.nombre = "Nuevo nombre"
    sello.save()
    assert SelloDiscografico.objects.get(id_sello_discografico=sello.id_sello_discografico).nombre == "Nuevo nombre"

# Prueba de eliminación de un sello discográfico
@pytest.mark.django_db
def test_delete_sello_discografico(sello_discografico_creation):
    sello_discografico_creation.delete()
    with pytest.raises(SelloDiscografico.DoesNotExist):
        SelloDiscografico.objects.get(id_sello_discografico=sello_discografico_creation.id_sello_discografico)

# Prueba de consulta de un sello discográfico
@pytest.mark.django_db
def test_query_sello_discografico(sello_discografico_creation):
    assert SelloDiscografico.objects.filter(nombre="Sello Discográfico 1").exists()

##

# Creación de un género musical
@pytest.fixture
def genero_musical_creation():
    return GeneroMusical.objects.create(
        nombre="Género Musical 1"
    )

# Prueba de creación de un género musical
@pytest.mark.django_db
def test_genero_musical_creation(genero_musical_creation):
    assert genero_musical_creation.nombre == "Género Musical 1"

# Prueba de actualización de un género musical
@pytest.mark.django_db
def test_update_genero_musical(genero_musical_creation):
    genero = genero_musical_creation
    genero.nombre = "Nuevo nombre"
    genero.save()
    assert GeneroMusical.objects.get(id_genero_musical=genero.id_genero_musical).nombre == "Nuevo nombre"

# Prueba de eliminación de un género musical
@pytest.mark.django_db
def test_delete_genero_musical(genero_musical_creation):
    genero_musical_creation.delete()
    with pytest.raises(GeneroMusical.DoesNotExist):
        GeneroMusical.objects.get(id_genero_musical=genero_musical_creation.id_genero_musical)

# Prueba de consulta de un género musical
@pytest.mark.django_db
def test_query_genero_musical(genero_musical_creation):
    assert GeneroMusical.objects.filter(nombre="Género Musical 1").exists()

##

# Creación de un detalle de disco
@pytest.fixture
def detalle_disco_creation(sello_creation, genero_musical_creation, artista_creation):
    return DetalleDisco.objects.create(
        sello_discografico_id=sello_creation.id_sello_discografico,
        genero_musical_id=genero_musical_creation.id_genero_musical,
        artista_id=artista_creation.id_artista
    )

# Creación de un detalle de disco
@pytest.mark.django_db
def test_detalle_disco_creation(detalle_disco_creation):
    assert detalle_disco_creation.sello_discografico.id_sello_discografico == 1
    assert detalle_disco_creation.genero_musical.id_genero_musical == 1
    assert detalle_disco_creation.artista.id_artista == 1

# Prueba de actualización de un detalle de disco
@pytest.mark.django_db
def test_update_detalle_disco(detalle_disco_creation, artista_creation):
    detalle_disco = detalle_disco_creation
    detalle_disco.artista_id = artista_creation.id_artista
    detalle_disco.save()
    assert DetalleDisco.objects.get(id_detalle_disco=detalle_disco.id_detalle_disco).artista_id == artista_creation.id_artista

# Prueba de eliminación de un detalle de disco
@pytest.mark.django_db
def test_delete_detalle_disco(detalle_disco_creation):
    detalle_disco_creation.delete()
    with pytest.raises(DetalleDisco.DoesNotExist):
        DetalleDisco.objects.get(id_detalle_disco=detalle_disco_creation.id_detalle_disco)

# Prueba de consulta de un detalle de disco
@pytest.mark.django_db
def test_query_detalle_disco(detalle_disco_creation):
    assert DetalleDisco.objects.filter(sello_discografico_id=1).exists()

##

@pytest.fixture
def tipo_instrumento_creation():
    return TipoInstrumento.objects.create(tipo="Tipo 1")

# Creación de TipoInstrumento
@pytest.mark.django_db
def test_tipo_instrumento_creation():
    tipo_instrumento = TipoInstrumento.objects.create(tipo="Tipo 1")
    assert tipo_instrumento.tipo == "Tipo 1"

# Lectura de TipoInstrumento
@pytest.mark.django_db
def test_tipo_instrumento_read(tipo_instrumento_creation):
    tipo_instrumento = tipo_instrumento_creation
    tipo_instrumento_leido = TipoInstrumento.objects.get(id_tipo_instrumento=tipo_instrumento.id_tipo_instrumento)
    assert tipo_instrumento_leido.tipo == "Tipo 1"

# Actualización de TipoInstrumento
@pytest.mark.django_db
def test_tipo_instrumento_update(tipo_instrumento_creation):
    tipo_instrumento = tipo_instrumento_creation
    tipo_instrumento.tipo = "Nuevo Tipo"
    tipo_instrumento.save()
    tipo_instrumento_actualizado = TipoInstrumento.objects.get(id_tipo_instrumento=tipo_instrumento.id_tipo_instrumento)
    assert tipo_instrumento_actualizado.tipo == "Nuevo Tipo"

# Eliminación de TipoInstrumento
@pytest.mark.django_db
def test_tipo_instrumento_delete(tipo_instrumento_creation):
    tipo_instrumento = tipo_instrumento_creation
    tipo_instrumento.delete()
    with pytest.raises(TipoInstrumento.DoesNotExist):
        TipoInstrumento.objects.get(id_tipo_instrumento=tipo_instrumento.id_tipo_instrumento)

##


# Fixture para la creación de Marca
@pytest.fixture
def marca_creation():
    return Marca.objects.create(nombre="Marca 1")

# Test para la creación de Marca
@pytest.mark.django_db
def test_marca_creation(marca_creation):
    assert marca_creation.nombre == "Marca 1"

# Test para la lectura de Marca
@pytest.mark.django_db
def test_marca_read(marca_creation):
    marca = marca_creation
    marca_leida = Marca.objects.get(id_marca=marca.id_marca)
    assert marca_leida.nombre == "Marca 1"

# Test para la actualización de Marca
@pytest.mark.django_db
def test_marca_update(marca_creation):
    marca = marca_creation
    marca.nombre = "Nueva Marca"
    marca.save()
    marca_actualizada = Marca.objects.get(id_marca=marca.id_marca)
    assert marca_actualizada.nombre == "Nueva Marca"

# Test para la eliminación de Marca
@pytest.mark.django_db
def test_marca_delete(marca_creation):
    marca = marca_creation
    marca.delete()
    with pytest.raises(Marca.DoesNotExist):
        Marca.objects.get(id_marca=marca.id_marca)

##

# Fixture para la creación de DetalleInstrumento
@pytest.fixture
def detalle_instrumento_creation(tipo_instrumento_creation, marca_creation):
    return DetalleInstrumento.objects.create(
        descripcion="Descripción 1",
        tipo_instrumento=tipo_instrumento_creation,
        marca=marca_creation
    )

# Test para la creación de DetalleInstrumento
@pytest.mark.django_db
def test_detalle_instrumento_creation(detalle_instrumento_creation):
    assert detalle_instrumento_creation.descripcion == "Descripción 1"

# Test para la lectura de DetalleInstrumento
@pytest.mark.django_db
def test_detalle_instrumento_read(detalle_instrumento_creation):
    detalle_instrumento = detalle_instrumento_creation
    detalle_leido = DetalleInstrumento.objects.get(id_detalle_instrumento=detalle_instrumento.id_detalle_instrumento)
    assert detalle_leido.descripcion == "Descripción 1"

# Test para la actualización de DetalleInstrumento
@pytest.mark.django_db
def test_detalle_instrumento_update(detalle_instrumento_creation):
    detalle_instrumento = detalle_instrumento_creation
    detalle_instrumento.descripcion = "Nueva Descripción"
    detalle_instrumento.save()
    detalle_actualizado = DetalleInstrumento.objects.get(id_detalle_instrumento=detalle_instrumento.id_detalle_instrumento)
    assert detalle_actualizado.descripcion == "Nueva Descripción"

# Test para la eliminación de DetalleInstrumento
@pytest.mark.django_db
def test_detalle_instrumento_delete(detalle_instrumento_creation):
    detalle_instrumento = detalle_instrumento_creation
    detalle_instrumento.delete()
    with pytest.raises(DetalleInstrumento.DoesNotExist):
        DetalleInstrumento.objects.get(id_detalle_instrumento=detalle_instrumento.id_detalle_instrumento)

##

# Fixture para la creación de Instrumento
@pytest.fixture
def instrumento_creation(detalle_instrumento_creation):
    return Instrumento.objects.create(
        modelo="Modelo 1",
        detalle_instrumento=detalle_instrumento_creation
    )

# Test para la creación de Instrumento
@pytest.mark.django_db
def test_instrumento_creation(instrumento_creation):
    assert instrumento_creation.modelo == "Modelo 1"

# Test para la lectura de Instrumento
@pytest.mark.django_db
def test_instrumento_read(instrumento_creation):
    instrumento = instrumento_creation
    instrumento_leido = Instrumento.objects.get(id_instrumento=instrumento.id_instrumento)
    assert instrumento_leido.modelo == "Modelo 1"

# Test para la actualización de Instrumento
@pytest.mark.django_db
def test_instrumento_update(instrumento_creation):
    instrumento = instrumento_creation
    instrumento.modelo = "Nuevo Modelo"
    instrumento.save()
    instrumento_actualizado = Instrumento.objects.get(id_instrumento=instrumento.id_instrumento)
    assert instrumento_actualizado.modelo == "Nuevo Modelo"

# Test para la eliminación de Instrumento
@pytest.mark.django_db
def test_instrumento_delete(instrumento_creation):
    instrumento = instrumento_creation
    instrumento.delete()
    with pytest.raises(Instrumento.DoesNotExist):
        Instrumento.objects.get(id_instrumento=instrumento.id_instrumento)

##

# Fixture para la creación de Producto
@pytest.fixture
def producto_creation():
    disco = Disco.objects.create(titulo="Mi Disco")
    instrumento = Instrumento.objects.create(modelo="Mi Instrumento")
    return Producto.objects.create(
        disco=disco,
        instrumento=instrumento,
        precio=100.00,
        stock=10,
        aprobado=True
    )

# Test para la creación de Producto
@pytest.mark.django_db
def test_producto_creation(producto_creation):
    producto = producto_creation
    assert Producto.objects.filter(id_producto=producto.id_producto).exists()

# Test para la lectura de Producto
@pytest.mark.django_db
def test_producto_read(producto_creation):
    producto = producto_creation
    producto_leido = Producto.objects.get(id_producto=producto.id_producto)
    assert producto_leido.precio == 100.00
    assert producto_leido.stock == 10
    assert producto_leido.aprobado == True

# Test para la actualización de Producto
@pytest.mark.django_db
def test_producto_update(producto_creation):
    producto = producto_creation
    producto.precio = 150.00
    producto.save()
    producto_actualizado = Producto.objects.get(id_producto=producto.id_producto)
    assert producto_actualizado.precio == 150.00

# Test para la eliminación de Producto
@pytest.mark.django_db
def test_producto_delete(producto_creation):
    producto = producto_creation
    producto.delete()
    assert not Producto.objects.filter(id_producto=producto.id_producto).exists()