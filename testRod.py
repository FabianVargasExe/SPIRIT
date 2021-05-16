# -*- coding: utf-8 -*-

import numpy as np

c = 0
temp = 0
tempi = 0
tempj = 0
listCaminos = []
listVelocidad= []

#Falta Orientacion, velocidad, 
class Node:
    def __init__(self, i, j,meta,posAnteriores, orientacion, tiempo):
        #Creamos las variables de cada nodo, que incluye los hijos, las posiciones anteriores,
        #orientacion, posicion, la meta, junto a si el nodo es valido (llego a la meta)
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.tiempo = 0
        #Gaurdamos la lista de posiciones anteriores en el nodo, para no repetirlas en futuros nodos
        self.posAnteriores = posAnteriores
        self.orientacion = orientacion
        self.i = i   
        self.j = j
        self.meta = meta
        self.valido = False
        #En caso que la posicion actual no sea la meta, seguiremos creando un camino
        if self.meta[0] != self.i or self.meta[1] != self.j:
            self.norte = self.crearHijo("N")
            self.sur = self.crearHijo("S")
            self.este = self.crearHijo("E")
            self.oeste = self.crearHijo("O")
        #En caso contrario, validamos el nodo como un camino a la meta
        else:
            global c
            c+=1
            self.valido = True
            print("Meta encontrada")
            print(self.posAnteriores)
    
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
        if dir == "N" and self.i>0 and "N" not in obs[self.i][self.j] and [self.i-1, self.j] not in self.posAnteriores and self.orientacion != "S":
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i - 1, self.j,self.meta,self.new_posAnteriores, "N", self.calcularTiempo("N"))
        elif dir == "S" and self.i<5 and "S" not in obs[self.i][self.j] and [self.i+1, self.j] not in self.posAnteriores and self.orientacion != "N": 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i+1, self.j,self.meta,self.new_posAnteriores, "S", self.calcularTiempo("S"))
        elif dir == "E" and self.j<7 and "E" not in obs[self.i][self.j] and [self.i, self.j+1] not in self.posAnteriores and self.orientacion != "O": 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i, self.j+1,self.meta,self.new_posAnteriores, "E", self.calcularTiempo("E"))
        elif dir == "O" and self.j>0 and "O" not in obs[self.i][self.j] and [self.i, self.j-1] not in self.posAnteriores and self.orientacion != "E": 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            return Node(self.i, self.j-1,self.meta,self.new_posAnteriores, "O", self.calcularTiempo("O"))
            


    def calcularTiempo(self, dir):
        '''
        Funcion para calcular el tiempo que se demora cada movimiento                 
        Recibimos una direccion, y en base a la posicion actual, de destino
        y el mapa se calcula el tiempo que toma aquel movimiento
        
        Este tiempo es acumulado con el de la posicion anterior, por lo que
        el tiempo de cada nodo es cuanto se demora desde el origen hasta 
        la pos del nodo actual

        '''
        global temp
        global tempi
        global tempj
        temp = 0
        #En caso de que la orientacion sea distinta, implica hacer un giro
        #con un costo de 4 segundos
        if dir != self.orientacion:
            temp+=4
        
        #Calculamos la posicion final de cada nodo
        if dir == "N" or dir == "S":
            tempj = self.j
            if dir == "N":

                tempi = self.i - 1
            else:

                tempi = self.i +1
        if dir == "E" or dir == "O":
            tempi = self.i
            if dir == "E":

                tempj = self.j + 1
            else:

                tempj = self.j -1
        #Verificamos si el suelo es liso o no
        if mapa[tempi][tempj] == "1":
            temp+=1/1.2
        elif mapa[tempi][tempj] == "2":
            temp+=1/0.5
        return temp
            

#Leemos el mapa y los obstaculos
#Estas son guardadas en dos matrices 
mapa = np.zeros((6,8))
obs = np.zeros((6,8),dtype=list)
meta = []
archMapa = open('mapa.txt', "r")
for i in range(6):
    linea = archMapa.readline().strip()
    for j in range(8):
        mapa[i][j] = int(linea[j])
        if linea[j] == "0":
            meta = [i,j]
archMapa.close()

archObs = open('obstaculos.txt',"r")
for i in range(6):
    linea = archObs.readline().strip()
    partes = linea.split(",")
    for j in range(8):
        obs[i][j] = list(partes[j])

#Creamos el nodo inicial
nodo = Node(0,0,meta,list(), "E", 0)
