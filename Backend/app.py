from flask import Flask, jsonify, request
from flask_cors import CORS
from Controller import Controller

app = Flask(__name__)
CORS(app)
ctrl = Controller()

@app.route('/')
def ping():
    return jsonify({'message':'API IPC2-Proyecto2'})

@app.route('/reset',methods=['DELETE'])
def reset():
    return ctrl.initObjects()

@app.route('/uploadFile',methods=['POST'])
def upload():
    data = request.json
    return ctrl.upload(
        data.get('xml')
    )

@app.route('/machine',methods=['GET'])
def getMachines():
    return ctrl.getMachines()

@app.route('/machine',methods=['POST'])
def getDotM():
    data = request.json
    return ctrl.getDotM(
        data.get('dot')
    )

@app.route('/machinesC',methods=['POST'])
def getMachineC():
    data = request.json
    return ctrl.getMachinesC(data.get('compound'))

@app.route('/elements',methods=['GET'])
def getElements():
    return ctrl.getElements()

@app.route('/elements',methods=['POST'])
def newElement():
    data = request.json
    return ctrl.newElement(
        data.get('atomicNum'),
        data.get('symbol'),
        data.get('name')
    )

@app.route('/compounds',methods=['GET'])
def getCompounds():
    return ctrl.getCompounds()

@app.route('/compounds',methods=['POST'])
def getDotStep():
    data = request.json
    return ctrl.getDotStep(
        data.get('machine'),
        data.get('compound')
    )

if __name__ == '__main__':
    app.run(debug = True, port = 4000)