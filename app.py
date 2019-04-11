from flask import Flask, jsonify
from lib import dht

app = Flask(__name__)
dht = dht.Dht()
dht.update()


@app.route('/')
def hello_world():
    return 'Temperature&Humidity API in Raspberry Pi'


@app.route('/api/temperature', methods=['GET'])
def temperature():
    dht.update()
    return jsonify(dht.temperature)


@app.route('/api/humidity', methods=['GET'])
def humidity():
    dht.update()
    return jsonify(dht.humidity)


if __name__ == '__main__':
    app.run()
