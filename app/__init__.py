from flask import Flask, request, render_template
import jsonpickle
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

def wrap(parcel):
    r = requests.get('http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel={}'.format(parcel))
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
    return jsonpickle.encode(iterate(root))

@app.route('/api/<parcel>')
def frompage(parcel):
    return wrap(parcel)

@app.route('/api')
def fromquerystring():
    parcel = request.args.get('p','109-02-088')
    return wrap(parcel)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

@app.route('/')
def index():
    return render_template('index.html')
