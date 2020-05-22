from flask import Flask, jsonify, request

app = Flask(__name__)

from UNIVERSO import UNIVERSO

@app.route("/")
def saludo():
    return("Bienvenido a la API Universo Planetario de Star Wars")

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

#GET
@app.route('/UNIVERSO')
def getUNIVERSO():
    return jsonify({'UNIVERSO': UNIVERSO})

@app.route('/UNIVERSO/<string:PLANETA_name>')
def getUNIVERSOS(PLANETA_name):
    encontrado=False
    for UNIVERSO in UNIVERSO:
        if UNIVERSO['PLANETA'].title() == PLANETA_name.title():
            UNIVERSOFound=UNIVERSO
            encontrado=True
        
    
    if encontrado==True:
        return jsonify({'UNIVERSO': UNIVERSOFound})
    else:
        return jsonify({'message': 'UNIVERSO EN TU GALAXIA NO HAY'})

#CREATE
@app.route('/UNIVERSO', methods=['POST'])
def addProduct():
    new_UNIVERSO = {
        'PLANETA': request.json['PLANETA'],
        'DESCIPCION': request.json['DESCIPCION'],
        'HABITANTES': request.json['HABITANTES']
    }
    UNIVERSO.append(new_UNIVERSO)
    return jsonify({'mensaje':'EL UNIVERSO CORRECTAMENTE AGREGADO SE HA','UNIVERSO': UNIVERSO})

#UPDATE
@app.route('/UNIVERSO/<string:PLANETA_name>', methods=['PUT'])
def editUNIVERSO(PLANETA_name):
    for UNIVERSO in UNIVERSO:
        if UNIVERSO['PLANETA'] == PLANETA_name.title():
            UNIVERSOFound=UNIVERSO
   
    if (len(UNIVERSOFound) > 0):
        UNIVERSOFound[0]['PLANETA'] = request.json['PLANETA']
        UNIVERSOFound[0]['DESCIPCION'] = request.json['DESCIPCION']
        UNIVERSOFound[0]['HABITANTES'] = request.json['HABITANTES']
        return jsonify({
            'message': 'EL UNIVERSO MODIFICADO CORRECTAMENTE SE HA',
            'UNIVERSO': UNIVERSOFound[0]
        })
    return jsonify({'message': 'EL UNIVERSO DESCONOCIDO ES, DATOS SOBRE EL NO HAY, OBI WAN A INVESTIGARLO IRÁ'})

#DELETE
@app.route('/UNIVERSO/<string:PLANETA_name>', methods=['DELETE'])
def deleteUNIVERSO(PLANETA_name):
    for UNIVERSO in UNIVERSO:
        if UNIVERSO['PLANETA'] == PLANETA_name.title():
            UNIVERSOFound=UNIVERSO
    
    if len(UNIVERSOFound) > 0:
        UNIVERSO.remove(UNIVERSOFound[0])
        return jsonify({
            'message': 'EL UNIVERSO BORRADO SE HA',
            'UNIVERSO': UNIVERSO
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)