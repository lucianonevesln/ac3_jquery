import os
from flask import Flask, render_template, json, request, jsonify


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/teste')
def index():
    return render_template('testejson.html')


@app.route('/teste2')
def index2():
    return render_template('testejson2.html')


@app.route('/teste3')
def index3():
    return render_template('testejson3.html')


@app.route('/teste4')
def index4():
    return render_template('testejson4.html')


@app.route('/teste5')
def index5():
    return render_template('testejson5.html')


@app.route('/api/say_name', methods=['GET'])
def say_name0():
    return render_template('testejson.html')


@app.route('/api/say_name', methods=['POST'])
def say_name():
    json = request.get_json()
    nomeCompleto = json['nomeCompleto']
    idEmail = json['idEmail']
    return jsonify(nomeCompleto=nomeCompleto, idEmail=idEmail)


@app.route('/api/say_name2', methods=['GET'])
def say_name_2():
    return render_template('testejson2.html')


@app.route('/api/say_name2', methods=['POST'])
def say_name2():
    nomeCompleto = request.form['nomeCompleto']
    idEmail = request.form['idEmail']
    print(nomeCompleto)
    print(idEmail)
    return jsonify(nomeCompleto=nomeCompleto)


@app.route('/api/say_name3', methods=['GET'])
def say_name_3():
    return render_template('testejson3.html')


@app.route('/api/say_name3', methods=['POST'])
def say_name3():
    nomeCompleto = request.form['nomeCompleto']
    print(nomeCompleto)
    return jsonify(nomeCompleto=nomeCompleto)


@app.route('/api/say_name4', methods=['GET'])
def say_name_4():
    return render_template('testejson4.html')


@app.route('/api/say_name4', methods=['POST'])
def say_name4():
    json = request.get_json()
    first_name = json['first']
    last_name = json['last']
    return jsonify(first_name=first_name, last_name=last_name)


@app.route('/api/say_name5', methods=['GET'])
def say_name_5():
    return render_template('testejson5.html')


@app.route('/api/say_name5', methods=['POST'])
def say_name5():

    json = request.get_json()
    first_name = json['first']
    last_name = json['last']
    valor = json['combo']
    return jsonify(first_name=valor)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=port)