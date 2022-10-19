import datetime

from flask import Blueprint, request

import utils

delivery_app = Blueprint('delivery_app', __name__)


@delivery_app.route('/api/delivery/create')
def api_delivery_create():
    pass
    return utils.complete_request(request, request.path)

@delivery_app.route('/api/deliveries/get')
def api_deliveries_get():
    pass
    return utils.complete_request(request, request.path)


@delivery_app.route('/api/delivery/get')
def api_delivery_get():
    pass
    return utils.complete_request(request, request.path)


@delivery_app.route('/api/delivery/edit')
def api_delivery_edit():
    pass
    return utils.complete_request(request, request.path)



@delivery_app.route('/api/delivery/remove')
def api_delivery_remove():
    pass
    return utils.complete_request(request, request.path)


@delivery_app.route('/api/delivery/get_info')
def api_delivery_get_info():
    pass
    return utils.complete_request(request, request.path)


@delivery_app.route('/api/delivery/closed')
def api_delivery_closed():
    return utils.complete_request(request, request.path)
