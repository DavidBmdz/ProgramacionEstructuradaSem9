# Visualizador de pila con Flask

## Requisitos
- Python 3.10 o superior
- Conexión a internet para cargar Bootstrap desde CDN

## Instalación
En una terminal, dentro de esta carpeta:

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Instala Flask:
```bash
pip install -r requirements.txt
```

Ejecuta:
```bash
python app.py
```

Abre http://127.0.0.1:5000 en el navegador.

## Buenas prácticas y límites
- Las operaciones están separadas en funciones pequeñas.
- Se valida la capacidad como entero positivo y se rechazan elementos vacíos.
- Se controla el desbordamiento y el subdesbordamiento de la pila.
- Los formularios usan POST y redirección después de procesar operaciones.
- La plantilla usa el escape automático de Jinja para mostrar entradas de usuario.
- La pila y su capacidad viven en memoria: al reiniciar el servidor se pierden y varios usuarios compartirían el mismo estado. Para uso multiusuario, se debe guardar estado por sesión o usar una base de datos.
- Cambia `SECRET_KEY` por una variable de entorno antes de desplegar.
- `debug=True` es solo para desarrollo local; no debe usarse en producción.
