from flask import Blueprint

auth_bp = Blueprint("authentification", __name__, url_prefix="/auth", template_folder="templates")

from . import routes, forms