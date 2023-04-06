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
        data['path']
    )

@app.route('/dotMachine',methods=['POST'])
def getDotM():
    data = request.json
    return ctrl.getDotM(
        data['dot']
    )

if __name__ == '__main__':
    app.run(debug = True, port = 4000)