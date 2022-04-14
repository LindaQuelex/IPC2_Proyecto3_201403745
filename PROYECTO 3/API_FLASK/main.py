from flask import Flask, request
from manage import Manager
from flask.json import jsonify
from xml.etree import ElementTree as ET

app=Flask(__name__)

manager=Manager()

@app.route('/')
def index():
    return "API :)"

@app.route('/obtenerxml', methods=['POST'])
def lecturaxml():
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
                        contadortres+=1
                if tipo_diccionario.tag=='sentimientos_negativos':
                    contadorcuatro=0
                    for sentimientonegativo in tipo_diccionario:
                        palabra_negativa=sentimientonegativo.text
                        contadorcuatro+=1
                if tipo_diccionario.tag =='empresas_analizar':
                    # hasta aquí las pruebas de funcionamiento
                    contadorcinco=0
                    for empresa in tipo_diccionario:
                        contadorseis=0
                        for nombreoservicio in empresa:
                            if nombreoservicio.tag=='nombre':
                                nombre_empresa=nombreoservicio.text
                            if nombreoservicio.tag=='servicio':
                                servicio= nombreoservicio.attrib['nombre']
                                contadorsiete=0
                                for alias in nombreoservicio:
                                    aliasservicio=alias.text
                                contadorsiete+=1
                            contadorseis+=1
                        contadorcinco+=1
                contadordos+=1        
        if diccionario_mensajes.tag=='lista_mensajes':
            contadorocho=0
            for mensajes in diccionario_mensajes:
                mensaje=mensajes.text
                print(mensaje)
                contadorocho+=1
        contador+=1
                
    return jsonify ({'msg':'prueba de funcionamiento de API'}),200

if __name__=="__main__":
    app.run(host='localhost',debug=True, port=8000)