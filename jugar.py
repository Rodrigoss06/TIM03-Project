"""Interfaz de consola para el juego Snake.

Solo se encarga de dibujar el tablero, leer el teclado y llamar a
tick(). No contiene reglas del juego.
"""

import curses

from snake import Direccion, Juego

TECLAS_DIRECCION = {
    curses.KEY_UP: Direccion.ARRIBA,
    curses.KEY_DOWN: Direccion.ABAJO,
    curses.KEY_LEFT: Direccion.IZQUIERDA,
    curses.KEY_RIGHT: Direccion.DERECHA,
}


def dibujar(pantalla, juego):
    _, columnas = pantalla.getmaxyx()
    pantalla.erase()
    for y in range(juego.alto):
        fila = ""
        for x in range(juego.ancho):
            if (x, y) == juego.serpiente.cabeza:
                fila += "@"
            elif (x, y) in juego.serpiente.cuerpo:
                fila += "o"
            elif (x, y) == juego.comida:
                fila += "*"
            else:
                fila += "."
        pantalla.addstr(y, 0, fila[: columnas - 1])
    pantalla.addstr(juego.alto, 0, f"Puntaje: {juego.puntaje}"[: columnas - 1])
    pantalla.refresh()


def main(pantalla):
    curses.curs_set(0)
    pantalla.nodelay(True)
    pantalla.timeout(150)

    filas, columnas = pantalla.getmaxyx()
    ancho = min(20, columnas - 1)
    alto = min(15, filas - 2)
    juego = Juego(ancho=ancho, alto=alto)

    while not juego.terminado:
        dibujar(pantalla, juego)

        tecla = pantalla.getch()
        if tecla == ord("q"):
            return
        if tecla in TECLAS_DIRECCION:
            juego.serpiente.cambiar_direccion(TECLAS_DIRECCION[tecla])

        juego.tick()

    dibujar(pantalla, juego)
    mensaje = "Ganaste!" if juego.gano else "Game over"
    pantalla.nodelay(False)
    _, columnas = pantalla.getmaxyx()
    pantalla.addstr(juego.alto + 1, 0, f"{mensaje} Presiona una tecla para salir."[: columnas - 1])
    pantalla.refresh()
    pantalla.getch()


if __name__ == "__main__":
    curses.wrapper(main)
