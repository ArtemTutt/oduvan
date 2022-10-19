import json

from flask import Blueprint, request

import utils

flower_app = Blueprint('flower_app', __name__)


@flower_app.route('/api/flower/create')
def api_flower_create():
    return utils.complete_request(request, request.path)


@flower_app.route('/api/flowers/get')
def api_flowers_get():
    pass
    return utils.complete_request(request, request.path)


@flower_app.route('/api/flower/get')
def api_flower_get():
    pass
    return utils.complete_request(request, request.path)


@flower_app.route('/api/flower/edit')
def api_flower_edit():
    pass
    return utils.complete_request(request, request.path)


@flower_app.route('/api/flower/remove')
def api_flower_remove():
    return utils.complete_request(request, request.path)
