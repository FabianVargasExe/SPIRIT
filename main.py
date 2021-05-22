# -*- coding: utf-8 -*-

import numpy as np
import random
import timeit
import time
class Node:
    def __init__(self, i, j,posAnteriores, orientacion, tiempo):
        global mapaPrueba
        #Creamos las variables de cada nodo, que incluye los hijos, las posiciones anteriores,
        #orientacion, posicion, la meta, junto a si el nodo es valido (llego a la meta)
        self.tiempo = tiempo
        self.padre = None
        #Gaurdamos la lista de posiciones anteriores en el nodo, para no repetirlas en futuros nodos
        self.posAnteriores = posAnteriores
        self.orientacion = orientacion
        self.i = i   
        self.j = j
        self.valido = False
        if mapaPrueba.meta[0] == self.i and mapaPrueba.meta[1] == self.j:
            self.valido = True
            self.posAnteriores.append([i,j])
  
    
    def crearHijo(self, dir):
        '''
        Funcion para continuar camino hasta la meta
        Se recibe la direccion que corresponde a un caracter en mayuscula de
        la orientacion donde se planea mover. 
        
        Luego, se verifica la direccion, que el movimiento sea valido dentro
        del mapa (no salirse de este), que el movimiento no se encuentre bloqueado
        por algun obstaculo entre la pos de origen y la pos de destino, asi como que 
        la posicion de destino no haya sido una posicion anterior, con tal de evitar
        posibles bucles infinitos, y finalmente que el movimiento no sea en 
        180 grados (Norte a sur por ejemplo)
        
        Dentro de cada condicional, guardamos las posiciones anteriores en
        una lista, y agregamos la pos de origen a esta.
        Finalmente, se guarda el nuevo nodo en la posicion correspondiente
        
        '''
        global mapaPrueba
        if dir == "N" and self.i>0 and "N" not in mapaPrueba.obs[self.i][self.j] and [self.i-1, self.j] not in self.posAnteriores:
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i - 1, self.j,self.new_posAnteriores, "N", self.calcularTiempo("N"))
        elif dir == "S" and self.i<mapaPrueba.n -1 and "S" not in mapaPrueba.obs[self.i][self.j] and [self.i+1, self.j] not in self.posAnteriores: 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i+1, self.j,self.new_posAnteriores, "S", self.calcularTiempo("S"))
        elif dir == "E" and self.j<mapaPrueba.m-1 and "E" not in mapaPrueba.obs[self.i][self.j] and [self.i, self.j+1] not in self.posAnteriores: 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i, self.j+1,self.new_posAnteriores, "E", self.calcularTiempo("E"))
        elif dir == "O" and self.j>0 and "O" not in mapaPrueba.obs[self.i][self.j] and [self.i, self.j-1] not in self.posAnteriores: 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i, self.j-1,self.new_posAnteriores, "O", self.calcularTiempo("O"))
            


    def calcularTiempo(self, dir):
        '''
        Funcion para calcular el tiempo que se demora cada movimiento                 
        Recibimos una direccion, y en base a la posicion actual, de destino
        y el mapa se calcula el tiempo que toma aquel movimiento
        
        Este tiempo es acumulado con el de la posicion anterior, por lo que
        el tiempo de cada nodo es cuanto se demora desde el origen hasta 
        la pos del nodo actual

        '''
        global mapaPrueba

        self.temp = self.tiempo
        #En caso de que la orientacion sea distinta, implica hacer un giro
        #con un costo de 4 segundos
        if dir != self.orientacion:
            if (dir == "N" and self.orientacion == "S") or (dir == "S" and self.orientacion == "N") or (dir == "E" and self.orientacion == "O") or (dir == "O" and self.orientacion == "E"):
                self.temp+=8
            else:
                self.temp+=4
        
        #Calculamos la posicion final de cada nodo
        if dir == "N" or dir == "S":
            self.tempj = self.j
            if dir == "N":

                self.tempi = self.i - 1
            else:

                self.tempi = self.i +1
        if dir == "E" or dir == "O":
            self.tempi = self.i
            if dir == "E":

                self.tempj = self.j + 1
            else:

                self.tempj = self.j -1
        #Verificamos si el suelo es liso o no
        if mapaPrueba.mapa[self.tempi][self.tempj] == 1:
            self.temp+= (1.0/1.2)
        elif mapaPrueba.mapa[self.tempi][self.tempj] == 2:
            self.temp+=(1.0/0.5)
        return self.temp
        
    def setPadre(self, padre):
        if isinstance(padre, Node):
            self.padre = padre
            

class claseMapa:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mapa = np.zeros((n,m))
        self.obs = np.zeros((n,m),dtype=list)
        for i in range(n):
            for j in range(m):
                self.obs[i][j] = []
        self.meta = []
        
    def generarMapa(self):
        for i in range(self.n):
            for j in range(self.m):
                self.mapa[i][j] = random.choice([1,2])
                if len(self.obs[i][j]) <= 1:
                    self.pared = random.choice(["N","S","E","O"])
                    if self.pared == "N" and i >0:
                        if len(self.obs[i-1][j]) <= 1 and "S" not in self.obs[i-1][j]:
                            self.obs[i][j].append("N")
                            self.obs[i-1][j].append("S")
                    elif self.pared == "S" and i <self.n-1:
                        if len(self.obs[i+1][j]) <= 1 and "N" not in self.obs[i+1][j]:
                            self.obs[i][j].append("S")
                            self.obs[i+1][j].append("N")
                    elif self.pared == "E" and j < self.m-1:
                        if len(self.obs[i][j+1]) <= 1 and "O" not in self.obs[i][j+1]:
                            self.obs[i][j].append("E")
                            self.obs[i][j+1].append("O")
                    elif self.pared == "O" and j >0:
                        if len(self.obs[i][j-1]) <= 1 and "E" not in self.obs[i][j-1]:
                            self.obs[i][j].append("O")
                            self.obs[i][j-1].append("E")
        self.meta.append(random.randrange(1,self.n))
        self.meta.append(random.randrange(1,self.m))
    def leerMapa(self, nomMapa):
        self.archMapa = open(nomMapa, "r")
        for i in range(self.n):
            self.linea = self.archMapa.readline().strip()
            for j in range(self.m):
                self.mapa[i][j] = int(self.linea[j])
                if self.linea[j] == "0":
                    self.meta = [i,j]
        self.archMapa.close()
        
    def leerObstaculos(self, nomObs):
        self.archObs = open(nomObs,"r")
        for i in range(self.n):
            self.linea = self.archObs.readline().strip()
            self.partes = self.linea.split(",")
            for j in range(self.m):
                self.obs[i][j] = list(self.partes[j])
    
