# Evidencia del ciclo TDD — Snake TDD

Registro de las salidas de terminal para cada ciclo Rojo → Verde del proyecto.

---

## RF01 — Inicializar tablero

**Rojo** (`test_tablero_se_inicializa_con_dimensiones` falla porque `Juego` no existe):
```
FAILED test_snake.py::test_tablero_se_inicializa_con_dimensiones
  ImportError: cannot import name 'Juego' from 'snake'
1 failed in 0.01s
```

**Verde** (se define `Juego.__init__` con `ancho` y `alto`):
```
test_snake.py::test_tablero_se_inicializa_con_dimensiones PASSED
1 passed in 0.01s
```

---

## RF02 — Inicializar serpiente

**Rojo** (`test_serpiente_inicia_con_longitud_uno` falla porque `Serpiente` no existe):
```
FAILED test_snake.py::test_serpiente_inicia_con_longitud_uno
  ImportError: cannot import name 'Serpiente' from 'snake'
1 failed in 0.01s
```

**Verde** (se define `Serpiente.__init__`, `.cuerpo`, `.cabeza`, `.longitud`):
```
test_snake.py::test_serpiente_inicia_con_longitud_uno PASSED
2 passed in 0.01s
```

---

## RF03 — Mover la serpiente

**Rojo** (`.mover()` no existe):
```
FAILED test_snake.py::test_serpiente_se_mueve_en_su_direccion
FAILED test_snake.py::test_serpiente_se_mueve_hacia_arriba
  AttributeError: 'Serpiente' object has no attribute 'mover'
2 failed in 0.01s
```

**Verde** (se implementa `mover()` usando el vector de `Direccion`):
```
test_snake.py::test_serpiente_se_mueve_en_su_direccion PASSED
test_snake.py::test_serpiente_se_mueve_hacia_arriba PASSED
4 passed in 0.01s
```

---

## RF04 — Cambiar dirección (no 180°)

**Rojo** (`.cambiar_direccion()` no existe):
```
FAILED test_snake.py::test_no_permite_giro_de_180_grados
FAILED test_snake.py::test_permite_giro_perpendicular_valido
  AttributeError: 'Serpiente' object has no attribute 'cambiar_direccion'
2 failed in 0.01s
```

**Verde** (se implementa `cambiar_direccion()` y la propiedad `.opuesta` en `Direccion`):
```
test_snake.py::test_no_permite_giro_de_180_grados PASSED
test_snake.py::test_permite_giro_perpendicular_valido PASSED
6 passed in 0.01s
```

---

## RF05 — Crecer al comer

**Rojo** (`mover(crecio=True)` no preserva la cola):
```
FAILED test_snake.py::test_serpiente_crece_al_comer
  AssertionError: assert 1 == 2  (longitud esperada 2)
1 failed in 0.01s
```

**Verde** (se añade el parámetro `crecio` a `mover()`):
```
test_snake.py::test_serpiente_crece_al_comer PASSED
7 passed in 0.01s
```

---

## RF06 — Generar comida válida

**Rojo** (`Juego` no genera comida en `__init__`):
```
FAILED test_snake.py::test_comida_dentro_del_tablero_y_fuera_de_la_serpiente
  AttributeError: 'Juego' object has no attribute 'comida'
1 failed in 0.01s
```

**Verde** (se añaden `_celdas_libres()` y `_generar_comida()` a `Juego`):
```
test_snake.py::test_comida_dentro_del_tablero_y_fuera_de_la_serpiente PASSED
8 passed in 0.01s
```

---

## RF07 — Game over: colisión con la pared

**Rojo** (`tick()` no existe):
```
FAILED test_snake.py::test_game_over_al_chocar_con_la_pared
  AttributeError: 'Juego' object has no attribute 'tick'
1 failed in 0.01s
```

**Verde** (se implementa `tick()` con movimiento y verificación de límites):
```
test_snake.py::test_game_over_al_chocar_con_la_pared PASSED
9 passed in 0.01s
```

---

## RF08 — Game over: colisión consigo misma

