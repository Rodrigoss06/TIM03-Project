# Guion de Exposición — Snake TDD
### Pruebas de Software · UCSM · Semana 4
**Duración estimada: 10–15 minutos**

---

## 1. Nombre y objetivo del juego

**Nombre:** Snake TDD

**Objetivo del juego:** Controlar una serpiente en un tablero de cuadrícula.
La serpiente se mueve continuamente y el jugador cambia su dirección con las
flechas del teclado. Cada vez que la serpiente come la comida que aparece en el
tablero, crece en longitud y el puntaje sube. La partida termina si la serpiente
choca contra la pared o contra sí misma. La victoria se logra cuando la serpiente
ocupa cada celda del tablero.

**Objetivo del proyecto:** Demostrar la metodología TDD (_Test-Driven Development_)
aplicada desde cero a un proyecto real en Python, con separación de responsabilidades
entre la lógica del juego y la interfaz de usuario.

---

## 2. Reglas principales y requerimientos funcionales

| # | RF | Descripción |
|---|-----|-------------|
| RF01 | Tablero | El juego se inicializa con dimensiones configurables (ancho × alto). |
| RF02 | Serpiente | La serpiente empieza con longitud 1 en el centro del tablero. |
| RF03 | Movimiento | La serpiente avanza una celda por tick en su dirección actual. |
| RF04 | Giro | Puede girar 90°, pero no 180° (no puede invertir su dirección). |
| RF05 | Crecimiento | Al comer la comida, la serpiente crece en una celda. |
| RF06 | Comida | La comida aparece aleatoriamente en una celda libre del tablero. |
| RF07 | Derrota (pared) | Si la cabeza sale del tablero, la partida termina en game over. |
| RF08 | Derrota (cuerpo) | Si la cabeza choca con el propio cuerpo, también es game over. |
| RF09 | Puntaje | El puntaje incrementa en 1 cada vez que se come la comida. |
| RF10 | Victoria | Cuando la serpiente llena todo el tablero, el jugador gana. |

**Reglas de arquitectura aplicadas:**
- `snake.py` contiene únicamente lógica pura — sin ninguna operación de E/S.
- `jugar.py` contiene únicamente la presentación — sin ninguna regla de juego.
- Toda la aleatoriedad pasa por `random.Random(semilla)` para que las pruebas sean deterministas.

---

## 3. ¿Qué es TDD?

TDD (_Test-Driven Development_) es una técnica de desarrollo de software en la que
**primero se escribe la prueba** y luego el código de producción. El ciclo tiene tres fases:

```
🔴 ROJO   → Se escribe la prueba. Se ejecuta y FALLA (el código aún no existe).
🟢 VERDE  → Se escribe el código MÍNIMO para que la prueba pase.
🔵 REFACTOR → Se limpia el código sin romper ninguna prueba.
```

**¿Por qué TDD?**
- Obliga a pensar en el comportamiento esperado antes de implementar.
- Cada prueba es un contrato verificable automáticamente.
- El refactor es seguro porque la suite de pruebas actúa como red de seguridad.
- Resultado: código más simple, bien estructurado y con alta cobertura de pruebas.

---

## 4. Ejemplo real del ciclo TDD: RF05 — Crecer al comer

Este es uno de los ciclos más ilustrativos del proyecto porque muestra cómo
la prueba define con precisión qué debe hacer el código.

### Paso 1 — Escribir la prueba (antes de que exista el código)

```python
# test_snake.py — RF05
def test_serpiente_crece_al_comer():
    serpiente = Serpiente(inicio=(5, 5), direccion=Direccion.DERECHA)

    serpiente.mover(crecio=True)

    assert serpiente.longitud == 2
    assert serpiente.cabeza == (6, 5)
    assert serpiente.cuerpo == [(6, 5), (5, 5)]
```

### Paso 2 — Ejecutar: la prueba FALLA (rojo)

En este momento `mover()` no tenía el parámetro `crecio`, así que al ejecutar
`python -m pytest -v` se obtiene:

```
FAILED test_snake.py::test_serpiente_crece_al_comer
  TypeError: mover() got an unexpected keyword argument 'crecio'
1 failed in 0.01s
```

