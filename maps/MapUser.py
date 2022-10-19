import json

from flask import Blueprint, request, session, abort

import utils

user_app = Blueprint('user_app', __name__)


@user_app.route('/api/user/create')
def api_user_create():
    return utils.complete_request(request, request.path)


@user_app.route('/api/users/get')
def api_users_get():
    return utils.complete_request(request, request.path)


@user_app.route('/api/user/get')
def api_user_get():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'user_id' not in params.keys():
        if 'user_id' in session:
            params = {'user_id': session['user_id']}
        else:
            return 'error'
    res = utils.complete_request_with_parameters(params, request.path)
    if 'liked' in session:
        res['message']['user']['liked'] = session['liked']
    return res


@user_app.route('/api/user/remove')
def api_user_remove():
    return utils.complete_request(request, request.path)


@user_app.route('/api/user/check')
def api_user_check():
    return utils.complete_request(request, request.path)


@user_app.route('/api/user/registration')
def api_user_registration():
    resp = utils.complete_request(request, request.path)
    return resp


@user_app.route('/api/user/auth')
def api_user_auth():
    resp = utils.complete_request(request, request.path)
    if 'user_id' not in session:
        if 'user' in resp:
            session['user_id'] = resp['user']
    return resp


@user_app.route('/api/user/liked')
def api_user_liked():
    product_id = request.values.get('product_id')
    # session.pop('liked', None)
    if 'liked' not in session:
        session['liked'] = list(product_id)
    else:
        l = list(session.get('liked'))
        if product_id not in l:
            l.append(product_id)
        session['liked'] = l
    return utils.getAnswer('ok')


@user_app.route('/api/user/list_likes')
def api_user_list_likes():
    if 'liked' in session:
        resp = utils.complete_request_with_parameters({'liked': json.dumps(session['liked'])}, request.path)
        return resp
    else:
        return utils.getError('error')


@user_app.route('/api/user/disliked')
def api_user_disliked():
    product_id = request.values.get('product_id')
    l = list(session.get('liked'))
    if product_id in l:
        l.remove(product_id)
    session['liked'] = l
    return utils.getAnswer('ok')


@user_app.route('/api/user/add_address')
def api_user_add_address():
    return utils.complete_request(request, request.path)


@user_app.route('/api/user/check_password')
def api_user_check_password():
    return utils.complete_request(request, request.path)


@user_app.route('/api/user/add_avatar', methods=['POST'])
def api_user_add_new_avatar():
    return utils.complete_request_post(json.loads(request.data), request.path)


@user_app.route('/api/user/remove_avatar')
def api_user_remove_avatar():
    return utils.complete_request(request, request.path)


@user_app.route('/api/user/change_address')
def api_user_change_address():
    return utils.complete_request(request, request.path)


@user_app.route('/api/user/change_info')
def api_user_change_info():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'user_id' not in params.keys():
        if 'user_id' in session:
            params['user_id'] = session['user_id']
        else:
            return 'error'
    response = utils.complete_request_with_parameters(params, request.path)
    return response


@user_app.route('/api/user/change_password')
def api_user_change_password():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    if 'user_id' not in params.keys():
        if 'user_id' in session:
            params['user_id'] = session['user_id']
        else:
            return 'error'
    response = utils.complete_request_with_parameters(params, request.path)
    return response


@user_app.route('/api/user/remove_address')
def api_user_remove_address():
    return utils.complete_request(request, request.path)


@user_app.route('/api/history_deals/get_all')
def get_all_deals_for_user():
    params = {}
    for item in request.args:
        params[item] = request.args.get(item)
    params['id'] = session['user_id']
    response = utils.complete_request_with_parameters(params, request.path)
    return response


@user_app.route('/api/user/confirmed')
def api_user_confirmed():
    resp = utils.complete_request(request, request.path)
    if 'user_id' not in session:
        if 'user_id' in resp:
            session['user_id'] = resp['user_id']
    return resp


@user_app.route('/logout')
def logout():
    if 'user_id' in session:
        session.modified = True
        for key in list(session.keys()):
            session.pop(key)
        session.modified = True
        return utils.getAnswer('')