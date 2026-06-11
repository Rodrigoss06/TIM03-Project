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


# RF04 — Cambiar dirección (no 180°)
def test_no_permite_giro_de_180_grados():
    serpiente = Serpiente(inicio=(5, 5), direccion=Direccion.DERECHA)

    serpiente.cambiar_direccion(Direccion.IZQUIERDA)

    assert serpiente.direccion == Direccion.DERECHA


def test_permite_giro_perpendicular_valido():
    serpiente = Serpiente(inicio=(5, 5), direccion=Direccion.DERECHA)

    serpiente.cambiar_direccion(Direccion.ARRIBA)

    assert serpiente.direccion == Direccion.ARRIBA


# RF05 — Crecer al comer
def test_serpiente_crece_al_comer():
    serpiente = Serpiente(inicio=(5, 5), direccion=Direccion.DERECHA)

    serpiente.mover(crecio=True)

    assert serpiente.longitud == 2
    assert serpiente.cabeza == (6, 5)
    assert serpiente.cuerpo == [(6, 5), (5, 5)]
