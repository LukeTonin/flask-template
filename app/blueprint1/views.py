from flask import Blueprint, render_template, request

blueprint = Blueprint("blueprint1", __name__,
                      static_folder='static',
                      static_url_path='/static/blueprint1',
                      template_folder='templates')

@blueprint.route('/blueprint1', methods=['POST'])
def blueprint1():
    render_template('blueprint1.html')