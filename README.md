# Snake TDD

Juego Snake básico en Python, construido con TDD (Rojo → Verde → Refactor)
para el curso de Pruebas de Software.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar las pruebas

```bash
python -m pytest -v
```

## Jugar

```bash
python jugar.py
```

## Estructura

- `snake.py`: lógica pura del juego (sin E/S).
- `test_snake.py`: pruebas pytest, una por criterio de aceptación.
- `jugar.py`: interfaz de consola.