def getCamino(nodo):
    camino = ""
    while nodo is not None:
        if nodo.padre is not None:
            camino= nodo.orientacion + camino
        nodo = nodo.padre
    print("Las direcciones del mejor camino son:",camino)
#Leemos el mapa y los obstaculos
#Estas son guardadas en dos matrices 

def breadthFirst(nodo):
    cola = []
    tiempo = 99999999999999999999999
    camino = []
    meta = None
    cola.append(nodo)
    while len(cola) != 0:
        if cola[0].valido == True:
            tiempo = cola[0].tiempo
            camino = cola[0].posAnteriores
            meta = cola.pop(0)
            break
        else:
            hijoN = cola[0].crearHijo("N")
            hijoS = cola[0].crearHijo("S")
            hijoE = cola[0].crearHijo("E")
            hijoO = cola[0].crearHijo("O")
            if hijoN is not None:
                hijoN.setPadre(cola[0])
                cola.append(hijoN)
            if hijoS is not None:
                hijoS.setPadre(cola[0])
                cola.append(hijoS)
            if hijoE is not None:
                hijoE.setPadre(cola[0])
                cola.append(hijoE)
            if hijoO is not None:
                hijoO.setPadre(cola[0])
                cola.append(hijoO)
            del cola[0]
    if meta is None:
        print("Ningun camino llega al punto final.")
    else:
        print("Tiempo:",tiempo,"; Camino:",camino)
        getCamino(meta)
    
    
def bestTime(nodo):
    cola = []
    tiempo = 99999999999999999999999
    camino = []
    meta = None
    cola.append(nodo)
    while len(cola) != 0:
        if cola[0].valido == True:
            if cola[0].tiempo < tiempo:
                tiempo = cola[0].tiempo
                camino = cola[0].posAnteriores
                meta = cola.pop(0)
            else:
                del cola[0]
        else:
            hijoN = cola[0].crearHijo("N")
            hijoS = cola[0].crearHijo("S")
            hijoE = cola[0].crearHijo("E")
            hijoO = cola[0].crearHijo("O")
            if hijoN is not None:
                hijoN.setPadre(cola[0])
                cola.append(hijoN)
            if hijoS is not None:
                hijoS.setPadre(cola[0])
                cola.append(hijoS)
            if hijoE is not None:
                hijoE.setPadre(cola[0])
                cola.append(hijoE)
            if hijoO is not None:
                hijoO.setPadre(cola[0])
                cola.append(hijoO)
            del cola[0]
    if meta is None:
        print("Ningun camino llega al punto final.")
    else:
        print("Tiempo:",tiempo,"; Camino:",camino)
        getCamino(meta)
    
print("Taller Sistemas Inteligentes - SPIRIT")
n = int(input("Ingrese N: "))
m = int(input("Ingrese M: "))
mapaPrueba = claseMapa(n,m) 
mapaPrueba.generarMapa()
print("Mapa de tamaño",n,"x",m,"generado. Punto de destino generado")    
origenI = random.randrange(n-1)
origenJ = random.randrange(m-1)
orientacionOrigen = random.choice(["N","S","E","O"])
nodo = Node(origenI, origenJ, list(), orientacionOrigen, 0.0)
while True:
    print("")
    print("")
    print("Menu-")
    print("1) Realizar BreadthFirst")
    print("2) Buscar mejor tiempo")
    print("3) Volver a generar mapa aleatoriamente")
    print("0) Salir")
    print("")
    opcion = int(input("Ingrese opcion: "))
    print(chr(27) + "[2J")
    print("")
    if opcion == 1:
        print("Opcion ingresada: Breadth First")
        inicio = timeit.default_timer()
        breadthFirst(nodo)
        fin = timeit.default_timer()
        print("Tiempo de ejecucion:",fin-inicio,"segundos")
    elif opcion == 2:
        print("Opcion ingresada: Mejor Tiempo")
        inicio = timeit.default_timer()
        bestTime(nodo)
        fin = timeit.default_timer()
        print("Tiempo de ejecucion:",fin-inicio,"segundos")
    elif opcion == 3:
        print("Opcion ingresada: Volver a generar mapa")
        mapaPrueba = claseMapa(n,m) 
        mapaPrueba.generarMapa()
        print("Mapa de tamaño",n,"x",m,"generado. Punto de destino generado") 
    elif opcion == 0:
        print("Opcion ingresada: Salir")
        break
    else:
        print("Opcion invalida.")
    time.sleep(0.5)

'''
print(mapaPrueba.mapa)
test = mapaPrueba.obs
for i in range(10):
    temp = ""
    for j in range(10):
        for k in range(len(test[i][j])):
            temp+=test[i][j][k]
        temp+=",\t"
    print(temp)
'''