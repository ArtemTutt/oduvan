from flask import Blueprint, request

import utils

package_app = Blueprint('package_app', __name__)


@package_app.route('/api/packages/get')
def api_packages_get():
    return utils.complete_request(request, request.path)


