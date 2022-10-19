from flask import Blueprint, request

import utils

category_app = Blueprint('category_app', __name__)


@category_app.route('/api/category/create')
def api_category_create():
    pass
    return utils.complete_request(request, request.path)


@category_app.route('/api/categories/get')
def api_categories_get():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    response = utils.complete_request_with_parameters(params, request.path)
    return response


@category_app.route('/api/category/get')
def api_category_get():
    pass
    return utils.complete_request(request, request.path)


@category_app.route('/api/category/edit')
def api_category_edit():
    pass
    return utils.complete_request(request, request.path)


@category_app.route('/api/category/remove')
def api_category_remove():
    pass
    return utils.complete_request(request, request.path)


@category_app.route('/api/categories/get_for_main')
def api_categories_get_for_main():
    return utils.complete_request(request, request.path)


@category_app.route('/api/category/top_category_products_count')
def api_get_top_category():
    return utils.complete_request(request, request.path)