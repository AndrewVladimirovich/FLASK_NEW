from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetail
from combojsonapi.spec import ApiSpecPlugin

from blog.api.user import UserList, UserDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.article import ArticleList, Article

from combojsonapi.permission import PermissionPlugin
def init_api(app):
    event_plugin = EventPlugin()
    api_spec_plugin = create_api_spec_plugin(app)
    permission_plugin = PermissionPlugin(strict=False)
    api = Api(
        app,
        plugins=[
            event_plugin,
            api_spec_plugin,
            permission_plugin,
], )