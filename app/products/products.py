from flask import Blueprint, render_template, request
from flask_login import login_user

from app.products.queries import search


products = Blueprint("Products", __name__, template_folder="templates", static_folder="static", url_prefix="/products")


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

@products.route("/")
def product_home():
    product_list = search()
    products = []
    for pair in pairwise(product_list):
        products.append(pair)
    if len(product_list) % 2 != 0:
        products.append((product_list[len(product_list) - 1], ))
    print(products[0][0])
    return render_template("products.html", products = products)

@products.route("/s", methods=["GET"])
def product_search():
    product_list = search(request.args.get('text'))
    products = []
    for pair in pairwise(product_list):
        products.append(pair)
    if len(product_list) % 2 != 0:
        products.append((product_list[len(product_list) - 1], ))
    return render_template("products.html", products = products)