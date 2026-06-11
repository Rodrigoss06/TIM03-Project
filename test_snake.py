"""Pruebas pytest para snake.py. Una por criterio de aceptación."""

from snake import Direccion, Serpiente, Juego


# RF01 — Inicializar el tablero
def test_tablero_se_inicializa_con_dimensiones():
    juego = Juego(ancho=10, alto=8)

    assert juego.ancho == 10
    assert juego.alto == 8


# RF02 — Inicializar la serpiente
def test_serpiente_inicia_con_longitud_uno():
    serpiente = Serpiente(inicio=(5, 5))

    assert serpiente.longitud == 1
    assert serpiente.cabeza == (5, 5)


# RF03 — Mover la serpiente
def test_serpiente_se_mueve_en_su_direccion():
    serpiente = Serpiente(inicio=(5, 5), direccion=Direccion.DERECHA)

    serpiente.mover()

    assert serpiente.cabeza == (6, 5)


def test_serpiente_se_mueve_hacia_arriba():
    serpiente = Serpiente(inicio=(5, 5), direccion=Direccion.ARRIBA)

    serpiente.mover()

    assert serpiente.cabeza == (5, 4)
