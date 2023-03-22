from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from blog.models import User

auth_app = Blueprint("auth_app", __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))
__all__ = [
    "login_manager",
    "auth_app",
]

@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="username not passed")
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login.html", error=f"no user {username!r}
found")
    login_user(user)
    return redirect(url_for("index"))

@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
   logout_user()
   return redirect(url_for("index"))
@auth_app.route("/secret/")
@login_required
def secret_view():
   return "Super secret data"

from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from blog.models.database import db
from blog.models import User
from blog.forms.user import RegistrationForm

from werkzeug.exceptions import NotFound

def login():
    return "WIP"
    # if request.method == "GET":
    #     return render_template("auth/login.html")
    #
    #
    # login_user(user)
    # return redirect(url_for("index"))
@auth_app.route("/login-as/", methods=["GET", "POST"], endpoint="login-as")
def login_as():
if not (current_user.is_authenticated and current_user.is_staff): # non-admin users should not know about this feature
raise NotFound


from blog.forms.user import LoginForm

def login():
    if current_user.is_authenticated:
        return redirect("index")
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            return render_template("auth/login.html", form=form, error="username doesn't exist")
        if not user.validate_password(form.password.data):
            return render_template("auth/login.html", form=form, error="invalid username or password")
        login_user(user)
        return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)