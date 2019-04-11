import urllib.request, urllib.parse

GET_URL = "https://api.thingspeak.com/update?api_key=7QHAZ88F2JRP0ZCQ&"
TEMPERATURE = "field1"
HUMIDITY = "field2"
MOTION_COUNT = "field3"


def send(url, params):
    p = urllib.parse.urlencode(params)
    url = url + p
    with urllib.request.urlopen(url) as res:
        res.read().decode("utf-8")


def send_temperature(temperature):
    params = {
        TEMPERATURE: temperature
    }
    send(GET_URL, params)


def send_humidity(humidity):
    params = {
        HUMIDITY: humidity
    }
    send(GET_URL, params)


def send_data(temperature, humidity):
    params = {
        TEMPERATURE: temperature,
        HUMIDITY: humidity
    }
    send(GET_URL, params)


def send_motion_count(count):
    params = {
        MOTION_COUNT: count
    }
    send(GET_URL, params)
