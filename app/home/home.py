from flask import Blueprint, render_template, redirect, url_for


home = Blueprint("Home", __name__, template_folder="templates", static_folder="static")
logedin = True

@home.route("/")
def main_page():
    print(logedin)
    if not logedin:
        return redirect(url_for('Auth.login'))
    return render_template("home.html")
