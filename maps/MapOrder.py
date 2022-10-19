from flask import Blueprint, request

import utils

order_app = Blueprint('order_app', __name__)


@order_app.route('/api/order/create')
def api_order_create():
    return utils.complete_request(request, request.path)


@order_app.route('/api/orders/get')
def api_orders_get():
    return utils.complete_request(request, request.path)


@order_app.route('/api/order/get')
def api_order_get():
    return utils.complete_request(request, request.path)


@order_app.route('/api/order/remove')
def api_order_remove():
    return utils.complete_request(request, request.path)


@order_app.route('/api/orders/close')
def api_orders_close():
    return utils.complete_request(request, request.path)


@order_app.route('/api/orders/get_opened')
def api_orders_get_opened():
    return utils.complete_request(request, request.path)