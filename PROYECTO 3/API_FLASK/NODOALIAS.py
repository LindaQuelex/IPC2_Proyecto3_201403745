class NodoAlias():
    def __init__(self, alias ):
        self.idalias=0
        self.alias =alias
        self.siguiente = None
        self.anterior = None   

    def getalias(self):
        return self.alias

    def setalias(self, alias):
        self.alias=alias

    def getidalias(self):
        return self.idalias

    def setidalias(self, idalias):
        self.idalias=idalias

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevoalias):
        self.anterior = nuevoalias
   

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevoalias):
        self.siguiente = nuevoalias