class Node:
    def __init__(self, i, j,posAnteriores, orientacion, tiempo, mapaVar):
        #Creamos las variables de cada nodo, que incluye los hijos, las posiciones anteriores,
        #orientacion, posicion, la meta, junto a si el nodo es valido (llego a la meta)
        self.tiempo = tiempo
        self.padre = None
        #Gaurdamos la lista de posiciones anteriores en el nodo, para no repetirlas en futuros nodos
        self.posAnteriores = posAnteriores
        self.orientacion = orientacion
        self.i = i   
        self.j = j
        self.hijoN = None
        self.hijoS = None
        self.hijoE = None
        self.hijoO = None
        self.valido = False
        if mapaVar.getMeta()[0] == self.i and mapaVar.getMeta()[1] == self.j:
            self.valido = True
            self.posAnteriores.append([i,j])
  
    
    def crearHijo(self, dir, mapaVar):
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
        if dir == "N" and self.i>0 and "N" not in mapaVar.getObs()[self.i][self.j] and [self.i-1, self.j] not in self.posAnteriores:
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.hijoN = Node(self.i - 1, self.j,self.new_posAnteriores, "N", self.calcularTiempo("N", mapaVar), mapaVar)
            return
        elif dir == "S" and self.i<mapaVar.getN() -1 and "S" not in mapaVar.getObs()[self.i][self.j] and [self.i+1, self.j] not in self.posAnteriores: 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.hijoS = Node(self.i+1, self.j,self.new_posAnteriores, "S", self.calcularTiempo("S", mapaVar), mapaVar)
            return
        elif dir == "E" and self.j<mapaVar.getM()-1 and "E" not in mapaVar.getObs()[self.i][self.j] and [self.i, self.j+1] not in self.posAnteriores: 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.hijoE = Node(self.i, self.j+1,self.new_posAnteriores, "E", self.calcularTiempo("E", mapaVar), mapaVar)
            return
        elif dir == "O" and self.j>0 and "O" not in mapaVar.getObs()[self.i][self.j] and [self.i, self.j-1] not in self.posAnteriores: 
            self.new_posAnteriores = self.posAnteriores.copy()
            self.new_posAnteriores.append([self.i, self.j])
            self.hijoO = Node(self.i, self.j-1,self.new_posAnteriores, "O", self.calcularTiempo("O", mapaVar), mapaVar)
            return
        return     

    def obtenerHijo(self, dir):
        '''
        Funcion para obtener el hijo segun la direccion solicitada
        '''
        if dir == "N":
            return self.hijoN
        elif dir == "S":
            return self.hijoS
        elif dir == "E":
            return self.hijoE
        elif dir == "O":
            return self.hijoO
        else:
            return None
    def calcularTiempo(self, dir, mapaVar):
        '''
        Funcion para calcular el tiempo que se demora cada movimiento                 
        Recibimos una direccion, y en base a la posicion actual, de destino
        y el mapa se calcula el tiempo que toma aquel movimiento
        
        Este tiempo es acumulado con el de la posicion anterior, por lo que
        el tiempo de cada nodo es cuanto se demora desde el origen hasta 
        la pos del nodo actual

        '''

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
        if mapaVar.getMapa()[self.tempi][self.tempj] == 1:
            self.temp+= (1.0/1.2)
        elif mapaVar.getMapa()[self.tempi][self.tempj] == 2:
            self.temp+=(1.0/0.5)
        return self.temp
        
    def setPadre(self, padre):
        if isinstance(padre, Node):
            self.padre = padre