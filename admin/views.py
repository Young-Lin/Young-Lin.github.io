from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from base.models import Article
from django.urls import reverse
from admin.paging import Pager
import time
import os

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '448263764' and password == 'linlin':
            request.session['admin_id'] = 3
            return redirect(reverse('admin_index'))
        else:
            return redirect(reverse('admin_login'))
    return render(request, 't_admin/login.html',
                  {'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                  })


def checkLogin(request):
    admin_id = request.session.get('admin_id', 0)
    if admin_id == 3:
        return True
    return False


def index(request):
    if not checkLogin(request):
        return redirect(reverse('admin_login'))
    articles = Article.objects.all()
    for article in articles:
        timestr = time.strftime('%Y-%m-%d', time.localtime(article.publish_date))
        article.date = timestr
    return render(request, 't_admin/index.html',
                  {'articles': articles,
                   'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                   'portrait': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433297986&di=13a26e2490f50c35087234f97282983b&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F63%2F05%2F06f58PICz97_1024.jpg',
                   'adminlogo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530424282713&di=c9be9da966ced152aa475aa005c36918&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0102ab569355cf6ac725af23e08e49.jpg%401280w_1l_2o_100sh.jpg'}
                  )


def table(request):
    if not checkLogin(request):
        return redirect(reverse('admin_login'))
    articles = Article.objects.all()
    for article in articles:
        timestr = time.strftime('%Y-%m-%d', time.localtime(article.publish_date))
        article.date = timestr
    return render(request, 't_admin/table.html',
                  {'articles': articles,
                   'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                   'portrait': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433297986&di=13a26e2490f50c35087234f97282983b&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F63%2F05%2F06f58PICz97_1024.jpg',
                   'adminlogo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530424282713&di=c9be9da966ced152aa475aa005c36918&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0102ab569355cf6ac725af23e08e49.jpg%401280w_1l_2o_100sh.jpg'}
                 )


def form(request):
    if not checkLogin(request):
        return redirect(reverse('admin_login'))
    return render(request, 't_admin/form.html',
                  {'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                   'portrait': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433297986&di=13a26e2490f50c35087234f97282983b&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F63%2F05%2F06f58PICz97_1024.jpg',
                   'adminlogo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530424282713&di=c9be9da966ced152aa475aa005c36918&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0102ab569355cf6ac725af23e08e49.jpg%401280w_1l_2o_100sh.jpg',
                   })


def admin_tablelist(request):
    if not checkLogin(request):
        return redirect(reverse('admin_login'))
    current_page = request.GET.get('page', 1)
    page_obj = Pager(current_page)
    articles = Article.objects.all()[page_obj.start:page_obj.end]
    for article in articles:
        timestr = time.strftime('%Y-%m-%d', time.localtime(article.publish_date))
        article.date = timestr
    current_page = request.GET.get('page', 1)
    page_obj = Pager(current_page)
    all_item = Article.objects.all().count()
    pager_str = page_obj.page_str(all_item, '/admin_tablelist/')
    return render(request, 't_admin/tablelist.html',
                  {'articles': articles, 'pager_str': pager_str,
                   'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                   'portrait': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433297986&di=13a26e2490f50c35087234f97282983b&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F63%2F05%2F06f58PICz97_1024.jpg',
                   'adminlogo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530424282713&di=c9be9da966ced152aa475aa005c36918&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0102ab569355cf6ac725af23e08e49.jpg%401280w_1l_2o_100sh.jpg',
                   })


def admin_tablelistimg(request):
    if not checkLogin(request):
        return redirect(reverse('admin_login'))
    current_page = request.GET.get('page', 1)
    page_obj = Pager(current_page)
    articles = Article.objects.all()[page_obj.start:page_obj.end]
    for article in articles:
        timestr = time.strftime('%Y-%m-%d', time.localtime(article.publish_date))
        article.date = timestr
    current_page = request.GET.get('page', 1)
    page_obj = Pager(current_page)
    all_item = Article.objects.all().count()
    pager_str = page_obj.page_str(all_item, '/admin_tablelistimg/')
    return render(request, 't_admin/tablelistimg.html',
                  {'articles': articles, 'pager_str': pager_str,
                   'logo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433642582&di=459a7e0be96186d8554a54d4504a5ae7&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F87%2F78%2F01i58PICFWN_1024.jpg',
                   'portrait': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530433297986&di=13a26e2490f50c35087234f97282983b&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F14%2F63%2F05%2F06f58PICz97_1024.jpg',
                   'adminlogo': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530424282713&di=c9be9da966ced152aa475aa005c36918&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0102ab569355cf6ac725af23e08e49.jpg%401280w_1l_2o_100sh.jpg',
                   })


def delete(request, article_id):
    Article.objects.filter(id=article_id).delete()
    return redirect(reverse('admin_tablelist'))


def save(request):
    article_id = request.GET.get('article_id')
    article = None
    if article_id is not '':
        article = Article.objects.filter(id=article_id).first()
    if article:
        pass
    else:
        article = Article()
    article_title = request.POST.get('article_title')
    if article_title:
        article.title = article_title
    article_publish_date = request.POST.get('article_publish_date')
    if article_publish_date:
        timeArray = time.strptime(article_publish_date, "%Y-%m-%d")
        article.publish_date = int(time.mktime(timeArray))
    article_author = request.POST.get('article_author')
    if article_author:
        article.author = article_author
    article_brief = request.POST.get('article_brief')
    if article_brief:
        article.brief = article_brief
    article_picture_href = request.POST.get('article_picture_href')
    if article_picture_href:
        article.picture_href = article_picture_href
    article_tags = request.POST.get('article_tags')
    if article_tags:
        article.tags = article_tags
    article_content = request.POST.get('article_content')
    if article_content:
        article.content = article_content
    article.save()
    return redirect(reverse('admin_tablelist'))


def edit(request, article_id):
    if not checkLogin(request):
        return redirect(reverse('admin_login'))
    article = Article.objects.filter(id=article_id)[0]
    if request.method == "POST":
        article_title = request.POST.get('article_title')
        article_publish_date = request.POST.get('article_publish_date')
        if article_publish_date:
            timeArray = time.strptime(article_publish_date, "%Y-%m-%d")
        article_publish_date = int(time.mktime(timeArray))
        article_author = request.POST.get('article_author')
        article_brief = request.POST.get('article_brief')
        article_picture_href = request.POST.get('article_picture_href')
        article_tags = request.POST.get('article_tags')
        article_content = request.POST.get('article_content')
        Article.objects.filter(id=article_id).update(title=article_title, publish_date=article_publish_date, author=article_author, brief=article_brief, picture_href=article_picture_href,
                                                     tags=article_tags, content=article_content)
        return redirect(reverse('admin_tablelist'))
    return render(request, 't_admin/edit.html', {'article': article})



def upload_avatar(request):
    file_obj = request.FILES.get('avatar')
    file_path = os.path.join('static/images/', file_obj.name)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return HttpResponse(file_path)