### Paso 3 — Implementar el código mínimo (verde)

```python
# snake.py — Serpiente.mover()
def mover(self, crecio=False):
    dx, dy = self.direccion.value
    x, y = self.cabeza
    nueva_cabeza = (x + dx, y + dy)
    if crecio:
        self.cuerpo = [nueva_cabeza] + self.cuerpo      # conserva la cola
    else:
        self.cuerpo = [nueva_cabeza] + self.cuerpo[:-1] # descarta la cola
```

Solo se agregó el parámetro `crecio` y la bifurcación. Nada más.

### Paso 4 — Ejecutar: la prueba PASA (verde)

```
test_snake.py::test_serpiente_crece_al_comer PASSED
7 passed in 0.01s
```

### Paso 5 — Refactor

El código ya era claro y sin duplicación, así que el refactor consistió en
verificar que los nombres eran descriptivos (`nueva_cabeza`, `crecio`) y
que no había lógica redundante. Las pruebas anteriores continuaron en verde.

---

## 5. Guion de la demo en vivo

### 5.1 Ejecutar la suite de pruebas

```bash
python -m pytest -v
```

**Qué mostrar y resaltar:**
- Que aparecen los 16 tests con sus nombres descriptivos (uno por criterio de aceptación).
- Que todos pasan (`16 passed`).
- Opcional: mostrar cobertura al 100%:

```bash
python -m pytest --cov=snake --cov-report=term-missing
```

### 5.2 Correr el juego

```bash
python jugar.py
```

**Pasos durante la demo:**
1. Mostrar el tablero inicial con la serpiente (`@`) y la comida (`*`).
2. Mover la serpiente con las flechas — demostrar que no puede girar 180°.
3. Comer la comida y mostrar que el puntaje sube y la serpiente crece.
4. Chocar con la pared (o el cuerpo) para mostrar el game over.
5. Presionar `r` para reiniciar y `q` para salir.

### 5.3 Modo mejorado (opcional)

```bash
python jugar.py --mejorado
```

Muestra los mismos controles pero con símbolos Unicode (`█` / `▓` / `●`) y
colores (verde para la serpiente, rojo para la comida).

---

## 6. Conclusiones y dificultades encontradas

*(El equipo completa estas viñetas antes de la exposición.)*

### Conclusiones

- [ ] La metodología TDD garantizó que **cada funcionalidad fuera testeable** desde el
  momento en que fue diseñada.
- [ ] La separación `snake.py` / `jugar.py` permitió probar la lógica de forma
  totalmente independiente de la interfaz.
- [ ] La cobertura del 100 % en `snake.py` fue consecuencia natural del ciclo TDD,
  no un objetivo perseguido a posteriori.
- [ ] *(añadir conclusión del equipo)*
- [ ] *(añadir conclusión del equipo)*

### Dificultades encontradas

- [ ] *(describir una dificultad real: p. ej. el orden del tick(), la detección de victoria,
  el manejo de `curses` en distintos sistemas operativos, etc.)*
- [ ] *(describir cómo se resolvió)*
- [ ] *(añadir otra dificultad si aplica)*

---

## Checklist de la demo

Ejecutar en este orden antes y durante la exposición:

- [ ] Abrir terminal en la carpeta del proyecto.
- [ ] `pip install -r requirements.txt` (verificar que no haya errores).
- [ ] `python -m pytest -v` → confirmar **16 passed**.
- [ ] `python -m pytest --cov=snake --cov-report=term-missing` → confirmar **100 %**.
- [ ] `python jugar.py` → jugar una partida completa hasta game over.
- [ ] Al terminar, presionar `r` para reiniciar → mostrar que funciona.
- [ ] Cerrar con `q`.
- [ ] (Opcional) `python jugar.py --mejorado` → mostrar modo con colores.
- [ ] Tener `snake.py` y `test_snake.py` abiertos en el editor para mostrar el ejemplo TDD.
- [ ] Tener `docs/evidencia-tdd.md` listo para mostrar la evidencia del ciclo rojo/verde.
