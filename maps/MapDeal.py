import datetime

from flask import Blueprint, request

import utils

deal_app = Blueprint('deal_app', __name__)


@deal_app.route('/api/deal/create')
def api_deal_create():
    pass
    return utils.complete_request(request, request.path)



@deal_app.route('/api/deals/get')
def api_deals_get():
    pass
    return utils.complete_request(request, request.path)


@deal_app.route('/api/deal/get')
def api_deal_get():
    pass
    return utils.complete_request(request, request.path)


@deal_app.route('/api/deal/edit')
def api_deal_edit():
    pass
    return utils.complete_request(request, request.path)


@deal_app.route('/api/deal/remove')
def api_deal_remove():
    pass
    return utils.complete_request(request, request.path)


@deal_app.route('/api/deal_closed')
def api_deal_closed():
    pass
    return utils.complete_request(request, request.path)


