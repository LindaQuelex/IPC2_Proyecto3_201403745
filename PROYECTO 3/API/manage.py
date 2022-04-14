from p import sent_positivos, empresa, sent_negativos, mensajes,alias_servicioem

class Manager():
    def __init__(self):
        self.lista_positivos=[]
        self.lista_negativos=[]
        self.lista_empresas=[]
        self.lista_mensajes=[]
        self.lista_alias_servicio=[]

    def add_positivos(self, sen_positivos):
        nuevo= sent_positivos(sen_positivos)
        self.lista_positivos.append(nuevo)
        return True

    def add_negativos(self, sen_negativos):
        nuevo= sent_negativos(sen_negativos) 
        self.lista_negativos.append(nuevo)
        return True

    def add_alias_servicio(self, alias_servicio):
        nuevo=alias_servicioem(alias_servicio)
        self.lista_negativos.append(nuevo)
        return True

    def add_empresas(self, nombre,servicio):
        nuevo=empresa(nombre,servicio)
        self.lista_negativos.append(nuevo)
        return True

    def add_mensajes(self, mensaje):
        nuevo=mensajes(mensaje)
        self.lista_mensajes.append(nuevo)
        return True