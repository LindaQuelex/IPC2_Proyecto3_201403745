import json
from urllib import response
from flask import Flask, request
from manage import Manager
from flask.json import jsonify
from xml.etree import ElementTree as ET
from LISTAEMPRESAS import ListaEmpresas
from LISTAMENSAJES import ListaMsg
from LISTAPOSITIVOS import ListaPositivos
from LISTANEGATIVOS import ListaNegativos
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
import xml.dom.minidom
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

@app.route('/almacenardatosxml', methods=['GET'])
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

    empresas.mostrar_empresas()   #prueba de datos cargados en TDA??s
    #INICIA EL AN??LISIS DE LOS DATOS XML
    tam_list_mensajes=manager.tama??o_lista_mensajes()
    print('TAMA??O DE LISTA DE MENSAJES', tam_list_mensajes)
    idmensaje=0
    while idmensaje<tam_list_mensajes: 
        mensaje_analizar=msg.retornar_nodo(idmensaje)
        print('MENSAJE ORIGINAL:   ',mensaje_analizar)
        quitar=";;:,.\n!\"'"
        for caracter in quitar:
            mensaje_analizar=mensaje_analizar.replace(caracter,"")
        mensaje_analizar=mensaje_analizar.replace("??","a")
        mensaje_analizar=mensaje_analizar.replace("??","e")
        mensaje_analizar=mensaje_analizar.replace("??","i")
        mensaje_analizar=mensaje_analizar.replace("??","o")
        mensaje_analizar=mensaje_analizar.replace("??","u")
        mensaje_analizar=mensaje_analizar.replace("??","A")
        mensaje_analizar=mensaje_analizar.replace("??","E")
        mensaje_analizar=mensaje_analizar.replace("??","I")
        mensaje_analizar=mensaje_analizar.replace("??","O")
        mensaje_analizar=mensaje_analizar.replace("??","U")
        print('MENSAJES SIN SIGNOS NI TILDES:    ',mensaje_analizar)
        tam_lista_empresas=empresas.tama??o_lista_empresas()
        print('El tama??o de la lista empresas es: ', tam_lista_empresas)
        idempresa=0
        while idempresa<=tam_lista_empresas:
            name_empresa=empresas.retornarNombreEmpresa(idempresa)
            quitar=";;:,.\n!\"'"
            for caracter in quitar:
                name_empresa=name_empresa.replace(caracter,"")
            name_empresa=name_empresa.replace("??","a")
            name_empresa=name_empresa.replace("??","e")
            name_empresa=name_empresa.replace("??","i")
            name_empresa=name_empresa.replace("??","o")
            name_empresa=name_empresa.replace("??","u")
            name_empresa=name_empresa.replace("??","A")
            name_empresa=name_empresa.replace("??","E")
            name_empresa=name_empresa.replace("??","I")
            name_empresa=name_empresa.replace("??","O")
            name_empresa=name_empresa.replace("??","U")
            print('EL NOMBRE DE LA EMPRESA ES:   ',name_empresa)
            # name=name_empresa.lower()
            # print(name)
            # manager.retornar_mensaje(1)
            serch_empresa= re.findall(name_empresa,mensaje_analizar, flags=re.IGNORECASE)
            print('La empresa a analizar es:', serch_empresa)
            cantidad_empresa=len(re.findall(name_empresa,mensaje_analizar, flags=re.IGNORECASE))
            print('cantidad de repeticiones de la empresa en el mensaje=',cantidad_empresa)
            if cantidad_empresa>0:
                print('Se analizar?? el mensaje', idmensaje,'porque se si se menciona a la empresa')
                tam_lista_servicios=empresas.retornarNodoEmpresa(idempresa).Lista_servicios.tama??o_lista_servicios()
                print('El tama??o de la lista servicios es: ', tam_lista_servicios)
                idservicio=0
                while idservicio<=tam_lista_servicios:
                    name_servicio=empresas.retornarNodoEmpresa(idempresa).Lista_servicios.retornarNombreServicio(idservicio)
                    quitar=";;:,.\n!\"'"
                    for caracter in quitar:
                        name_servicio=name_servicio.replace(caracter,"")
                    name_servicio=name_servicio.replace("??","a")
                    name_servicio=name_servicio.replace("??","e")
                    name_servicio=name_servicio.replace("??","i")
                    name_servicio=name_servicio.replace("??","o")
                    name_servicio=name_servicio.replace("??","u")
                    name_servicio=name_servicio.replace("??","A")
                    name_servicio=name_servicio.replace("??","E")
                    name_servicio=name_servicio.replace("??","I")
                    name_servicio=name_servicio.replace("??","O")
                    name_servicio=name_servicio.replace("??","U")
                    print('El servicio a buscar es=', name_servicio)
                    serch_servicio=re.findall(name_servicio,mensaje_analizar, flags=re.IGNORECASE)
                    repeticiones_servicio=len(re.findall(name_servicio,mensaje_analizar, flags=re.IGNORECASE))
                    print('cantidad de repeticiones del servicio en el mensaje:', repeticiones_servicio)
                    if repeticiones_servicio>0:
                        #print(manager.get_sentimientos_positivos())
                        tam_lista_positivos=manager.tama??o_lista_positivos()
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
                        tam_lista_negativos=manager.tama??o_lista_negativos()
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
                            print('Clasificaci??n: MENSAJE POSITIVO :)')
                        elif totalpositivos< totalnegativos:
                            print('Clasificaci??n: MENSAJE NEGATIVO :(')
                        else:
                            print('Clasificaci??n: MENSAJE NEUTRO')           
                    elif repeticiones_servicio==0:
                        print('no existe servicio en el mensaje, por lo tanto se analizar?? por alias')
                        tam_lista_alias=empresas.retornarNodoEmpresa(idempresa).Lista_servicios.retornar_nodo_servicio(idservicio).lista_alias.tama??o_lista_alias()
                        print('este es el tama??o de la lista alias:=',tam_lista_alias)
                        idalias=0
                        while idalias<=tam_lista_alias:
                            name_alias=empresas.retornarNodoEmpresa(idempresa).Lista_servicios.retornar_nodo_servicio(idservicio).lista_alias.retornarNombreAlias(idalias)
                            quitar=";;:,.\n!\"'"
                            for caracter in quitar:
                                name_alias=name_alias.replace(caracter,"")
                            name_alias=name_alias.replace("??","a")
                            name_alias=name_alias.replace("??","e")
                            name_alias=name_alias.replace("??","i")
                            name_alias=name_alias.replace("??","o")
                            name_alias=name_alias.replace("??","u")
                            name_alias=name_alias.replace("??","A")
                            name_alias=name_alias.replace("??","E")
                            name_alias=name_alias.replace("??","I")
                            name_alias=name_alias.replace("??","O")
                            name_alias=name_alias.replace("??","U")
                            print('el nombre del alias a buscar es=', name_alias)
                            repeticiones_alias=len(re.findall(name_alias,mensaje_analizar, flags=re.IGNORECASE))
                            print('cantidad de repeticiones del alias en el mensaje es:', repeticiones_alias)
                            if repeticiones_alias>0:
                                print('buscar alias en mensaje y contar')
                                tam_lista_positivos=manager.tama??o_lista_positivos()
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
                                tam_lista_negativos=manager.tama??o_lista_negativos()
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
                                    print('Clasificaci??n: MENSAJE POSITIVO :)')
                                    contador_mensajes_positivos+=1
                                elif totalpositivos2< totalnegativos2:
                                    print('Clasificaci??n: MENSAJE NEGATIVO :(')
                                    contador_memsajes_negativos+=1
                                else:
                                    print('Clasificaci??n: MENSAJE NEUTRO')
                                    contador_mensajes_neutros+=1
                            if repeticiones_alias==0:
                                print('no exite alias en el mensaje, por lo tanto no se analiza')
                            idalias+=1
                    idservicio+=1
            idempresa+=1
        else: 
            print('No se analiza el msg',idmensaje,'porque no existe mencion')
        idmensaje+=1
        print('EL ID MENSAJE ES:' ,idmensaje)
    # serch_fecha= r''
    # quitar=",;:.\n!??\"'"
    # for caracter in quitar:
    #     mensaje_analizar=mensaje_analizar.replace(caracter,"")

    # print(manager.get_sentimientos_positivos())
    # print(manager.get_sentimientos_negativos())
    # print(manager.get_mensajes())
  
    return jsonify ({'msg':'prueba de funcionamiento de del m??todo "almacenar_datos_xml" de la API'}),200

