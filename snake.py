"""Lógica pura del juego Snake.

Este módulo no realiza ninguna operación de E/S (sin print, input, ni
librerías de pantalla). Toda la aleatoriedad debe pasar por
random.Random(semilla) para que el comportamiento sea determinista.
"""

from enum import Enum


class Direccion(Enum):
    """Direcciones posibles de movimiento de la serpiente."""


class Serpiente:
    """Representa a la serpiente: su cuerpo y su movimiento."""


class Juego:
    """Coordina el tablero, la serpiente, la comida y el puntaje."""

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
