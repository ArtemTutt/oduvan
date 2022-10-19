from flask import Blueprint, request

import utils

article_app = Blueprint('article_app', __name__)


@article_app.route('/api/article/create', methods=['POST'])
def api_article_create():
    return utils.complete_request(request, request.path)


@article_app.route('/api/articles/get')
def api_articles_get():
    return utils.complete_request(request, request.path)


@article_app.route('/api/article/get')
def api_article_get():
    return utils.complete_request(request, request.path)


@article_app.route('/api/article/edit', methods=['POST'])
def api_article_edit():
    return utils.complete_request(request, request.path)


@article_app.route('/api/article/remove')
def api_article_remove():
    return utils.complete_request(request, request.path)


@article_app.route('/api/articles/get_last')
def api_article_get_last():
    return utils.complete_request(request, request.path)