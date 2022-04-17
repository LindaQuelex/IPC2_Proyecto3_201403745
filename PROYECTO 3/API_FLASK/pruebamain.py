from flask import Flask, request
from manage import Manager
from flask.json import jsonify
from xml.etree import ElementTree as ET
from LISTAEMPRESAS import ListaEmpresas
from LISTAMENSAJES import ListaMsg
from LISTAPOSITIVOS import ListaPositivos
from LISTANEGATIVOS import ListaNegativos
import re

app=Flask(__name__)

manager=Manager()
empresas=ListaEmpresas()
msg=ListaMsg()
positivos=ListaPositivos()
negativos=ListaNegativos()

@app.route('/')
def index():
    return "API :)"

@app.route('/almacenardatosxml', methods=['POST'])
def alamacenar_datos_xml():
    print('\n','****ENCABEZADOS****','\n')
    print(request.headers)
    print('****ARCHIVO XML***','\n')
    xml=request.data.decode('UTF-8')
    print (xml)
    raiz=ET.XML(xml)
    contador=0
    for diccionario_mensajes in raiz:
        if diccionario_mensajes.tag=='diccionario':
            contadordos=0
            for tipo_diccionario in diccionario_mensajes:
                if tipo_diccionario.tag=='sentimientos_positivos':
                    contadortres=0
                    for sentimientopositivo in tipo_diccionario:
                        palabra_positiva=sentimientopositivo.text
                        manager.add_positivos(palabra_positiva)
                        positivos.inserta_al_final_positivos(palabra_positiva)
                        contadortres+=1
                if tipo_diccionario.tag=='sentimientos_negativos':
                    contadorcuatro=0
                    for sentimientonegativo in tipo_diccionario:
                        palabra_negativa=sentimientonegativo.text
                        manager.add_negativos(palabra_negativa)
                        negativos.inserta_al_final_positivos(palabra_negativa)
                        contadorcuatro+=1
                if tipo_diccionario.tag =='empresas_analizar':
                    contadorcinco=0
                    for empresa in tipo_diccionario:
                        contadorseis=0
                        for nombreoservicioempresa in empresa:
                            if nombreoservicioempresa.tag=='nombre':
                                nombre_empresa=nombreoservicioempresa.text
                                empresas.inserta_al_final_empresa(nombre_empresa)
                            if nombreoservicioempresa.tag=='servicio':
                                servicio= nombreoservicioempresa.attrib['nombre']
                                empresas.retornarNodoEmpresa(contadorcinco).Lista_servicios.inserta_al_final_servicio(servicio)
                                contadorsiete=0
                                for alias in nombreoservicioempresa:
                                    aliasservicio=alias.text
                                    empresas.retornarNodoEmpresa(contadorcinco).Lista_servicios.retornar_nodo_servicio(contadorseis).lista_alias.inserta_al_final_alias(aliasservicio)
                                    contadorsiete=+1    
                                contadorseis+=1
                        contadorcinco+=1
                    contadordos+=1        
        if diccionario_mensajes.tag=='lista_mensajes':
            contadorocho=0
            for mensajes in diccionario_mensajes:
                mensaje=mensajes.text
                manager.add_mensajes(mensaje)
                msg.inserta_al_final_mensaje(mensaje)
                contadorocho+=1
        contador+=1

    #empresas.mostrar_empresas()   #prueba de datos cargados en TDA´s
    #ENCONTRAR NOMBRE DE EMPRESA
    idempresa=0
    name_empresa=empresas.retornarNombreEmpresa(idempresa)
    print(name_empresa)
    # name=name_empresa.lower()
    # print(name)
    tam_list_mensajes=manager.tamaño_lista_mensajes()
    idmensaje=0
    mensaje_analizar=msg.retornar_nodo(idmensaje)
    print(mensaje_analizar)
    # manager.retornar_mensaje(1)
    serch_empresa= re.findall(name_empresa,mensaje_analizar, flags=re.IGNORECASE)
    print('La empresa a analizar es:', serch_empresa)
    cantidad_empresa=len(re.findall(name_empresa,mensaje_analizar, flags=re.IGNORECASE))
    print('cantidad de repeticiones de la empresa en el mensaje=',cantidad_empresa)
    if cantidad_empresa>0:
        print('Se analizará el mensaje', idmensaje,'porque se si se menciona a la empresa')
        tam_lista_servicios=empresas.retornarNodoEmpresa(idempresa).Lista_servicios.tamaño_lista_servicios()
        print('El tamaño de la lista servicios es: ', tam_lista_servicios)
        idservicio=0
        while idservicio<tam_lista_servicios:
            name_servicio=empresas.retornarNodoEmpresa(idempresa).Lista_servicios.retornarNombreServicio(idservicio)
            print('El servicio a buscar es=', name_servicio)
            serch_servicio=re.findall(name_servicio,mensaje_analizar, flags=re.IGNORECASE)
            repeticiones_servicio=len(re.findall(name_servicio,mensaje_analizar, flags=re.IGNORECASE))
            print('cantidad de repeticiones del servicio en el mensaje:', repeticiones_servicio)
    #id alias que aumente con while
            idalias=0
            name_alias=empresas.retornarNodoEmpresa(idempresa).Lista_servicios.retornar_nodo_servicio(idservicio).lista_alias.retornarNombreAlias(idalias)
            print('el nombre del alias a buscar es=', name_alias)
            repeticiones_alias=len(re.findall(name_alias,mensaje_analizar, flags=re.IGNORECASE))
            print('cantidad de repeticiones del alias en el mensaje es:', repeticiones_alias)
            if repeticiones_servicio>0:
                #print(manager.get_sentimientos_positivos())
                tam_lista_positivos=manager.tamaño_lista_positivos()
                print('Total de palabras positivas a buscar=',tam_lista_positivos)
                conteopositivos=0
                idpositivo=0
                while idpositivo< tam_lista_positivos:
                    positivo=positivos.retornar_nodo(idpositivo)
                    print('palabra positiva a buscar=',positivo)
                    serch_positivos_msg= len(re.findall(positivo,mensaje_analizar, flags=re.IGNORECASE))
                    print('cantidad de veces encontradas=',serch_positivos_msg)
                    idpositivo+=1
                    conteopositivos+=serch_positivos_msg
                totalpositivos=conteopositivos
                print('TOTAL DE POSITIVOS EN EN MENSAJE=',totalpositivos)
                tam_lista_negativos=manager.tamaño_lista_negativos()
                print('Total de palabra negativas a buscar=',tam_lista_negativos)
                conteonegativos=0
                idnegativo=0
                while idnegativo<tam_lista_negativos:
                    negativo=negativos.retornar_nodo(idnegativo)
                    print('palabra negativa a buscar=',negativo)
                    serch_negativo_msg= len(re.findall(negativo,mensaje_analizar, flags=re.IGNORECASE))
                    print('cantidad de veces encontradas=',serch_negativo_msg)
                    idnegativo+=1
                    conteonegativos+=serch_negativo_msg
                totalnegativos=conteonegativos
                print('TOTAL DE NEGATIVOS EN EL MENSAJE=',totalnegativos)
                if totalpositivos>totalnegativos:
                    print('Clasificación: MENSAJE POSITIVO :)')
                elif totalpositivos< totalnegativos:
                    print('Clasificación: MENSAJE NEGATIVO :(')
                else:
                    print('Clasificación: MENSAJE NEUTRO')
            elif repeticiones_servicio==0:
                print('no existe servicio en el mensaje, por lo tanto no se analiza')

            elif repeticiones_alias>0:
                print('buscar alias en mensaje y contar')
                tam_lista_positivos=manager.tamaño_lista_positivos()
                print('Total de palabras positivas a buscar=',tam_lista_positivos)
                conteopositivos=0
                idpositivo=0
                while idpositivo< tam_lista_positivos:
                    positivo=positivos.retornar_nodo(idpositivo)
                    print('palabra positiva a buscar=',positivo)
                    serch_positivos_msg= len(re.findall(positivo,mensaje_analizar, flags=re.IGNORECASE))
                    print('cantidad de veces encontradas=',serch_positivos_msg)
                    idpositivo+=1
                    conteopositivos+=serch_positivos_msg
                totalpositivos2=conteopositivos
                print('TOTAL DE POSITIVOS EN EN MENSAJE=',totalpositivos2)
                tam_lista_negativos=manager.tamaño_lista_negativos()
                print('Total de palabra negativas a buscar=',tam_lista_negativos)
                conteonegativos=0
                idnegativo=0
                while idnegativo<tam_lista_negativos:
                    negativo=negativos.retornar_nodo(idnegativo)
                    print('palabra negativa a buscar=',negativo)
                    serch_negativo_msg= len(re.findall(negativo,mensaje_analizar, flags=re.IGNORECASE))
                    print('cantidad de veces encontradas=',serch_negativo_msg)
                    idnegativo+=1
                    conteonegativos+=serch_negativo_msg
                totalnegativos2=conteonegativos
                print('TOTAL DE NEGATIVOS EN EL MENSAJE=',totalnegativos2)
                contador_mensajes_positivos=0
                contador_memsajes_negativos=0
                contador_mensajes_neutros=0
                if totalpositivos2>totalnegativos2:
                    print('Clasificación: MENSAJE POSITIVO :)')
                    contador_mensajes_positivos+=1
                elif totalpositivos2< totalnegativos2:
                    print('Clasificación: MENSAJE NEGATIVO :(')
                    contador_memsajes_negativos+=1
                else:
                    print('Clasificación: MENSAJE NEUTRO')
                    contador_mensajes_neutros+=1
            elif repeticiones_alias==0:
                print('no exite alias en el mensaje, por lo tanton no se analiza')
            idservicio+=1
    else: 
        print('No se analiza el msg',idmensaje,'porque no existe mencion')



    # serch_fecha= r''
    # quitar=",;:.\n!¡\"'"
    # for caracter in quitar:
    #     mensaje_analizar=mensaje_analizar.replace(caracter,"")

    # print(manager.get_sentimientos_positivos())
    # print(manager.get_sentimientos_negativos())
    # print(manager.get_mensajes())

            
    return jsonify ({'msg':'prueba de funcionamiento de del método "almacenar_datos_xml" de la API'}),200

@app.route('/showpositivos', methods=['GET'])
def get_positivos():
    c =manager.get_sentimientos_positivos()
    return jsonify(c),200


if __name__=="__main__":
    app.run(host='localhost',debug=True, port=4000)