# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from base.models import Article
from base.models import Archives
from admin.paging import Pager
import mistune
import time


def index(request):
    current_page = request.GET.get('page', 1)
    page_obj = Pager(current_page)
    articles = Article.objects.all()[page_obj.start:page_obj.end]
    for article in articles:
        timestr = time.strftime('%Y-%m-%d', time.localtime(article.publish_date))
        article.date = timestr
        current_page = request.GET.get('page', 1)
        page_obj = Pager(current_page)
        all_item = Article.objects.all().count()
        pager_str = page_obj.page_str(all_item, '/index/')
    return render(request, 't_blog/index.html',
                  {'articles': articles, 'pager_str': pager_str,
                   'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                   })


def archive(request):
    archives = Archives.objects.all()
    return render(request, 't_blog/archives.html',
                  {'archives': archives,
                   'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg'
                   })


def article(request, article_id):
    article = Article.objects.filter(id=article_id)[0]
    timestr = time.strftime('%Y-%m-%d', time.localtime(article.publish_date))
    article.date = timestr
    markdown = mistune.Markdown()
    article.content = markdown(article.content)
    return render(request, 't_blog/article.html',
                  {'article': article,
                   'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                   })


def data_fresh(request):
    context = {"data1": Article.objects.order_by("-time")[0].title,
               "data2": Article.objects.order_by("-time")[0].title}
    return JsonResponse(context)


def a(request):
    return render(request, 't_blog/a.html')


def getdata(request):
    article = Article.objects.first()
    return JsonResponse({'article': article})