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
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.tiempo = 0
        self.posAnteriores = posAnteriores
        self.orientacion = orientacion
        self.i = i   
        self.j = j
        self.meta = meta
        self.valido = False
        if self.meta[0] != self.i or self.meta[1] != self.j:
            self.norte = self.crearHijo("N")
            self.sur = self.crearHijo("S")
            self.este = self.crearHijo("E")
            self.oeste = self.crearHijo("O")
        else:
            global c
            c+=1
            self.valido = True
            print("Meta encontrada")
            print(self.posAnteriores)
    def crearHijo(self, dir):
        if dir == "N" and self.i>0 and "N" not in obs[self.i][self.j] and [self.i-1, self.j] not in self.posAnteriores and self.orientacion != "S":
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.norte = Node(self.i - 1, self.j,self.meta,self.new_posAnteriores, "N", self.calcularTiempo("N"))
        elif dir == "S" and self.i<5 and "S" not in obs[self.i][self.j] and [self.i+1, self.j] not in self.posAnteriores and self.orientacion != "N": 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.sur = Node(self.i+1, self.j,self.meta,self.new_posAnteriores, "S", self.calcularTiempo("S"))
        elif dir == "E" and self.j<7 and "E" not in obs[self.i][self.j] and [self.i, self.j+1] not in self.posAnteriores and self.orientacion != "O": 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.este = Node(self.i, self.j+1,self.meta,self.new_posAnteriores, "E", self.calcularTiempo("E"))
        elif dir == "O" and self.j>0 and "O" not in obs[self.i][self.j] and [self.i, self.j-1] not in self.posAnteriores and self.orientacion != "E": 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.oeste = Node(self.i, self.j-1,self.meta,self.new_posAnteriores, "O", self.calcularTiempo("O"))
            
    def PrintTree(self):
        print(self.data)
    def calcularTiempo(self, dir):
        global temp
        global tempi
        global tempj
        temp = 0
        if dir != self.orientacion:
            temp+=4
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
        if mapa[tempi][tempj] == "1":
            temp+=1/1.2
        elif mapa[tempi][tempj] == "2":
            temp+=1/0.5
        return temp
            
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

nodo = Node(0,0,meta,list(), "E", 0)
