from flask import Blueprint, render_template, request, url_for
from flask_login import login_user


auth = Blueprint("Auth", __name__, template_folder="templates", static_folder="static", url_prefix="/auth")


@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/login", methods=['POST'])
def login_process():
    
    print(request.form["user_login"])
    return "Teste"


@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route("/signup", methods=['POST'])
def signup_process():

    print(request.form["user_login"])
    return "Test"


@auth.route("/company")
def company():
    return render_template("register_company.html")

@auth.route("/company", methods=['POST'])
def company_process():

    return "Test"