
from flask import Flask

from {{cookiecutter.project_name}} import config

def register_blueprints(app):
    pass


def register_extensions(app):
    pass


def register_errorhandlers(app):

    @app.before_request
    def check_session():
        pass

    @app.errorhandler(CSRFError)
    def csrf_error(error):
        pass

    @app.errorhandler(401)
    def unauthorized(error):
        pass

    @app.errorhandler(403)
    def access_denied(error):
        pass

    @app.errorhandler(404)
    def not_found(error):
        pass

    @app.errorhandler(501)
    def not_available(error):
        pass

    @app.errorhandler(NotImplementedError)
    def not_implemented(error):
        pass

    @app.errorhandler(503)
    def service_unavailable(error):
        pass

    @app.errorhandler(504)
    def connection_timeout(error):
        pass



def create_app():
    app = Flask(__name__)
    app.config.from_mapping(config.cwa.flask)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    with app.app_context():
        # db.create_all()
        pass

    return app