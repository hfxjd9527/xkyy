from django.db import models
from DjangoUeditor.models import UEditorField


class BigCategory(models.Model):
    name = models.CharField(verbose_name='大分类', max_length=20)
    desc = models.TextField(verbose_name='分类描述', max_length=100)

    class Meta:
        verbose_name = '大分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    bigcategory = models.ForeignKey(BigCategory, verbose_name='父级分类')
    name = models.CharField(verbose_name='分类', max_length=20)
    desc = models.TextField(verbose_name='分类描述', max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name='分类')
    title = models.CharField(verbose_name='标题', max_length=50)
    summary = models.CharField(verbose_name='摘要', max_length=50, default='', null=True, blank=True)
    author = models.CharField(verbose_name='作者', max_length=20)
    content = UEditorField(verbose_name='内容', width=600, height=300, toolbars="full", imagePath="org/ueditor/",
                          filePath="org/ueditor/", default='')
    article_tail = models.CharField(verbose_name='一句话概述', max_length=50, default='', null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to="org/%Y/%m", verbose_name="文章配图")
    click_nums = models.IntegerField(verbose_name='阅读量', default=0)
    fav_nums = models.IntegerField(verbose_name='喜爱量', default=0)
    created_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_date']

    def __str__(self):
        return self.title

