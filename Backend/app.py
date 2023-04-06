from flask import Flask, jsonify, request
from flask_cors import CORS
from Controller import Controller

app = Flask(__name__)
CORS(app)
ctrl = Controller()

@app.route('/')
def ping():
    return jsonify({'message':'API Biblioteca'})

@app.route('/uploadFile',methods=['POST'])
def upload(path):
    ctrl.upload(path)

if __name__ == '__main__':
    app.run(debug = True, port = 4000)