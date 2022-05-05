from LISTASERVICIOS import ListaServicios

class NodoEmpresa():
    def __init__(self, nombre_empresa) :
        self.idempresa=0
        self.nombre_empresa= nombre_empresa
        self.siguiente=None
        self.anterior=None
        self.Lista_servicios= ListaServicios()
    
    def setidempresa(self,idempresa):
        self.idempresa=idempresa

    def getidempresa(self):
        return self.idempresa

    def getnombre_empresa(self):
        return self.nombre_empresa
    
    def setnombre_empresa(self, nombre_empresa):
        self.nombre_empresa= nombre_empresa

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevaempresa):
        self.siguiente = nuevaempresa

    def getanterior(self):
        return self.anterior

    def setanterior(self,anterior):
        self.anterior = anterior
