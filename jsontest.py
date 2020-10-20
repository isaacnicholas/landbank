import jsonpickle
import requests
import xml.etree.ElementTree as ET

r = requests.get('http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=109-02-088')

root = ET.fromstring(r.text.lstrip())

j = {}

def iterate(root):
    i = {}
    for child in root:
        counter = 0
        found = False
        tag = ''
        while not found:
            if counter==0:
                if child.tag not in i:
                    tag = child.tag
                    found = True
            else:
                if child.tag+str(counter) not in i:
                    tag = child.tag+str(counter)
                    found = True
            counter += 1
        i[tag] = iterate(child)
    if i:
        return i
    return root.text

j = iterate(root)


print(j)
