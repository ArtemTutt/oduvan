from flask import Blueprint, request, session

import utils

promo_code_app = Blueprint('promo_code_app', __name__)


@promo_code_app.route('/api/promo_code/create_promo_code')
def create_promo_code():
    return utils.complete_request(request, request.path)


@promo_code_app.route('/api/promo_code/get_promo_code')
def get_promo_code():
    pass
    return utils.complete_request(request, request.path)


@promo_code_app.route('/api/promo_code/accept_promo_code')
def accept_promo_code():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    params['basket_id'] = session['basket_id']
    response = utils.complete_request_with_parameters(params, request.path)
    print(response, params)
    return response