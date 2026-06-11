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

Controles: flechas para cambiar de dirección, `q` para salir. El tablero se
dibuja con `@` (cabeza), `o` (cuerpo), `*` (comida) y `.` (celda vacía). Al
chocar con la pared o consigo misma termina la partida (game over); si la
serpiente llena todo el tablero, ganas.

### Modo mejorado

```bash
python jugar.py --mejorado
```

(o `python jugar.py -m`). Usa símbolos y colores: cabeza/cuerpo en verde
(`█`/`▓`) y comida en rojo (`●`). Si la terminal no soporta colores, se
muestran solo los símbolos.

## Estructura

- `snake.py`: lógica pura del juego (sin E/S). Contiene `Direccion`,
  `Serpiente` y `Juego`.
- `test_snake.py`: pruebas pytest, una por criterio de aceptación (RF01–RF10).
- `jugar.py`: interfaz de consola (render + teclado), sin reglas de juego.
