from __future__ import annotations
from flask import Flask
from app.config import Config
from app.errors import register_error_handlers
from app.routes.robots import robots_bp
from app.routes.routing import routing_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # blueprints
    app.register_blueprint(robots_bp)
    app.register_blueprint(routing_bp)

    # error handlers
    register_error_handlers(app)

    @app.get("/healthz")
    def healthz():
        return {"ok": True}

    return app
