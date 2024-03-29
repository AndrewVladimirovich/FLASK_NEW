from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from blog.models.database import db
from blog.models import Author, Article
from blog.forms.article import CreateArticleForm

articles_app = Blueprint("articles_app", __name__)

@articles_app.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
article = Article.query.filter_by(id=article_id).options( joinedload(Article.tags) # подгружаем связанные теги!
    ).one_or_none()
    if article is None:
        raise NotFound
    return render_template("articles/details.html", article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required

def create_article():
...
# добавляем доступные теги в форму
form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")] ...
if request.method == "POST" and form.validate_on_submit(): # при создании
статьи
if form.tags.data: # если в форму были переданы теги (были выбраны)
...
selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
for tag in selected_tags:
article.tags.append(tag) # добавляем выбранные теги к статье