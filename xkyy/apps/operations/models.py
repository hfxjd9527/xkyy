# _*_ encoding:utf-8 _*_
from datetime import datetime
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import UserProfile
from starry.models import Article


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(UserProfile, related_name='comments', verbose_name="用户名")
    text = models.TextField(verbose_name="评论")
    root = models.ForeignKey('self', related_name='root_comment', null=True, blank=True, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='parent_comment', null=True, blank=True, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(UserProfile, related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['-comment_time']

    def __str__(self):
        return self.text


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户名")
    fav_id = models.IntegerField(default=0, verbose_name="数据id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户喜欢"
        verbose_name_plural = verbose_name
