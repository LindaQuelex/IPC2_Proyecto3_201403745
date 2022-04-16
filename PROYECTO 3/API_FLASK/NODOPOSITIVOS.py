class NodoPositivos():
    def __init__(self, palabra_positiva ):
        self.idpositivo=0
        self.palabrapositiva =palabra_positiva
        self.siguiente = None
        self.anterior = None   

    def getpalabrapositiva(self):
        return self.palabrapositiva

    def setpalabrapositiva(self, palabrapositiva):
        self.palabrapositiva=palabrapositiva

    def getidpositivo(self):
        return self.idpositivo

    def setidpositivo(self, idpositivo):
        self.idpositivo=idpositivo

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevopositivo):
        self.anterior = nuevopositivo
   

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevopositivo):
        self.siguiente = nuevopositivo