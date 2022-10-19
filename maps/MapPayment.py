from flask import Blueprint, request

import utils

payment_app = Blueprint('payment_app', __name__)


@payment_app.route('/api/payment/create')
def api_payment_create():
    return utils.complete_request(request, request.path)

