from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import register_blueprints
from utils.db import init_db
from utils.config import Config
from utils.sqlalchemy_db import init_sqlalchemy_db
import os
import socket


def get_available_port(preferred_port=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(('0.0.0.0', preferred_port))
            return preferred_port
        except OSError:
            pass
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('0.0.0.0', 0))
        return sock.getsockname()[1]


def create_app():
    # Get the absolute path to the frontend dist directory
    frontend_dist_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'dist')
    
    app = Flask(__name__, static_folder=frontend_dist_path, static_url_path='')
    app.config.from_object(Config)
    CORS(app)
    register_blueprints(app)

    init_db(app.config['DATABASE_PATH'])
    init_sqlalchemy_db(app.config['DATABASE_PATH'])
    
    # Serve React app for non-API routes
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react_app(path):
        if path.startswith('api/'):
            # This shouldn't happen since blueprints handle API routes
            pass
        else:
            # Serve the React app for all other routes
            return send_from_directory(frontend_dist_path, 'index.html')
    
    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5001))
    if 'PORT' not in os.environ:
        port = get_available_port(port)
    app.run(host='0.0.0.0', port=port, debug=True)
