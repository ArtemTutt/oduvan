import json
import os

import requests
from flask import Response

address = os.getenv('BACKEND_URL')


def is_mobile(user_agent):
    return 'mobile' in str(user_agent).lower()


def complete_request_with_data(path):
    data = {}
    url = address + path
    resp = requests.get(url, data)
    return json.loads(resp.text)


def getError(error_text):
    res = {
        'status': 'error',
        'message': error_text
    }
    return Response(
        response=json.dumps(res, ensure_ascii=False),
        mimetype='application/json',
        status=200
    )


def getAnswer(text, info=None):
    if info is None:
        info = {}
    res = {
        'status': 'ok',
        'message': text
    }
    answer = {**res, **info}
    return Response(
        response=json.dumps(answer, ensure_ascii=False),
        mimetype='application/json',
        status=200
    )


def complete_request(req, path):
    data = {}
    for item in req.args:
        data[item] = req.args.get(item)
    url = address + path
    resp = requests.get(url, data)
    return json.loads(resp.text)


def complete_request_post(data, path):
    url = address + path
    data['image'] = data['image'][data['image'].find(','):]
    resp = requests.post(url, data)
    return json.loads(resp.text)


def complete_request_with_parameters(params, path):
    url = address + path
    resp = requests.get(url, params)
    return json.loads(resp.text)


def complete_request_post_with_parameters(params, path):
    url = address + path
    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.post(url, data=json.dumps(params['info'], ensure_ascii=False), headers=headers)
    return resp.text
