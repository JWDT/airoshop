from flask import Flask

app = Flask(__name__)


config_defaults = {

}


@app.route('/')
def hello_world():
    return 'Hello AiroShop!'


if __name__ == '__main__':
    app.run()
