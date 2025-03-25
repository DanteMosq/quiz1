import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hola Profe! Aqui se va a contar las veces que entre {count} veces.\n por otro lado tenemos pendiente hablar. El jueves nos vemos y espero que este bien. Yo estoy al dia, Saludos'