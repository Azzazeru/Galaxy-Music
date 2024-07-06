# Galaxy-Music

Descripcion:

Este proyecto se enfoca en analizar la productividad de los productos y facilitar herramientas para el desarrollo y análisis eficiente. Proporciona gráficos visuales clave para informar a otras áreas y ofrece una API para consultar productos listos para su venta.

- Tecnologías Utilizadas:
  - Lenguaje Backend: Python (Framework Django y Django Rest Framework)
  - Tecnologías Web: HTML, CSS, JavaScript, y Bootstrap como framework frontend
  - Base de Datos: PostgreSQL

Instalacion:

1. Para una instalación limpia y efectiva, se recomienda el uso de Entornos Virtuales de Python:
```bash
python -m venv nombrentornovirtual
```

2. Dentro de este ingresar los requirimientos de la pagina web:
```bash
python install -r requirements.txt
```

3. Configurar Base de Datos a utilizar en el archivo galaxymusicdp/settings.py (Se recomienda el uso de variables de entorno .env)

```python
from dotenv import load_dotenv
  DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
```

4. Migrar tablas
```bash
python manage.py makemigrations api
```
```bash
python manage.py migrate
```

5. Finalmente ejecutar en modo local local
```bash
python manage.py runserver
```
Uso:

Accede a la API a través de:

- API General: https://gmad.up.railway.app/api/public/
- Productos Aprobados: https://gmad.up.railway.app/api/public/productos/?estado=true

Contribución:

- Aaron Fuentes (Azzazeru): Programador Backend
- Octavio Figueroa (OctavioCDS): Programador Frontend
