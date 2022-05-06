import unicodedata
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

    def tamaño_lista_negativos(self):
        size_lista_negativos= len(self.lista_negativos)
        return size_lista_negativos
        #print(size_lista_mensajes)
    
    def retornar_mensaje(self, id):
        mensaje=self.lista_mensajes[id]
        return mensaje
  
    def remove_non_ascii(string:str )-> str:
        return string.encode('ascii','ignore').decode('utf-8').casefold()

    def remove_non_ascii_normalize(string:str)->str:
        normalized=unicodedata.normalize('NFD', string)
        return normalized.encode('ascii', 'ignore').decode('utf-8').casefold()

    def vaciar_positivos(self):
        self.lista_positivos.clear()
        return True

    def vaciar_negativos(self):
        self.lista_negativos.clear()
        return True

    def vaciar_mensajes(self):
        self.lista_mensajes.clear()
        return True


# string1='hola'
# string2='holá'

# print(Manager.remove_non_ascii(string2))
# print(Manager.remove_non_ascii_normalize(string2))