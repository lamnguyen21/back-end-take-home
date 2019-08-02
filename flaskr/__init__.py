from flask import Flask, abort
from .routes_loader import RoutesLoader
from .airports_loader import AirportsLoader
from .models import Routes
from .routes_finder import RoutesFinder
from .errors import InvalidOriginError
from .errors import InvalidDestinationError

def create_app(test_config):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_pyfile(app.instance_path + "/config.py")
    else:
        app.config.update(test_config)

    routes = RoutesLoader().load(app.config['ROUTES'])
    airports = AirportsLoader().load(app.config['AIRPORTS'])
    finder = RoutesFinder(routes, airports)

    @app.route('/routes/<string:start>/to/<string:end>')
    def find_route(start, end):
        ans = finder.find(start, end)
        if ans:
            return {
                'route': ans
            }
        return {
            'error': 'route not found'
        }, 404

    @app.errorhandler(InvalidOriginError)
    def handle_invalid_origin(error):
        return {'error': error.error_message()}, 400

    @app.errorhandler(InvalidDestinationError)
    def handle_invalid_destination(error):
        return {'error': error.error_message()}, 400

    @app.errorhandler(404)
    def handle_url_not_found(error):
        return {'error': 'url not found'}, 404

    @app.errorhandler(Exception)
    def handle_general_error(error):
        return {'error': 'server is unable to process your request.'}, 500
    return app
