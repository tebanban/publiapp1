"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Valla
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200


@api.route("/valla/<int:id>", methods=["GET"])   # Datos de cada sitio
def get_valla(id):

    valla = Valla.query.filter_by(id=id).all()
    valla = list(map(lambda x: x.serialize(), valla))

    return jsonify(valla), 200


