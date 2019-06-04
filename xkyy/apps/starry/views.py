from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from pure_pagination import Paginator, PageNotAnInteger
from operations.models import Comment
from operations.forms import CommentForm
from .models import Category, Article


class IndexView(View):
    def get(self, request):
        all_cate = Category.objects.all()
        articles = Article.objects.filter(category_id__lt=5)
        # 为分页做准备
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(articles, 5, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'all_cate': all_cate,
            'articles': articles
        })


class CategoryView(View):
    def get(self, request):
        all_cate = Category.objects.all()
        articles = Article.objects.filter(category_id__lt=5)

        # # 文章搜索
        # search_keywords = request.GET.get('keywords', '')
        # if search_keywords:
        #     articles = articles.filter(Q(title__icontains=search_keywords) | Q(content__icontains=search_keywords))

        # 筛选出种类
        cate_id = request.GET.get('cate', '')
        if cate_id:
            articles = articles.filter(category_id=cate_id)

        # 为分页做准备
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(articles, 6, request=request)
        articles = p.page(page)
        return render(request, 'category.html', {
            'all_cate': all_cate,
            'articles': articles
        })


def article_detail(request, article_id):
    all_cate = Category.objects.all()
    article = get_object_or_404(Article, pk=article_id)
    article.click_nums += 1
    article.save()
    context = {}
    context['all_cate'] = all_cate
    context['previous_article'] = Article.objects.filter(created_date__gt=article.created_date).last()
    context['next_article'] = Article.objects.filter(created_date__lt=article.created_date).first()
    context['article'] = article
    response = render(request, 'article.html', context)  # 响应
    # response.set_cookie(read_cookie_key, 'true') # 阅读cookie标记
    return response


class LyricView(View):
    def get(self, request):
        all_cate = Category.objects.all()
        articles = Article.objects.filter(category_id=5)
        return render(request, 'lyrics.html', {
            'all_cate': all_cate,
            'articles': articles,
        })


class MessageView(View):
    def get(self, request):
        all_cate = Category.objects.all()
        category = get_object_or_404(Category, pk=4)
        # read_cookie_key = read_statistics_once_read(request, blog)
        category_content_type = ContentType.objects.get_for_model(category)
        comments = Comment.objects.filter(content_type=category_content_type, object_id=category.id, parent=None)
        comment_form = CommentForm(initial={'content_type': category_content_type.model, 'object_id': 4, 'reply_comment_id': 0})
        return render(request, 'message.html', {
            'all_cate': all_cate,
            'comments': comments,
            'comment_form': comment_form,
        })


class DonateView(View):
    def get(self, request):
        all_cate = Category.objects.all()
        return render(request, 'donate.html', {
            'all_cate': all_cate,
        })


class DonateMeView(View):
    def get(self, request):
        return render(request, 'donate-me2.html', {})


class ArticleSearchView(View):
    def get(self, request):
        all_cate = Category.objects.all()
        sq = request.GET.get('sq')
        articles = {}
        if sq:
            articles = Article.objects.filter(Q(title__icontains=sq) | Q(content__icontains=sq))
        return render(request, 'search.html', {
            'all_cate': all_cate,
            'articles': articles
        })
