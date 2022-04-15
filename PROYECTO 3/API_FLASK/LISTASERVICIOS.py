from NODOSERVICIO import NodoServicio


class ListaServicios():
    def __init__(self):
        self.primero: NodoServicio= None
        self.ultimo=None
        self.size = 0

    def inserta_al_final_servicio(self, codigopatrones):
        nuevoservicio=NodoServicio(codigopatrones)
        nuevoservicio.setidservicio(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevoservicio
            self.ultimo=nuevoservicio
        else:
           self.ultimo.setsiguiente(nuevoservicio)
           self.ultimo=nuevoservicio
        nuevoservicio.lista_alias.inserta_al_final_alias
        return nuevoservicio

    def retornar_nodo_servicio(self, id):
        aux=self.primero
        while aux.getidservicio()<id:
            aux=aux.getsiguiente()
        return aux

    def mostrar_servicios(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'\n','Servicio',tmp.getservicio())
            tmp.lista_alias.mostrar_alias()
            tmp = tmp.getsiguiente()
    

