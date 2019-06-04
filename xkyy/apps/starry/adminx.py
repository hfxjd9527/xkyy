import xadmin
from .models import BigCategory, Category, Article


class BigCategoryAdmin(object):
    list_display = ['name', 'desc']


class CategoryAdmin(object):
    list_display = ['name', 'desc']


class ArticleAdmin(object):
    list_display = ['category', 'title', 'author', 'content', 'created_date']
    style_fields = {"content": 'ueditor'}


xadmin.site.register(BigCategory, BigCategoryAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
