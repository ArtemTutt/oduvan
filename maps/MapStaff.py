from flask import Blueprint, request

import utils

staff_app = Blueprint('staff_app', __name__)


@staff_app.route('/api/staff/create')
def api_staff_create():
    return utils.complete_request(request, request.path)


@staff_app.route('/api/staffs/get')
def api_staffs_get():
    return utils.complete_request(request, request.path)

@staff_app.route('/api/staff/get')
def api_staff_get():
    return utils.complete_request(request, request.path)


@staff_app.route('/api/staff/edit')
def api_staff_edit():
    return utils.complete_request(request, request.path)


@staff_app.route('/api/staff/remove')
def api_staff_remove():
    return utils.complete_request(request, request.path)


# Endpoints для регистрации/авторизации сотрудников
@staff_app.route('/api/staff/registration')
def api_staff_registration():
    return utils.complete_request(request, request.path)


@staff_app.route('/api/staff/auth')
def api_staff_auth():
    return utils.complete_request(request, request.path)
