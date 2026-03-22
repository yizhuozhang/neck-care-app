from __future__ import annotations

from pathlib import Path

from flask import Flask, send_from_directory


def create_app() -> Flask:
    """
    Create a Flask WSGI app that serves the existing static website files.
    """
    project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        static_folder=str(project_root),
        static_url_path="",
    )

    @app.get("/")
    def home():
        return send_from_directory(project_root, "index.html")

    @app.get("/pacman")
    def pacman():
        return send_from_directory(project_root, "pacman.html")

    @app.get("/pacman-test")
    def pacman_test():
        return send_from_directory(project_root, "pacman-test.html")

    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    return app