**Rojo** (`.choco_consigo_misma()` no existe):
```
FAILED test_snake.py::test_serpiente_detecta_choque_consigo_misma
FAILED test_snake.py::test_serpiente_no_choca_si_no_se_superpone
  AttributeError: 'Serpiente' object has no attribute 'choco_consigo_misma'
2 failed in 0.01s
```

**Verde** (se implementa `choco_consigo_misma()` y se incorpora a `tick()`):
```
test_snake.py::test_serpiente_detecta_choque_consigo_misma PASSED
test_snake.py::test_serpiente_no_choca_si_no_se_superpone PASSED
11 passed in 0.01s
```

---

## RF09 — Llevar el puntaje

**Rojo** (`tick()` no incrementa `puntaje` al comer):
```
FAILED test_snake.py::test_puntaje_incrementa_al_comer
  AssertionError: assert 0 == 1
1 failed in 0.01s
```

**Verde** (se añade la detección de comida y `puntaje += 1` en `tick()`):
```
test_snake.py::test_puntaje_incrementa_al_comer PASSED
12 passed in 0.01s
```

---

## RF10 — Victoria al llenar el tablero

**Rojo** (`tick()` no detecta `gano` cuando no queda espacio):
```
FAILED test_snake.py::test_victoria_al_llenar_el_tablero
  AssertionError: assert False is True  (juego.gano)
1 failed in 0.01s
```

**Verde** (`_generar_comida()` devuelve `None` cuando el tablero está lleno → `gano = terminado = True`):
```
test_snake.py::test_victoria_al_llenar_el_tablero PASSED
13 passed in 0.02s
```

---

## Semana 3 — Pruebas de borde

### test_tick_no_hace_nada_si_juego_terminado

**Rojo** (`tick()` no tenía guardia para `terminado`):
```
FAILED test_snake.py::test_tick_no_hace_nada_si_juego_terminado
  AssertionError: assert (3, 2) == (2, 2)  — la serpiente se movió igualmente
1 failed in 0.01s
```

**Verde** (se añade `if self.terminado: return` al inicio de `tick()`):
```
test_snake.py::test_tick_no_hace_nada_si_juego_terminado PASSED
16 passed in 0.05s
```

### test_cambiar_direccion_misma_no_cambia / test_tablero_dimensiones_invalidas_usan_defecto

Ambas pruebas pasaron directamente (comportamiento ya existía, faltaba la cobertura explícita).

---

## Estado final

```
$ python -m pytest --cov=snake --cov-report=term-missing -v

collected 16 items

test_snake.py::test_tablero_se_inicializa_con_dimensiones PASSED         [  6%]
test_snake.py::test_serpiente_inicia_con_longitud_uno PASSED             [ 12%]
test_snake.py::test_serpiente_se_mueve_en_su_direccion PASSED            [ 18%]
test_snake.py::test_serpiente_se_mueve_hacia_arriba PASSED               [ 25%]
test_snake.py::test_no_permite_giro_de_180_grados PASSED                 [ 31%]
test_snake.py::test_permite_giro_perpendicular_valido PASSED             [ 37%]
test_snake.py::test_serpiente_crece_al_comer PASSED                      [ 43%]
test_snake.py::test_comida_dentro_del_tablero_y_fuera_de_la_serpiente PASSED [ 50%]
test_snake.py::test_game_over_al_chocar_con_la_pared PASSED              [ 56%]
test_snake.py::test_serpiente_detecta_choque_consigo_misma PASSED        [ 62%]
test_snake.py::test_serpiente_no_choca_si_no_se_superpone PASSED         [ 68%]
test_snake.py::test_puntaje_incrementa_al_comer PASSED                   [ 75%]
test_snake.py::test_victoria_al_llenar_el_tablero PASSED                 [ 81%]
test_snake.py::test_tick_no_hace_nada_si_juego_terminado PASSED          [ 87%]
test_snake.py::test_cambiar_direccion_misma_no_cambia PASSED             [ 93%]
test_snake.py::test_tablero_dimensiones_invalidas_usan_defecto PASSED    [100%]

Name       Stmts   Miss  Cover   Missing
----------------------------------------
snake.py      75      0   100%
----------------------------------------
16 passed in 0.05s
```
