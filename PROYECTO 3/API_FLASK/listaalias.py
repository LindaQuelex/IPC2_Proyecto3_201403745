class alias_servicioem():
    def __init__(self, alias):
        self.alias=alias
        self.id_alias=0

    def getalias_servicio(self):
        return self

    def getid_alias(self):
        return self.id_alias

    def setid_alias(self, id_alias):
        self.id_alias=id_alias

    def getnombre_alias(self):
        return self.alias

class ListaAlias():
    def __init__(self):
        self.lista_alias_servicio=[]
        self.size=0

    def add_alias_servicio(self, alias_servicio):
        nuevo=alias_servicioem(alias_servicio)
        self.size+=1
        self.lista_alias_servicio.append(nuevo)
        return nuevo.alias
      
    def retornar_nodo_alias(self, id):
        self.lista_alias_servicio[id]
    
            

prueba=ListaAlias()
prueba.add_alias_servicio('ins')
prueba.add_alias_servicio('incri')
prueba.add_alias_servicio('incripcion')

prueba.retornar_nodo_alias(0)






