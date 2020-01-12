from flask import Flask

from load_config import Config

app = Flask(__name__)


config_defaults = {
    "products_table": "Products",
    "product_name": "Name",
    "product_description": "Description",
    "product_photos": "Photos",
    "product_status": "Status",
    "product_price": "Price",
    "orders_table": "Orders"
}

c = Config(defaults=config_defaults)


@app.route('/')
def hello_world():
    return 'Hello AiroShop!'


if __name__ == '__main__':
    app.run()
