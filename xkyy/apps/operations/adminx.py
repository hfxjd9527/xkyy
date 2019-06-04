# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
import xadmin
from .models import Comment, UserFavorite


# Register your models here.
class CommentsAdmin(object):
    list_display = ['user', 'text', 'comment_time']


xadmin.site.register(Comment, CommentsAdmin)
