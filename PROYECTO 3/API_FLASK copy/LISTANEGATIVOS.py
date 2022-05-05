from NODONEGATIVOS import NodoNegativos

class ListaNegativos():
    def __init__(self):
        self.iniciarnodopositivos = None
        self.primero=None
        self.ultimo= None
        self.size=0

    def inserta_al_final_positivos(self, palabra_negativa):
        nuevapalabranegativa=NodoNegativos(palabra_negativa)
        nuevapalabranegativa.setidnegativo(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevapalabranegativa
            self.ultimo=nuevapalabranegativa
        else:
           self.ultimo.setsiguiente(nuevapalabranegativa)
           self.ultimo=nuevapalabranegativa
        return nuevapalabranegativa

    def mostrar_negativos(self):
        tmp=self.primero
        for i in range(self.size):
            print("     ",i,'La palabra negativa es:', tmp.getpalabranegativa())
            tmp = tmp.getsiguiente() 

    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getidnegativo()< id:
            aux=aux.getsiguiente()
        palabranegativa= aux.palabranegativa
        return palabranegativa

