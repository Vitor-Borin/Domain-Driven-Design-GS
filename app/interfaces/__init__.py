from flask import Flask
from app.interfaces.api.resources import api_bp
from app.interfaces.web.views import web_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(web_bp)
    return app
