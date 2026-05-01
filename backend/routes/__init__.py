from .predict import predict_bp
from .ocr import ocr_bp
from .insights import insights_bp
from .chat import chat_bp
from .health import health_bp


def register_blueprints(app):
    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(predict_bp, url_prefix='/api')
    app.register_blueprint(ocr_bp, url_prefix='/api')
    app.register_blueprint(insights_bp, url_prefix='/api')
    app.register_blueprint(chat_bp, url_prefix='/api')
