from flask import Flask, jsonify, request
from flask_cors import CORS
from Controller import Controller

app = Flask(__name__)
CORS(app)
ctrl = Controller()

@app.route('/')
def ping():
    return jsonify({'message':'API IPC2-Proyecto2'})

@app.route('/uploadFile',methods=['POST'])
def upload():
    data = request.json
    return ctrl.upload(
        data['xml']
    )

@app.route('/machine',methods=['GET'])
def getMachines():
    return ctrl.getMachines()

@app.route('/machine',methods=['POST'])
def getDotM():
    data = request.json
    return ctrl.getDotM(
        data['dot']
    )

@app.route('/getElements',methods=['GET'])
def getElements():
    return ctrl.getElements()

@app.route('/newElement',methods=['POST'])
def newElement():
    data = request.json
    return ctrl.newElement(
        data['atomicNum'],
        data['symbol'],
        data['name']
    )

@app.route('/compounds',methods=['GET'])
def getCompounds():
    return ctrl.getCompounds()

@app.route('/compounds',methods=['POST'])
def getDotStep():
    data = request.json
    return ctrl.getDotStep(
        data['machine'],
        data['compound']
    )

if __name__ == '__main__':
    app.run(debug = True, port = 4000)