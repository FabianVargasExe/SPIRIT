import random
import numpy as np

# -*- coding: utf-8 -*-
class claseMapa:
    '''
    Clase mapa, que obtiene el tamaño del mapa en N x M, el mapa y sus obstaculos,
    junto a la posicion de la meta.
    
    '''
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
        '''       
        Funcion para generar el mapa al azar en base a N y M. Valores del mapa,
        obstaculos y meta se genera al azar.
        '''
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
        '''
        Funcion para poder leer un mapa a traves de un archivo de texto. 
        Utilizado netamente para probar el algoritmo en un comienzo, podria
        ser util mantenerlo
        '''
        self.archMapa = open(nomMapa, "r")
        for i in range(self.n):
            self.linea = self.archMapa.readline().strip()
            for j in range(self.m):
                self.mapa[i][j] = int(self.linea[j])
                if self.linea[j] == "0":
                    self.meta = [i,j]
        self.archMapa.close()
        
    def leerObstaculos(self, nomObs):
        '''
        Funcion para poder leer los obstaculos a traves de un archivo de texto. 
        Utilizado netamente para probar el algoritmo en un comienzo, podria
        ser util mantenerlo
        '''
        self.archObs = open(nomObs,"r")
        for i in range(self.n):
            self.linea = self.archObs.readline().strip()
            self.partes = self.linea.split(",")
            for j in range(self.m):
                self.obs[i][j] = list(self.partes[j])
    def getMapa(self):
        '''
        Funcion para poder obtener la matriz mapa del objeto
        '''
        return self.mapa
    
    def getObs(self):
        '''
        Funcion para poder obtener la matriz obstaculos del objeto
        '''
        return self.obs
    def getMeta(self):
        '''
        Funcion para poder obtener la meta del objeto
        '''
        return self.meta
    def getN(self):
        '''
        Funcion para poder obtener el N del objeto
        '''
        return self.n
    def getM(self):
        '''
        Funcion para poder obtener el M del objeto
        '''
        return self.m
