from NODOMENSAJE import NodoMensaje

class ListaMsg():
    def __init__(self):
        self.iniciarnodomsg = None
        self.primero=None
        self.ultimo= None
        self.size=0

    def inserta_al_final_mensaje(self, alias):
        nuevomsg=NodoMensaje(alias)
        nuevomsg.setidmensaje(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevomsg
            self.ultimo=nuevomsg
        else:
           self.ultimo.setsiguiente(nuevomsg)
           self.ultimo=nuevomsg
        return nuevomsg

    def mostrar_mensaje(self):
        tmp=self.primero
        if tmp!=None:
            for i in range(self.size):
                print("     ",i,'El mensaje es:', tmp.gettextomensaje())
                tmp = tmp.getsiguiente() 
        else: 
            print('lista mensajes vacía')

    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getidmensaje()< id:
            aux=aux.getsiguiente()
        msg= aux.textomensaje
        return msg

    def vaciar_lista_msg(self):
        self.primero=None
        self.ultimo=None


        return True