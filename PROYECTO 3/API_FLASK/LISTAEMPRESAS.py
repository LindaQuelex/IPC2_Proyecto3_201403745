from NODOEMPRESA import NodoEmpresa

class ListaEmpresas():
    def __init__(self):
        self.primero: NodoEmpresa= None
        self.ultimo=None
        self.size = 0

    def inserta_al_final_empresa(self, nombreempresa):
        nuevaempresa=NodoEmpresa(nombreempresa)
        nuevaempresa.setidempresa(self.size)
        self.size += 1 
        if self.primero is None: 
            self.primero=nuevaempresa
            self.ultimo=nuevaempresa
        else:
           self.ultimo.setsiguiente(nuevaempresa)
           self.ultimo=nuevaempresa
        nuevaempresa.Lista_servicios.inserta_al_final_servicio
        return nuevaempresa
    
    def retornarNodoEmpresa(self,id):
        aux = self.primero
        while aux.getidempresa()<id:
            aux=aux.getsiguiente()
        return aux

    def mostrar_empresas(self):
        tmp=self.primero
        if tmp!=None:
            for i in range(self.size):
                print(i,'El nombre de la empresa es:', tmp.getnombre_empresa())
                tmp.Lista_servicios.mostrar_servicios()
                tmp = tmp.getsiguiente()
        else:
            print('lista empresas vacía')

    def retornarNombreEmpresa(self,id):
        aux = self.primero
        while aux.getidempresa()<id:
            aux=aux.getsiguiente()
        nombreempresa=aux.nombre_empresa
        return nombreempresa


    def tamaño_lista_empresas(self):
        aux=self.ultimo
        idultimo=aux.idempresa
        #print(idultimo)
        return idultimo

    def mostrar_empresas_json(self):
        tmp=self.primero
        json=[]
        for i in range(self.size):
            empresa={
                'empresa':tmp.getnombre_empresa(),                
                #tmp.Lista_servicios.retornarNombreServicio()
            }
            json.append(empresa)
            tmp = tmp.getsiguiente()
        return json


    def vaciar_lista_empresa(self):
        self.primero=None
        self.ultimo=None
        return True