# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
from django.conf.urls import url
from .views import update_comment
urlpatterns = [
    url('update_comment', update_comment, name='update_comment')
]
