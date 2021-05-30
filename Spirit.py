# -*- coding: utf-8 -*-

import random
import timeit
import time
import node
import mapa
class Spirit:
    def __init__(self):
        print("Taller Sistemas Inteligentes - SPIRIT")
        self.n = int(input("Ingrese N: "))
        self.m = int(input("Ingrese M: "))
        self.mapaPrueba = mapa.claseMapa(self.n,self.m) 
        self.mapaPrueba.generarMapa()
        print("Mapa de tamaño",self.n,"x",self.m,"generado. Punto de destino generado")    
        self.origenI = random.randrange(self.n-1)
        self.origenJ = random.randrange(self.m-1)
        self.orientacionOrigen = random.choice(["N","S","E","O"])
        self.nodo = node.Node(self.origenI, self.origenJ, list(), self.orientacionOrigen, 0.0, self.mapaPrueba)
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
                self.inicio = timeit.default_timer()
                self.breadthFirst(self.nodo)
                self.fin = timeit.default_timer()
                print("Tiempo de ejecucion:",self.fin-self.inicio,"segundos")
            elif opcion == 2:
                print("Opcion ingresada: Mejor Tiempo")
                self.inicio = timeit.default_timer()
                self.bestTime(self.nodo)
                self.fin = timeit.default_timer()
                print("Tiempo de ejecucion:",self.fin-self.inicio,"segundos")
            elif opcion == 3:
                print("Opcion ingresada: Volver a generar mapa")
                self.mapaPrueba = mapa.claseMapa(self.n,self.m) 
                self.mapaPrueba.generarMapa()
                print("Mapa de tamaño",self.n,"x",self.m,"generado. Punto de destino generado") 
            elif opcion == 0:
                print("Opcion ingresada: Salir")
                break
            else:
                print("Opcion invalida.")
            time.sleep(0.5)

    def getCamino(self, nodo):
        '''
        Funcion para poder obtener el camino desde el nodo final (meta) hasta la
        raiz. Se imprime por pantalla las direcciones desde el origen hasta la meta
        '''
        
        camino = ""
        while nodo is not None:
            if nodo.padre is not None:
                camino= nodo.orientacion + camino
            nodo = nodo.padre
        print("Las direcciones del mejor camino son:",camino)
    
    
    def breadthFirst(self, nodo):
        '''
        Funcion para poder llegar a la meta a traves de Breadth First. 
        Utilizamos una cola para ir guardando los nodos que serán  recorridos,
        segun el orden del algoritmo. A esta cola solamente se agregarán aquellos
        hijos que existen (no habrán nodos nulos). Se termina una vez se encuentra
        la meta, o la cola se queda vacia por que no existe un camino a la meta.
        
        '''
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
                cola[0].crearHijo("N", self.mapaPrueba)
                cola[0].crearHijo("S", self.mapaPrueba)
                cola[0].crearHijo("E", self.mapaPrueba)
                cola[0].crearHijo("O", self.mapaPrueba)
                hijoN = cola[0].obtenerHijo("N")
                hijoS = cola[0].obtenerHijo("S")
                hijoE = cola[0].obtenerHijo("E")
                hijoO = cola[0].obtenerHijo("O")
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
            self.getCamino(meta)
        
        
    def bestTime(self, nodo):
        '''
        Funcion para buscar el camino más rapido a la meta. 
        Utilizamos una cola para ir guardando los nodos que serán  recorridos,
        segun el orden del algoritmo. A esta cola solamente se agregarán aquellos
        hijos que existen (no habrán nodos nulos). Se termina una vez se recorran
        todos los caminos posibles, y muestra por pantalla el mejor nodo.
        
        '''
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
                cola[0].crearHijo("N", self.mapaPrueba)
                cola[0].crearHijo("S", self.mapaPrueba)
                cola[0].crearHijo("E", self.mapaPrueba)
                cola[0].crearHijo("O", self.mapaPrueba)
                hijoN = cola[0].obtenerHijo("N")
                hijoS = cola[0].obtenerHijo("S")
                hijoE = cola[0].obtenerHijo("E")
                hijoO = cola[0].obtenerHijo("O")
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
            self.getCamino(meta)
        
Spirit()