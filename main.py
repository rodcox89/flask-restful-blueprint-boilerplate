from flask import Flask
from version_1.v1 import v1
from flask.ext.cors import CORS

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
app.register_blueprint(v1, url_prefix='/v1')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)
