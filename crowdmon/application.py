from flask import (Flask, Response, request, g,
	jsonify, redirect, url_for, flash)

from crowdmon import views

DEFAULT_MODULES = (
	(views.frontend, ""),
)

__all__ = ["create_app"]

def create_app():
    app = Flask("CrowdMon")

    modules = DEFAULT_MODULES

    configure_modules(app, modules)

    return app
    

def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)
