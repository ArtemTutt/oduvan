import json

from flask import Blueprint, request, session

import utils

product_app = Blueprint('product_app', __name__)


@product_app.route('/api/product/create')
def api_product_create():
    pass
    return utils.complete_request(request, request.path)


@product_app.route('/api/products/get')
def api_products_get():
    pass
    return utils.complete_request(request, request.path)


@product_app.route('/api/products/sort_from_min_to_max')
def api_products_sort_from_min_to_max():
    pass
    return utils.complete_request(request, request.path)


@product_app.route('/api/products/sort_from_max_to_min')
def api_products_sort_from_max_to_min():
    pass
    return utils.complete_request(request, request.path)


@product_app.route('/api/product/get')
def api_product_get():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    params['basket_id'] = session['basket_id']
    response = utils.complete_request_with_parameters(params, request.path)
    return response


@product_app.route('/api/product/edit')
def api_product_edit():
    pass
    return utils.complete_request(request, request.path)


@product_app.route('/api/product/add_discount_type')
def api_add_discount_type():
    pass
    return utils.complete_request(request, request.path)


@product_app.route('/api/product/remove_discount_type')
def api_remove_discount_type():
    pass
    return utils.complete_request(request, request.path)


@product_app.route('/api/product/remove')
def api_product_remove():
    return utils.complete_request(request, request.path)


@product_app.route('/site/products/smart', methods=['POST'])
def site_products_smart():
    params = json.loads(request.data)
    if 'user_id' in session:
        params['user_id'] = session['user_id']
    else:
        params['user_id'] = 0
    if 'basket_id' in session:
        params['basket_id'] = session['basket_id']
    else:
        params['basket_id'] = 0
    resp = utils.complete_request_post_with_parameters({'info': params}, request.path)
    return resp


@product_app.route('/site/likeds/products')
def site_likeds_products():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    params['user_id'] = session['user_id']
    params['basket_id'] = session['basket_id']
    response = utils.complete_request_with_parameters(params, request.path)
    return response


@product_app.route('/api/products/add_image', methods=['POST'])
def api_product_add_new_image():
    return utils.complete_request_post(json.loads(request.data), request.path)


@product_app.route('/api/products/remove_image')
def api_product_remove_image():
    return utils.complete_request(request, request.path)


@product_app.route('/api/products/edit_image', methods=['POST'])
def api_user_edit_image():
    return utils.complete_request_post(json.loads(request.data), request.path)


@product_app.route('/api/max_price_for_category')
def api_max_price_for_category():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    response = utils.complete_request_with_parameters(params, request.path)
    return response


@product_app.route('/api/min_price_for_category')
def api_min_price_for_category():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    response = utils.complete_request_with_parameters(params, request.path)
    return response
