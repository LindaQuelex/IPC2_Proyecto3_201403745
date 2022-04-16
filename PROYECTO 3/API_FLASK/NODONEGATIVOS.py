class NodoNegativos():
    def __init__(self, palabra_negativa ):
        self.idnegativos=0
        self.palabranegativa =palabra_negativa
        self.siguiente = None
        self.anterior = None   

    def getpalabranegativa(self):
        return self.palabranegativa

    def setpalabranegativa(self, palabranegativa):
        self.palabranegativa=palabranegativa

    def getidnegativo(self):
        return self.idnegativos

    def setidnegativo(self, idnegativo):
        self.idnegativos=idnegativo

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevonegativo):
        self.anterior = nuevonegativo
   

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevonegativo):
        self.siguiente = nuevonegativo