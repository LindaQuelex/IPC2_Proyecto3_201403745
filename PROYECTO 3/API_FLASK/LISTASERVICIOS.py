from NODOSERVICIO import NodoServicio


class ListaServicios():
    def __init__(self):
        self.iniciarnodoservicio=None
        self.primero: NodoServicio= None
        self.ultimo=None
        self.size = 0

    def inserta_al_final_servicio(self, nombreservicio):
        nuevoservicio=NodoServicio(nombreservicio)
        nuevoservicio.setidservicio(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevoservicio
            self.ultimo=nuevoservicio
        else:
           self.ultimo.setsiguiente(nuevoservicio)
           self.ultimo=nuevoservicio
        nuevoservicio.lista_alias.inserta_al_final_alias
        self.iniciarnodoservicio=nuevoservicio
        return nuevoservicio

    def retornar_nodo_servicio(self, id):
        aux=self.primero
        while aux.getidservicio()<id:
            aux=aux.getsiguiente()
        print(aux.servicio)
        return aux

    def mostrar_servicios(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'Servicio:',tmp.getservicio())
            tmp.lista_alias.mostrar_alias()
            tmp = tmp.getsiguiente()
    
    
    # def recorrer_lista(self):
    #     if self.iniciarnodoservicio is None:
    #         print("La lista no tiene elementos")
    #         return
    #     else:
    #         nuevo = self.iniciarnodoservicio
    #         while nuevo is not None:
    #             print("La lista de celdas es:",nuevo.nuevoservicio, "funciona el método de recorrer lista")    
    #             nuevo = nuevo.siguiente
                
    def retornarNombreServicio(self,id):
        aux = self.primero
        while aux.getidservicio()<id:
            aux=aux.getsiguiente()
        nombreservicio=aux.servicio
        return nombreservicio




# nodo=ListaServicios()

# n1=NodoServicio('incripción')
# n2=NodoServicio('ins')
# n3=NodoServicio('inscripc')

# nodo.inserta_al_final_servicio(n1.servicio)
# nodo.inserta_al_final_servicio(n2.servicio)
# nodo.inserta_al_final_servicio(n3.servicio)

# nodo.mostrar_servicios()

# nodo.retornar_nodo_servicio(1)

