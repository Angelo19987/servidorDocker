import os

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
bind_port = int(os.environ['BIND_PORT'])


@app.route('/')
def hello():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return f'¡Hola de nuevo, para pasar el ramo debes hacer {total_hits} ejercicios\n de abdominales y recargar la página, suerte!.'

@app.route('/login')
def sigin():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return f'¡Hola hola Carambolas, cuidado si no sales de aquí reprobaras {total_hits} ramos!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=bind_port)
