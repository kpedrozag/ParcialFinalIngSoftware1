import hashlib as hs
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def converter(string):
    sha256 = hs.sha256(string.encode()).hexdigest()
    sha384 = hs.sha384(string.encode()).hexdigest()
    sha224 = hs.sha224(string.encode()).hexdigest()
    sha512 = hs.sha512(string.encode()).hexdigest()
    sha1 = hs.sha1(string.encode()).hexdigest()
    return [('sha256', sha256), ('sha384', sha384), ('sha224', sha224), ('sha512', sha512), ('sha1', sha1)]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hash/<string>')
def hash_html5(string):
    lista = converter(string)
    lista.insert(0, ('Palabra', string))
    return render_template('hashes.html', lista=lista)


@app.route('/hash/<string>/json')
def hash_json(string):
    lista = converter(string)
    return jsonify(Palabra=string,
                   sha256=lista[0][1],
                   sha384=lista[1][1],
                   sha224=lista[2][1],
                   sha512=lista[3][1],
                   sha1=lista[4][1])


if __name__ == '__main__':
    app.run()