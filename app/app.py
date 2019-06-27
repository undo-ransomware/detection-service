from flask import Flask
from routes.info_api import info_api

app = Flask(__name__)

app.register_blueprint(info_api, url_prefix='/info')

@app.route('/')
def hello_docker():
    return 'Hello, I run in a docker container'

if __name__ == '__main__':
    app.run(host='0.0.0.0')