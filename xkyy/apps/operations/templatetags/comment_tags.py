# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
from django import template
from django.contrib.contenttypes.models import ContentType
from operations.models import Comment
from operations.forms import CommentForm
register = template.Library()


@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.id).count()


@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comment_form = CommentForm(initial={'content_type': content_type.model, 'object_id': obj.id, 'reply_comment_id': 0})
    return comment_form


@register.simple_tag
def get_comment_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.id, parent=None)
    return comments.order_by('-comment_time')

