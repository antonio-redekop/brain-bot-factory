from __future__ import annotations
from app.api import create_app

# dev entrypoint: python -m app.main
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
