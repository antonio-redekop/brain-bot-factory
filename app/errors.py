from __future__ import annotations
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def _bad_request(e):
        return jsonify({"error": "BadRequest", "detail": str(e)}), 400

    @app.errorhandler(404)
    def _not_found(e):
        return jsonify({"error": "NotFound", "detail": str(e)}), 404

    @app.errorhandler(422)
    def _unprocessable(e):
        return jsonify({"error": "UnprocessableEntity", "detail": str(e)}), 422

    @app.errorhandler(500)
    def _server_error(e):
        return jsonify({"error": "InternalServerError", "detail": "unexpected server error"}), 500
