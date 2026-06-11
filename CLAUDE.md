CLAUDE.md — Snake TDD (UCSM, Pruebas de Software)

Guía operativa para Claude Code en este repositorio. Léela completa antes de tocar código.

Qué es este proyecto

Juego Snake básico en Python, construido con TDD real (Rojo→Verde→Refactor) para el
curso de Pruebas de Software. La nota depende de que el ciclo TDD sea genuino (test primero,
ver fallar, implementar mínimo, refactorizar) y de la separación lógica/interfaz.

Fuente de verdad (specs)

Antes de implementar cualquier RF, consulta la especificación:


Notion — hub «🐍 Snake TDD — Proyecto de Testing de Software» (usa la herramienta de Notion
para buscarlo y leer la subpágina del RF / arquitectura). Es la fuente primaria.
Local (fallback siempre disponible): docs/PROYECTO-SNAKE-TDD.md.


Si Notion no está disponible, usa el archivo local; el contenido es equivalente.

Estado / alcance actual

🎯 Objetivo actual: dejar el proyecto al nivel de la SEMANA 2. No avances a Semana 3 ni 4 salvo
que se te indique. El alcance de Semana 2 es: RF01–RF10 implementados y probados (13 tests en verde)


jugar.py funcional por consola.


Stack y comandos


Python 3.10+, pytest (única dependencia de pruebas).
Ejecutar pruebas: python -m pytest -v
Cobertura (opcional): python -m pytest --cov=snake --cov-report=term-missing
Jugar: python jugar.py


Estructura de archivos (no cambiar nombres)

snake.py        # Lógica pura: Direccion (Enum), Serpiente, Juego. SIN print/input/UI.
test_snake.py   # Pruebas pytest. Una por criterio de aceptación.
jugar.py        # Interfaz de consola. Solo render + teclado + bucle. Sin reglas de juego.
README.md
requirements.txt
pytest.ini

Reglas de arquitectura (obligatorias)


snake.py no hace I/O. Nada de print, input, ni librerías de pantalla. Debe ser
100% testeable y determinista: toda aleatoriedad pasa por random.Random(semilla).
jugar.py no contiene reglas. Solo instancia Juego, lee teclas, dibuja y llama a tick().
Clases con responsabilidad única: la auto-colisión vive en Serpiente; los límites del
tablero y la victoria viven en Juego.
Firmas y flujo de tick(): ver §4.3 y §4.4 de docs/PROYECTO-SNAKE-TDD.md. Respeta el orden
del tick(); las 13 pruebas dependen de él.


Flujo TDD que DEBES seguir (no negociable)

Por cada requerimiento funcional, en orden RF01→RF10:


🔴 ROJO — Escribe la(s) prueba(s) del RF en test_snake.py. Ejecútalas y muestra que
fallan. No escribas el código de producción todavía.
🟢 VERDE — Escribe el código mínimo en snake.py para que esa(s) prueba(s) pasen.
Vuelve a ejecutar y muestra el verde. No agregues funcionalidad no exigida por el test.
🔵 REFACTOR — Limpia el código manteniendo el verde (extrae métodos, nombres claros).
Commit del RF con mensaje convencional:

test(RFxx): <prueba> en rojo
feat(RFxx): <descripción> — verde
refactor(RFxx): <mejora>
(Puedes agrupar en un commit por RF: feat(RFxx): <RF> con TDD (rojo→verde→refactor).)





⚠️ Nunca escribas la implementación antes que la prueba. Nunca escribas las 13 pruebas de
golpe y luego todo el código: eso no es TDD y rompe el criterio del curso. Avanza RF por RF.

Las 13 pruebas (nombres exactos)

test_tablero_se_inicializa_con_dimensiones              # RF01
test_serpiente_inicia_con_longitud_uno                  # RF02
test_serpiente_se_mueve_en_su_direccion                 # RF03
test_serpiente_se_mueve_hacia_arriba                    # RF03
test_no_permite_giro_de_180_grados                      # RF04
test_permite_giro_perpendicular_valido                  # RF04
test_serpiente_crece_al_comer                           # RF05
test_comida_dentro_del_tablero_y_fuera_de_la_serpiente  # RF06
test_game_over_al_chocar_con_la_pared                   # RF07
test_serpiente_detecta_choque_consigo_misma             # RF08
test_serpiente_no_choca_si_no_se_superpone              # RF08
test_puntaje_incrementa_al_comer                        # RF09
test_victoria_al_llenar_el_tablero                      # RF10

Usa semilla fija en los tests que generan comida para que sean deterministas
(Juego(..., semilla=0)).

Definición de «hecho» (Semana 2)


 snake.py con Direccion, Serpiente, Juego.
 13 pruebas en verde con python -m pytest -v.
 jugar.py corre una partida básica por consola.
 Cada RF con su evidencia de ciclo TDD (commits separados).
 README.md con instalación y ejecución.


Idioma

Código en español para identificadores de dominio (ya definidos en la spec). Comentarios y mensajes
de commit en español. Mantén los nombres de prueba exactamente como arriba (la evidencia y el
Notion los referencian).
