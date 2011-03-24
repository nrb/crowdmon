from flask import (Flask, Response, request, g,
	jsonify, redirect, url_for, flash)

from crowdmon import views
from crowdmon import extensions
from crowdmon.config import DefaultConfig

DEFAULT_MODULES = (
	(views.frontend, ""),
)

__all__ = ["create_app"]

def create_app(config=None):
    app = Flask("CrowdMon")

    modules = DEFAULT_MODULES
    
    configure_app(app, config)
    configure_db(app)

    configure_modules(app, modules)

    return app

def configure_app(app, config):
    app.config.from_object(DefaultConfig())

    if config is not None:
        app.config.from_object(config)

    app.config.from_envvar("APP_CONFIG", silent=True)
    
def configure_db(app):
    """Install the DB extension into the app instance."""
    extensions.db.init_app(app)

def configure_modules(app, modules):
    """Attach the modules to the app."""
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)
