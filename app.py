import requests
from flask import Flask, request, json, render_template
import base64

from flask import Flask, request, abort, session, json, render_template, redirect
import utils, traceback
from maps.MapArticle import article_app
from maps.MapBasket import basket_app
from maps.MapCategory import category_app
from maps.MapDeal import deal_app
from maps.MapDelivery import delivery_app
from maps.MapFlower import flower_app
from maps.MapOrder import order_app
from maps.MapPackage import package_app
from maps.MapComments import comment_app
from maps.MapPayment import payment_app
from maps.MapPosition import position_app
from maps.MapProduct import product_app
from maps.MapPromoCode import promo_code_app
from maps.MapShop import shop_app
from maps.MapStaff import staff_app
from maps.MapUser import user_app

app = Flask(__name__)
app.secret_key = 'testing secret key'

app.register_blueprint(promo_code_app)
app.register_blueprint(category_app)
app.register_blueprint(comment_app)
app.register_blueprint(product_app)
app.register_blueprint(basket_app)
app.register_blueprint(deal_app)
app.register_blueprint(payment_app)
app.register_blueprint(shop_app)
app.register_blueprint(staff_app)
app.register_blueprint(article_app)
app.register_blueprint(flower_app)
app.register_blueprint(user_app)
app.register_blueprint(delivery_app)
app.register_blueprint(position_app)
app.register_blueprint(package_app)
app.register_blueprint(order_app)

# Index
@app.route('/')
def index():
    if utils.is_mobile(request.user_agent):
        return render_template('index.html')
    else:
        return render_template('pc_index.html')


# Catalog
@app.route('/catalog')
def catalog():
    id = request.values.get('category_id', 0, int)
    sub_category = request.values.get('sub_category', 0, int)
    page = request.values.get('page', 0, int)
    sorted_type = request.values.get('sorted_type', 0, int)
    if utils.is_mobile(request.user_agent):
        return render_template('catalog.html', id=id, page=page, sub_category=sub_category, sorted_type=sorted_type)
    else:
        return render_template('pc_catalog.html', id=id, page=page, sub_category=sub_category, sorted_type=sorted_type)


# favorites
@app.route('/favorites')
def favorites():
    if utils.is_mobile(request.user_agent):
        return render_template('favourites.html')
    else:
        return render_template('pc_favourites.html')


# product
@app.route('/product')
def product():
    id = request.values.get('id', 0, int)
    if utils.is_mobile(request.user_agent):
        return render_template('product.html', id=id)
    else:
        return render_template('pc_product.html', id=id)


# createorder
@app.route('/createorder')
def createorder():
    if 'user_id' not in session:
        return redirect('/', code=302)
    if utils.is_mobile(request.user_agent):
        return render_template('createorder.html')
    else:
        return render_template('pc_createorder.html')


# cabinet
@app.route('/cabinet')
def cabinet():
    if 'user_id' not in session:
        return redirect('/', code=302)
    if utils.is_mobile(request.user_agent):
        return render_template('cabinet.html')
    else:
        return render_template('pc_cabinet.html')


# blog main page
@app.route('/blog')
def blog():
    if utils.is_mobile(request.user_agent):
        return render_template('blog.html')
    else:
        return render_template('pc_blog.html')


# article blog
@app.route('/article')
def article():
    id = request.values.get('id', 0, int)
    if utils.is_mobile(request.user_agent):
        return render_template('article.html', id=id)
    else:
        return render_template('pc_article.html', id=id)


# delivery
@app.route('/delivery_and_payment')
def delivery_and_payment():
    if utils.is_mobile(request.user_agent):
        return render_template('delivery_and_payment.html')
    else:
        return render_template('pc_delivery_and_payment.html')


# loyaltyprogram
@app.route('/loyaltyprogram')
def loyaltyprogram():
    if utils.is_mobile(request.user_agent):
        return render_template('loyaltyprogram.html')
    else:
        return render_template('pc_loyaltyprogram.html')


# weddingfloristry
@app.route('/weddingfloristry')
def weddingfloristry():
    if utils.is_mobile(request.user_agent):
        return render_template('weddingfloristry.html')
    else:
        return render_template('pc_weddingfloristry.html')


# freshnessinstruction
@app.route('/freshnessinstruction')
def freshnessinstruction():
    if utils.is_mobile(request.user_agent):
        return render_template('freshnessinstruction.html')
    else:
        return render_template('pc_freshnessinstruction.html')


# vacancies
@app.route('/vacancies')
def vacancies():
    if utils.is_mobile(request.user_agent):
        return render_template('vacancies.html')
    else:
        return render_template('pc_vacancies.html')


# legalinformation
@app.route('/legalinformation')
def legalinformation():
    if utils.is_mobile(request.user_agent):
        return render_template('legalinformation.html')
    else:
        return render_template('pc_legalinformation.html')


# returnproduct
@app.route('/returnproduct')
def returnproduct():
    if utils.is_mobile(request.user_agent):
        return render_template('returnproduct.html')
    else:
        return render_template('pc_returnproduct.html')


@app.route('/api/get_nesting_by_id')
def get_nesting_by_id():
    return utils.complete_request(request, request.path)


@app.route('/api/get_uuid', methods=['POST'])
def get_uuid():
    return utils.complete_request_post(json.loads(request.data), request.path)


@app.route('/api/get_photo')
def get_photo():
    uuid = request.values.get('uuid')
    resp = requests.get('http://b-ws.ru:1001/get', params={'uuid': uuid})
    return utils.getAnswer(resp.text)


# @app.before_request
# def redirect_on_api():
# print(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
