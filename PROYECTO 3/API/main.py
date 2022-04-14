from flask import Flask, request
from manage import Manager
from flask.json import jsonify
app=Flask(__name__)


manager=Manager()

@app.route('/')
def index():
    return "API :)"

@app.route('/addsent_positivo', methods=['POST','GET'])
def add_senti_positivo():
    return jsonify ({'msg':'prueba'}),200

if __name__=="__main__":
    app.run(host='localhost',debug=True, port=8000)