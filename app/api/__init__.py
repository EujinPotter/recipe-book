from flask import Blueprint, jsonify
from .aspects import api as aspects_api

api = Blueprint('api', __name__)
api.register_blueprint(aspects_api, url_prefix='/aspects')


@api.route('/test', methods=['GET'])
def api_test():
    return jsonify({'message': 'The api router is working'})
