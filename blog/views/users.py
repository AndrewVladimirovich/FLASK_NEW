from flask import Blueprint, render_template
users_app = Blueprint("users_app", __name__, url_prefix='/users', static_folder='../static')
USERS = {
    1: "Alex",
    2: "Max",
    3: "Douggy",
}
@users_app.route("/")
def users_list():
    return render_template("users/list.html", users=USERS)