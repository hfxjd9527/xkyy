# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
from django.conf.urls import url
from .views import UserInfoView, UploadImageView, UpdatePwdView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),  # 修改用户头像
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),  # 用户个人中心修改密码
]