@app.route('/showpositivos', methods=['GET'])
def get_positivos():
    c =manager.get_sentimientos_positivos()
    return jsonify(c),200

@app.route('/shownegativos', methods=['GET'])
def get_negativos():
    c2=manager.get_sentimientos_negativos()
    return jsonify(c2),200

@app.route('/retornarcontenidoxml', methods=['GET'])
def retornar_cont_xml():
    c2=manager.get_sentimientos_negativos()
    return jsonify(c2),200

@app.route('/crearxml', methods=['GET'])
def crearxml():
    root = ET.Element("lista_respuestas")
    respuesta = ET.SubElement(root, "respuesta")
    fecha = ET.SubElement(respuesta, "fecha") 
    fecha.text= "fechas"
    mensajes=ET.SubElement(respuesta, "mensajes")
    total=ET.SubElement(mensajes, "total")
    total.text="n??mero total"
    positivos=ET.SubElement(mensajes, "positivos")
    positivos.text="n??mero positivos"
    negativos=ET.SubElement(mensajes, "negativos")
    negativos.text="n??mero negativos"
    neutros=ET.SubElement(mensajes, "neutros")
    neutros.text="n??mero neutros"
    analisis=ET.SubElement(respuesta, "analisis")
    empresa_nombre=ET.SubElement(analisis, "empresa",atributo="nombre de la empresa")
    mensajes=ET.SubElement(empresa_nombre, "mensajes")
    total=ET.SubElement(mensajes, "total")
    total.text="n??mero total"
    positivos=ET.SubElement(mensajes, "positivos")
    positivos.text="n??mero positivos"
    negativos=ET.SubElement(mensajes, "negativos")
    negativos.text="n??mero negativos"
    neutros=ET.SubElement(mensajes, "neutros")
    neutros.text="n??mero neutros"
    servicios=ET.SubElement(empresa_nombre, "servicios")
    servicio=ET.SubElement(servicios, "servicio", name="nombre del servicio")
    mensajes=ET.SubElement(servicio, "mensajes")
    total=ET.SubElement(mensajes, "total")
    total.text="n??mero total"
    positivos=ET.SubElement(mensajes, "positivos")
    positivos.text="n??mero positivos"
    negativos=ET.SubElement(mensajes, "negativos")
    negativos.text="n??mero negativos"
    neutros=ET.SubElement(mensajes, "neutros")
    neutros.text="n??mero neutros"

    xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    xmlparse = xml.dom.minidom.parseString(xml_str)
    prettyxml = xmlparse.toprettyxml()
    print(prettyxml)
     
    archivosalida=open('ARCHIVO_SALIDA.xml','w',encoding='utf-8')
    archivosalida.write(prettyxml)
    archivosalida.close()

    # arbol = ET.ElementTree(root)
    # arbol.write("ARCHIVO_SALIDA")
    return jsonify ({'msg':'funcionamiento de creaci??n de xml'}),200

if __name__=="__main__":
    app.run(host='localhost',debug=True, port=4000)