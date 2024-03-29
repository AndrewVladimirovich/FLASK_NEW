from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app
from blog.views.authors import authors_app
from blog.api import init_api


api = init_api(app)

app.register_blueprint(authors_app, url_prefix="/authors")



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")
@app.cli.command("create-admin")
def create_admin():

    from blog.models import User
    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    db.session.add(admin)
    db.session.commit()


print("created admin:", admin)

app.config["SECRET_KEY"] = "abcdefg123456"
app.register_blueprint(auth_app, url_prefix="/auth")
login_manager.init_app(app)

import os

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")

from flask_migrate import Migrate

migrate = Migrate(app, db)


from blog.security import flask_bcrypt

flask_bcrypt.init_app(app)

@app.cli.command("create-tags")
def create_tags():
"""
Run in your terminal:
➜ flask create-tags
"""
from blog.models import Tag for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")

from blog.admin import admin

admin.init_app(app)