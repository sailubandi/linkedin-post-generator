from flask import Flask
from flask import Flask, request, jsonify
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    with app.app_context():
        from .routes import bp
        app.register_blueprint(bp)

    return app
