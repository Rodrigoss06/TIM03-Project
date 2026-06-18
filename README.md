# Snake TDD

Juego Snake básico en Python, construido con metodología TDD (Rojo → Verde →
Refactor) para el curso de Pruebas de Software (UCSM).

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
pip install -r requirements.txt
```

En Windows también instala `windows-curses` (ya incluido en `requirements.txt`
con el marcador de plataforma correcto).

## Ejecutar las pruebas

```bash
python -m pytest -v
```

Salida esperada: **16 passed** (13 RF01–RF10 + 3 pruebas de borde de Semana 3).

### Cobertura

```bash
python -m pytest --cov=snake --cov-report=term-missing
```

Resultado: `snake.py` → **100 %** de cobertura de líneas.

## Jugar

```bash
python jugar.py
```

| Tecla | Acción |
|-------|--------|
| ↑ ↓ ← → | Cambiar dirección |
| `r` | Reiniciar (al final de la partida) |
| `q` | Salir |

El tablero usa `@` (cabeza), `o` (cuerpo), `*` (comida) y `.` (celda vacía).
Al chocar con la pared o consigo misma aparece "Game over"; si la serpiente
llena todo el tablero, ganas. En ambos casos se muestra el puntaje final y
la opción de reiniciar o salir.

### Modo mejorado

```bash
python jugar.py --mejorado   # o -m
```

Usa símbolos Unicode y colores: cabeza/cuerpo en verde (`█` / `▓`) y comida
en rojo (`●`). Si la terminal no soporta colores, solo se muestran los símbolos.

## Estructura del proyecto

```
snake.py        — Lógica pura del juego (sin E/S). Clases: Direccion, Serpiente, Juego.
test_snake.py   — Suite pytest: 16 pruebas (RF01–RF10 + borde).
jugar.py        — Interfaz de consola: render + teclado + bucle. Sin reglas de juego.
docs/
  evidencia-tdd.md  — Capturas del ciclo Rojo → Verde por RF.
requirements.txt
pytest.ini
```

## Metodología TDD aplicada

Cada requerimiento funcional (RF01–RF10) siguió el ciclo estricto:

1. **Rojo** — se escribió la prueba y se ejecutó (`pytest`) confirmando el fallo.
2. **Verde** — se implementó el código mínimo para que la prueba pasara.
3. **Refactor** — se limpió el código sin romper ninguna prueba.

Cada ciclo quedó registrado en un commit separado con mensaje convencional
(`test(RFxx)`, `feat(RFxx)`, `refactor(RFxx)`). La evidencia de salidas de
terminal está en `docs/evidencia-tdd.md`.
