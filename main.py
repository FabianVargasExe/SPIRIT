# SPIRIT - Taller 2 
import pygame as pg
from os import path
from collections import deque
vec = pg.math.Vector2

""" ***************************
***** Definiendo Varibles *****
****************************"""

FPS = 30
CUADRO = 48
GRIDANCHO = 28
GRIDALTO = 15
ANCHO = CUADRO * GRIDANCHO
ALTO = CUADRO * GRIDALTO


#Colores
TIERRA = (250, 215, 160)
ROJO = (231, 76, 60)
NEGRO = (145, 50, 11) 


pg.init()
screen = pg.display.set_mode((ANCHO, ALTO))
clock = pg.time.Clock()

""" ***************************
*****  Funciones/Metodos  *****
****************************"""

class Superficie:
    def __init__(self, ANCHO, ALTO):
        self.ANCHO = ANCHO
        self.ALTO = ALTO
        self.obstaculos = []
        # movimientos posibles (arriba,izq,abajo,der)
        self.conexiones = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]

    def dibujar(self):
        for obstaculo in self.obstaculos:
            rect = pg.Rect(obstaculo * CUADRO, (CUADRO, CUADRO))
            pg.draw.rect(screen, NEGRO, rect)


def dibujar_superficie():
    for x in range(0, ANCHO, CUADRO):
        pg.draw.line(screen, NEGRO, (x, 0), (x, ALTO))
    for y in range(0, ALTO, CUADRO):
        pg.draw.line(screen, NEGRO, (0, y), (ANCHO, y))

def vec2int(v):
    return (int(v.x), int(v.y))


# Generacion de la superficie y obstaculos
g = Superficie(GRIDANCHO, GRIDALTO)
obstaculos = [(10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (4,9), (3,9), (18,0), (18,1), (18,2), (18,3), (18,4), (15, 7), (16, 7), (7, 7), (6, 7), (5, 7), (5, 5), (5, 6), (1, 6), (2, 6), (3, 6), (5, 10), (5, 11), (5, 12), (5, 9), (5, 8), (12, 8), (12, 9), (12, 10), (12, 11), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10), (17, 7), (18, 7), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (22, 5), (23, 5), (24, 5), (25, 5), (18, 10), (20, 10), (19, 10), (21, 10), (22, 10), (23, 10), (14, 4), (14, 5), (14, 6), (14, 0), (14, 1), (9, 2), (9, 1), (7, 3), (8, 3), (10, 3), (9, 3), (11, 3), (2, 5), (2, 4), (2, 3), (2, 2), (2, 0), (2, 1), (0, 11), (1, 11), (2, 11), (21, 2), (20, 11), (20, 12), (23, 13), (23, 14), (24, 10), (25, 10), (6, 12), (7, 12), (10, 12), (11, 12), (12, 12), (5, 3), (6, 3), (5, 4)]
for obstaculo in obstaculos:
    g.obstaculos.append(vec(obstaculo))
start = vec(14, 8)

""" ***************************
***** Ejercución Programa *****
****************************"""

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_m:
                print([(int(loc.x), int(loc.y)) for loc in g.obstaculos])
            

    pg.display.set_caption("{:.2f}".format(clock.get_fps()))
    screen.fill(TIERRA)
    dibujar_superficie()
    g.dibujar()
    pg.display.flip()
