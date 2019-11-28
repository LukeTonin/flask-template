from flask import Blueprint, render_template, request

from app.app import cache

blueprint = Blueprint("blueprint2", __name__,
                      static_folder='static',
                      static_url_path='/static/blueprint2',
                      template_folder='templates')


@cache.memoize(3600)
def func(parameter):
    """Memoization example."""
    pass


# URL is relative to base url since url_prefix is not set in register_blueprint.
@blueprint.route('/', methods=['GET', 'POST'])
def index():
        return render_template("blueprint2.html")
