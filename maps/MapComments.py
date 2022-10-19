from flask import Blueprint, request

import utils

comment_app = Blueprint('comment_app', __name__)

@comment_app.route('/api/comment/create')
def api_comment_create():
    return utils.complete_request(request, request.path)


@comment_app.route('/api/comments/get_all')
def api_comments_get():
    return utils.complete_request(request, request.path)


@comment_app.route('/api/comments/remove')
def api_comments_remove():
     return utils.complete_request(request, request.path)
