"""Lógica pura del juego Snake.

Este módulo no realiza ninguna operación de E/S (sin print, input, ni
librerías de pantalla). Toda la aleatoriedad debe pasar por
random.Random(semilla) para que el comportamiento sea determinista.
"""

from enum import Enum


class Direccion(Enum):
    """Direcciones posibles de movimiento de la serpiente.

    Cada miembro guarda su vector de desplazamiento (dx, dy), con el eje
    Y creciendo hacia abajo (convención de filas/columnas del tablero).
    """

    ARRIBA = (0, -1)
    ABAJO = (0, 1)
    IZQUIERDA = (-1, 0)
    DERECHA = (1, 0)


class Serpiente:
    """Representa a la serpiente: su cuerpo y su movimiento."""

    def __init__(self, inicio, direccion=Direccion.DERECHA):
        self.cuerpo = [inicio]
        self.direccion = direccion

    @property
    def cabeza(self):
        return self.cuerpo[0]

    @property
    def longitud(self):
        return len(self.cuerpo)

    def mover(self):
        dx, dy = self.direccion.value
        x, y = self.cabeza
        self.cuerpo = [(x + dx, y + dy)] + self.cuerpo[:-1]


class Juego:
    """Coordina el tablero, la serpiente, la comida y el puntaje."""

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
