from LISTAALIAS  import ListaAlias    


class NodoServicio():
    def __init__(self, servicio ):
        self.idservicio=0
        self.servicio =servicio
        self.siguiente = None
        self.anterior = None   
        self.lista_alias=ListaAlias()

    def getservicio(self):
        return self.servicio

    def setservicio(self, servicio):
        self.servicio=servicio

    def getidservicio(self):
        return self.idservicio

    def setidservicio(self, idservicio):
        self.idservicio=idservicio

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevoservicio):
        self.anterior = nuevoservicio
   
    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevoservicio):
        self.siguiente = nuevoservicio

       
