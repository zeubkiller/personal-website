from flask import render_template

from app import serverApp
from app.error import error_bp


@error_bp.errorhandler(404)
def not_found_error_404(error):
    return render_template("404.html"), 404


@error_bp.errorhandler(500)
def internal_error(error):
    serverApp.database_instance.session.rollback()
    return render_template("500.html"), 500


