from flask import Flask, request
from manage import Manager
from flask.json import jsonify
from xml.etree import ElementTree as ET


app=Flask(__name__)

manager=Manager()

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
                        contadortres+=1
                if tipo_diccionario.tag=='sentimientos_negativos':
                    contadorcuatro=0
                    for sentimientonegativo in tipo_diccionario:
                        palabra_negativa=sentimientonegativo.text
                        manager.add_negativos(palabra_negativa)
                        contadorcuatro+=1
                if tipo_diccionario.tag =='empresas_analizar':
                    contadorcinco=0
                    for empresa in tipo_diccionario:
                        contadorseis=0
                        for nombreoservicio in empresa:
                            if nombreoservicio.tag=='nombre':
                                nombre_empresa=nombreoservicio.text
                                #LISTA DE EMPRESAS INSERTAR
                            if nombreoservicio.tag=='servicio':
                                servicio= nombreoservicio.attrib['nombre']
                                #agregar a la lista empresas la lista de servicios
                                contadorsiete=0
                                for alias in nombreoservicio:
                                    aliasservicio=alias.text
                                #agregar a la lista servicio los alias

                                contadorsiete+=1
                            contadorseis+=1
                        contadorcinco+=1
                contadordos+=1        
        if diccionario_mensajes.tag=='lista_mensajes':
            contadorocho=0
            for mensajes in diccionario_mensajes:
                mensaje=mensajes.text
                manager.add_mensajes(mensaje)
                contadorocho+=1
        contador+=1
                
    return jsonify ({'msg':'prueba de funcionamiento de del método "almacenar_datos_xml" de la API'}),200

@app.route('/showpositivos', methods=['GET'])
def get_positivos():
    c =manager.get_sentimientos_positivos()
    return jsonify(c),200


if __name__=="__main__":
    app.run(host='localhost',debug=True, port=4000)