class sent_positivos():
    def __init__(self,sen_positivos):
        self.sen_positivos=sen_positivos

    def getsen_positivos(self):
        return self

class sent_negativos():
    def __init__(self,sen_negativos):
        self.sen_negativos=sen_negativos

    def getsen_negativos(self):
        return self

class empresa():
    def __init__(self, nombre):
        self.nombre=nombre
        self.lista_servicios=[]
        
    def getnombre_empresa(self):
        return self

class servicioem():
    def __init__(self, servicios):
        self.servicios=servicios
        self.lista_aliasservicios=[]

    def getservicio(self):
        return self

class alias_servicioem():
    def __init__(self, alias):
        self.alias=alias

    def getalias_servicio(self):
        return self

class mensajes():
    def __init__(self, mensaje):
        self.mensaje=mensaje

    def getmensaje(self):
        return self




