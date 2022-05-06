from NODOPOSITIVOS import NodoPositivos

class ListaPositivos():
    def __init__(self):
        self.iniciarnodpositivos = None
        self.primero=None
        self.ultimo= None
        self.size=0

    def inserta_al_final_positivos(self, palabra_positiva):
        nuevapalabrapositiva=NodoPositivos(palabra_positiva)
        nuevapalabrapositiva.setidpositivo(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevapalabrapositiva
            self.ultimo=nuevapalabrapositiva
        else:
           self.ultimo.setsiguiente(nuevapalabrapositiva)
           self.ultimo=nuevapalabrapositiva
        return nuevapalabrapositiva

    def mostrar_positivos(self):
        tmp=self.primero
        if tmp!=None:
            for i in range(self.size):
                print("     ",i,'La palabra positiva es:', tmp.getpalabrapositiva())
                tmp = tmp.getsiguiente() 
        else:
            print('lista positivos vacía')

    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getidpositivo()< id:
            aux=aux.getsiguiente()
        palabrapositiva= aux.palabrapositiva
        return palabrapositiva

    def vaciar_lista_positivos(self):
        self.primero=None
        self.ultimo=None


        return True