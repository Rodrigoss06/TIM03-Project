"""Interfaz de consola para el juego Snake.

Solo se encarga de dibujar el tablero, leer el teclado y llamar a
tick(). No contiene reglas del juego.
"""

import argparse
import curses

from snake import Direccion, Juego

TECLAS_DIRECCION = {
    curses.KEY_UP: Direccion.ARRIBA,
    curses.KEY_DOWN: Direccion.ABAJO,
    curses.KEY_LEFT: Direccion.IZQUIERDA,
    curses.KEY_RIGHT: Direccion.DERECHA,
}

SIMBOLOS_SIMPLES = {"cabeza": "@", "cuerpo": "o", "comida": "*", "vacio": "."}
SIMBOLOS_MEJORADOS = {"cabeza": "█", "cuerpo": "▓", "comida": "●", "vacio": "·"}


def _colores_mejorados():
    if not curses.has_colors():
        return {}
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    return {
        "cabeza": curses.color_pair(1) | curses.A_BOLD,
        "cuerpo": curses.color_pair(1),
        "comida": curses.color_pair(2) | curses.A_BOLD,
    }


def dibujar(pantalla, juego, simbolos, colores):
    _, columnas = pantalla.getmaxyx()
    pantalla.erase()
    for y in range(juego.alto):
        for x in range(juego.ancho):
            pos = (x, y)
            if pos == juego.serpiente.cabeza:
                clave = "cabeza"
            elif pos in juego.serpiente.cuerpo:
                clave = "cuerpo"
            elif pos == juego.comida:
                clave = "comida"
            else:
                clave = "vacio"
            pantalla.addstr(y, x, simbolos[clave], colores.get(clave, 0))
    pantalla.addstr(juego.alto, 0, f"Puntaje: {juego.puntaje}"[: columnas - 1])
    pantalla.refresh()


def _esperar_fin(pantalla, juego, simbolos, colores):
    """Muestra la pantalla final y devuelve True si el jugador quiere reiniciar."""
    dibujar(pantalla, juego, simbolos, colores)
    _, columnas = pantalla.getmaxyx()
    if juego.gano:
        linea1 = f"¡Ganaste! Puntaje final: {juego.puntaje}"
    else:
        linea1 = f"Game over. Puntaje final: {juego.puntaje}"
    linea2 = "[r] Reiniciar   [q] Salir"
    pantalla.addstr(juego.alto, 0, linea1[: columnas - 1])
    pantalla.addstr(juego.alto + 1, 0, linea2[: columnas - 1])
    pantalla.nodelay(False)
    pantalla.refresh()
    while True:
        tecla = pantalla.getch()
        if tecla in (ord("q"), ord("Q")):
            return False
        if tecla in (ord("r"), ord("R")):
            return True


def main(pantalla, mejorado):
    curses.curs_set(0)
    simbolos = SIMBOLOS_MEJORADOS if mejorado else SIMBOLOS_SIMPLES
    colores = _colores_mejorados() if mejorado else {}

    filas, columnas = pantalla.getmaxyx()
    ancho = min(20, columnas - 1)
    alto = min(15, filas - 2)

    while True:
        pantalla.nodelay(True)
        pantalla.timeout(150)
        juego = Juego(ancho=ancho, alto=alto)

        while not juego.terminado:
            dibujar(pantalla, juego, simbolos, colores)
            tecla = pantalla.getch()
            if tecla == ord("q"):
                return
            if tecla in TECLAS_DIRECCION:
                juego.serpiente.cambiar_direccion(TECLAS_DIRECCION[tecla])
            juego.tick()

        if not _esperar_fin(pantalla, juego, simbolos, colores):
            return


def parse_args():
    parser = argparse.ArgumentParser(description="Snake por consola")
    parser.add_argument(
        "-m",
        "--mejorado",
        action="store_true",
        help="usa simbolos y colores mejorados para el tablero",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    curses.wrapper(main, args.mejorado)
