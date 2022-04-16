from listas_pos_neg_msg import sent_positivos, sent_negativos, mensajes

class Manager():
    def __init__(self):
        self.lista_positivos=[]
        self.lista_negativos=[]
        self.lista_mensajes=[]
 
    def add_positivos(self, sen_positivos):
        nuevo= sent_positivos(sen_positivos)
        self.lista_positivos.append(nuevo)
        return True

    def add_negativos(self, sen_negativos):
        nuevo= sent_negativos(sen_negativos) 
        self.lista_negativos.append(nuevo)
        return True

    def add_mensajes(self, mensaje):
        nuevo=mensajes(mensaje)
        self.lista_mensajes.append(nuevo)
        return True

    def get_sentimientos_positivos(self):
        json=[]
        for k in self.lista_positivos:
            positivos={
                'palabra': k.sen_positivos,
            }
            json.append(positivos)
        return json
    
    def get_sentimientos_negativos(self):
        json=[]
        for k in self.lista_negativos:
            negativos={
                'palabra': k.sen_negativos,
            }
            json.append(negativos)
        return json

    def get_mensajes(self):
        json=[]
        for k in self.lista_mensajes:
            mensaje={
                'mensaje': k.mensaje,
            }
            json.append(mensaje)
        return json

    def tamaño_lista_mensajes(self):
        size_lista_mensajes= len(self.lista_mensajes)
        return size_lista_mensajes
        #print(size_lista_mensajes)

    def tamaño_lista_positivos(self):
        size_lista_positivos= len(self.lista_positivos)
        return size_lista_positivos
        #print(size_lista_mensajes)
    
    def retornar_mensaje(self, id):
        mensaje=self.lista_mensajes[id]
        return mensaje
  
        
        
        