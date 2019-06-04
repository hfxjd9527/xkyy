# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
from django.conf.urls import url
from .views import CategoryView, article_detail, LyricView, MessageView, DonateView
from .views import ArticleSearchView, DonateMeView
urlpatterns = [
    url(r'^list/', CategoryView.as_view(), name='cate_list'),
    url(r'^article/(?P<article_id>\d+)/', article_detail, name='article_detail'),
    # url(r'^comment/(?P<article_id>\d+)/$', CommentsView.as_view(), name='article_comment'),
    # url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
    url(r'^lyrics/', LyricView.as_view(), name='starry_lyrics'),
    url(r'^message/', MessageView.as_view(), name='starry_message'),
    url(r'^donate/', DonateView.as_view(), name='starry_donate'),
    url(r'^donate-me/', DonateMeView.as_view(), name='starry_donate_me'),
    url(r'^search/', ArticleSearchView.as_view(), name='starry_search'),
]
