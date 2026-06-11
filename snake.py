"""Lógica pura del juego Snake.

Este módulo no realiza ninguna operación de E/S (sin print, input, ni
librerías de pantalla). Toda la aleatoriedad debe pasar por
random.Random(semilla) para que el comportamiento sea determinista.
"""

import random
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

    @property
    def opuesta(self):
        opuestas = {
            Direccion.ARRIBA: Direccion.ABAJO,
            Direccion.ABAJO: Direccion.ARRIBA,
            Direccion.IZQUIERDA: Direccion.DERECHA,
            Direccion.DERECHA: Direccion.IZQUIERDA,
        }
        return opuestas[self]


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

    def mover(self, crecio=False):
        dx, dy = self.direccion.value
        x, y = self.cabeza
        nueva_cabeza = (x + dx, y + dy)
        if crecio:
            self.cuerpo = [nueva_cabeza] + self.cuerpo
        else:
            self.cuerpo = [nueva_cabeza] + self.cuerpo[:-1]

    def cambiar_direccion(self, nueva_direccion):
        if nueva_direccion != self.direccion.opuesta:
            self.direccion = nueva_direccion

    def choco_consigo_misma(self):
        return self.cabeza in self.cuerpo[1:]


class Juego:
    """Coordina el tablero, la serpiente, la comida y el puntaje."""

    def __init__(self, ancho=20, alto=20, inicio=None, semilla=None):
        if ancho <= 0 or alto <= 0:
            ancho, alto = 20, 20
        self.ancho = ancho
        self.alto = alto

        if inicio is None:
            inicio = (ancho // 2, alto // 2)
        self.serpiente = Serpiente(inicio)

        self._random = random.Random(semilla)
        self.puntaje = 0
        self.terminado = False
        self.gano = False
        self.comida = self._generar_comida()

    def _celdas_libres(self):
        todas = {(x, y) for x in range(self.ancho) for y in range(self.alto)}
        return todas - set(self.serpiente.cuerpo)

    def _generar_comida(self):
        libres = self._celdas_libres()
        if not libres:
            return None
        return self._random.choice(sorted(libres))

    def _fuera_de_limites(self, pos):
        x, y = pos
        return not (0 <= x < self.ancho and 0 <= y < self.alto)

    def tick(self):
        dx, dy = self.serpiente.direccion.value
        x, y = self.serpiente.cabeza
        siguiente = (x + dx, y + dy)
        comio = siguiente == self.comida

        self.serpiente.mover(crecio=comio)

        if self._fuera_de_limites(self.serpiente.cabeza) or self.serpiente.choco_consigo_misma():
            self.terminado = True
            return

        if comio:
            self.puntaje += 1
            self.comida = self._generar_comida()
