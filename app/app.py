from flask import Flask
from routes.status import status_api

app = Flask(__name__)

app.register_blueprint(status_api, url_prefix='/status')

@app.route('/')
def hello_docker():
    return 'Hello, I run in a docker container'

if __name__ == '__main__':
    app.run(host='0.0.0.0')