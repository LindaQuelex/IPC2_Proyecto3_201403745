from NODOALIAS import NodoAlias

class ListaAlias():
    def __init__(self):
        self.iniciarnodoalias = None
        self.primero=None
        self.ultimo= None
        self.size=0

    def inserta_al_final_alias(self, alias):
        nuevoalias=NodoAlias(alias)
        nuevoalias.setidalias(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevoalias
            self.ultimo=nuevoalias
        else:
           self.ultimo.setsiguiente(nuevoalias)
           self.ultimo=nuevoalias
        return nuevoalias

    def recorrer_lista(self):
        if self.iniciarnodoalias is None:
            print("La lista no tiene alias del servicio")
            return
        else:
            nuevo = self.iniciarnodoalias
            while nuevo is not None:
                print("La lista de alias del servicios es:",nuevo.alias , "funciona el método de recorrer lista")    
                nuevo = nuevo.siguiente

    def mostrar_alias(self):
        tmp=self.primero
        for i in range(self.size):
            print("     ",i,'El alias es:', tmp.getalias())
            tmp = tmp.getsiguiente() 

    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getidalias()< id:
            aux=aux.getsiguiente()
        #print(aux.idalias, aux.alias)
        return aux



# nodo=ListaAlias()

# n1=NodoAlias('incripción')
# n2=NodoAlias('ins')
# n3=NodoAlias('inscripc')

# nodo.inserta_al_final_alias(n1.alias)
# nodo.inserta_al_final_alias(n2.alias)
# nodo.inserta_al_final_alias(n3.alias)

# nodo.mostrar_alias()

# nodo.retornar_nodo(2)


