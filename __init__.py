from flask import Flask
from app.route.user_route import user_bp
from app.route.products_route import product_bp
from app.route.carts_route import carts_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(carts_bp, url_prefix="/carts")
    return app
