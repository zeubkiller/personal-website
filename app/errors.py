from flask import render_template

from app import serverApp, database_instance


@serverApp.errorhandler(404)
def not_found_error_404(error):
    return render_template("404.html"), 404


@serverApp.errorhandler(500)
def internal_error(error):
    database_instance.session.rollback()
    return render_template("500.html"), 500


