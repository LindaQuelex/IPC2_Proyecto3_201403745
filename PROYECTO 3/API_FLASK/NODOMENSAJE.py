class NodoMensaje():
    def __init__(self, textomensaje ):
        self.idmensaje=0
        self.textomensaje =textomensaje
        self.siguiente = None
        self.anterior = None   

    def gettextomensaje(self):
        return self.textomensaje

    def settextomensaje(self, textomensaje):
        self.textomensaje=textomensaje

    def getidmensaje(self):
        return self.idmensaje

    def setidmensaje(self, idmensaje):
        self.idmensaje=idmensaje

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevomensaje):
        self.anterior = nuevomensaje
   

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevomensaje):
        self.siguiente = nuevomensaje