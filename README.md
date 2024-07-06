# Galaxy-Music

Descripcion:

Este proyecto se enfoca en analizar la productividad de los productos y facilitar herramientas para el desarrollo y análisis eficiente. Proporciona gráficos visuales clave para informar a otras áreas y ofrece una API para consultar productos listos para su venta.

Tecnologías Utilizadas
Lenguaje Backend: Python (Framework Django y Django Rest Framework)
Tecnologías Web: HTML, CSS, JavaScript, y Bootstrap como framework frontend
Base de Datos: PostgreSQL

Instalacion:

1.- Para una instalación limpia y efectiva, se recomienda el uso de Entornos Virtuales de Python:
`python -m venv nombrentornovirtual`

2.- Dentro de este ingresar los requirimientos de la pagina web:
(pip install -r requirements.txt)
3.- Configurar Base de Datos a utilizar en el archivo galaxymusicdp/settings.py
4.- Migrar tablas
(python manage.py makemigrations api
python3 manage.py migrate)
5.- Finalmente encender el local
(python manage.py runserver)
