"""The app module, containing the app factory function."""
import os
from os.path import join

from flask import Flask
from flask_caching import Cache
cache = Cache()

from app.utils import read_json
from app import blueprint1, blueprint2, ROOT_DIR


def create_app():
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    """
    app = Flask(__name__.split('.')[0])

    # Use default settings then overide with settings file
    # contained in environment variable SETTINGS
    app.config.from_json(join(ROOT_DIR, 'default_config.json'))

    if 'SETTINGS' in os.environ:
        app.config.from_json(os.environ['SETTINGS'])

    cache.init_app(app, config=app.config['CACHE'])

    register_blueprints(app)
    return app

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(blueprint1.views.blueprint)
    app.register_blueprint(blueprint2.views.blueprint)
