from flask import Blueprint, request, session

import utils

busket_app = Blueprint('busket_app', __name__)


@busket_app.route('/api/busket/create')
def api_busket_create():
    resp = utils.complete_request(request, request.path)
    if 'busket_id' not in session:
        session['busket_id'] = resp['busket']['id']
    return resp


@busket_app.route('/api/buskets/get')
def api_buskets_get():
    return utils.complete_request(request, request.path)


@busket_app.route('/api/busket/edit')
def api_busket_edit():
    return utils.complete_request(request, request.path)


@busket_app.route('/api/busket/add_product')
def api_busket_add_product():
    return utils.complete_request(request, request.path)


@busket_app.route('/api/busket/remove_product_key')
def api_busket_remove_product_key():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'busket_id' not in params.keys():
        if 'busket_id' in session:
            params = {'busket_id': session['busket_id']}
        else:
            return 'error'
    resp = utils.complete_request(params, request.path)
    if 'busket_id' not in session:
        session['busket_id'] = resp['busket']['id']
    return resp


@busket_app.route('/api/busket/remove_product_count')
def api_busket_remove_product_count():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'busket_id' not in params.keys():
        if 'busket_id' in session:
            params = {'busket_id': session['busket_id']}
        else:
            return 'error'
    resp = utils.complete_request(params, request.path)
    if 'busket_id' not in session:
        session['busket_id'] = resp['busket']['id']
    return resp


@busket_app.route('/api/busket/clear')
def api_busket_clear():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'busket_id' not in params.keys():
        if 'busket_id' in session:
            params = {'busket_id': session['busket_id']}
        else:
            return 'error'
    resp = utils.complete_request(params, request.path)
    if 'busket_id' not in session:
        session['busket_id'] = resp['busket']['id']
    return resp


@busket_app.route('/api/busket/remove')
def api_busket_remove():
    return utils.complete_request(request, request.path)


@busket_app.route('/api/busket/get_by_busket_id')
def api_busket_get_by_busket_id():
    return utils.complete_request(request, request.path)



@busket_app.route('/api/busket/get_by_user')
def api_busket_get_by_user():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'busket_id' not in params.keys():
        if 'busket_id' in session:
            params = {'busket_id': session['busket_id']}
        else:
            return 'error'
    resp = utils.complete_request(params, request.path)
    if 'busket_id' not in session:
        session['busket_id'] = resp['busket']['id']
    return resp


@busket_app.route('/api/busket/choice_purchase_type')
def api_busket_choice_purchase_type():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'busket_id' not in params.keys():
        if 'busket_id' in session:
            params = {'busket_id': session['busket_id']}
        else:
            return 'error'
    resp = utils.complete_request(params, request.path)
    if 'busket_id' not in session:
        session['busket_id'] = resp['busket']['id']
    return resp