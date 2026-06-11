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
