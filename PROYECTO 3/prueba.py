# import xml.etree.cElementTree as ET

# root = ET.Element("root")
# doc = ET.SubElement(root, "doc")
# nodo1 = ET.SubElement(doc, "nodo1", name="nodo")
# nodo1.text = "Texto de nodo1"
# ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"
# arbol = ET.ElementTree(root)
# arbol.write("ARCHIVOS/MENSAJES.xml")

# import xml.etree.ElementTree as ET
# from xml.dom import minidom
# def prettify(elem):
#     """Return a pretty-printed XML string for the Element.
#     """
#     rough_string = ET.tostring(elem, 'utf-8').decode('utf8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="  ")
# prtg = ET.Element("prtg")
# result = ET.SubElement(prtg,'result')
# ET.SubElement(result, "channel", name="channel").text = "Canal1"
# ET.SubElement(result, "value", name="value").text = "71"
# ET.SubElement(result, "float", name="float").text = "1"
# print (prettify(prtg))
# arbol = ET.ElementTree(prettify(prtg))
# arbol.write("ARCHIVOS/MENSAJES.xml")


import xml.etree.ElementTree as ET
from xml.dom import minidom
# def prettify(elem):
#     """Return a pretty-printed XML string for the Element.
#     """
#     rough_string = ET.tostring(elem, 'utf-8').decode('utf8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="  ")
#prtg = ET.Element("prtg")
# result = ET.SubElement(prtg,'result')
# ET.SubElement(result, "channel", name="channel").text = "Canal1"
# ET.SubElement(result, "value", name="value").text = "71"
# ET.SubElement(result, "float", name="float").text = "1"


# print (prettify(prtg))


# inicio= ET.Element("etiquetapadre")
# prueba=ET.tostring(inicio,'utf-8').decode('utf8')
# reparsed = minidom.parseString(prueba)
# reparsed2=reparsed.toprettyxml(indent="  ")
# arbol = ET.ElementTree(inicio)
# arbol.write("ARCHIVOS/MENSAJES.xml")


from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettify

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

print prettify(top)