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