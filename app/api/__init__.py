from flask.blueprints import Blueprint


api_blueprint = Blueprint('api', __name__)

from . import views
