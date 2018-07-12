"""l_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
from django.contrib import admin

from blog import views as blog_views
from admin import views as admin_views
from django.conf.urls import url


urlpatterns = [url(r'^index/$', blog_views.index, name='index'),
               url(r'^archive/$', blog_views.archive, name='archives'),
               url(r'^a/$', blog_views.a, name='a'),
               url(r'^getdata/$', blog_views.getdata, name='getdata'),
               url(r'^article/(\d+)/$', blog_views.article, name='article'),
               url('data_fresh/$', blog_views.data_fresh, name="data_fresh"),

               url(r'^admin/login$', admin_views.login, name='admin_login'),
               url(r'^admin/index$', admin_views.index, name='admin_index'),
               url(r'^admin/table$', admin_views.table, name='admin_table'),
               url(r'^admin/form$', admin_views.form, name='admin_form'),
               url(r'^admin/save$', admin_views.save, name='admin_save'),
               url(r'^admin_tablelist/$', admin_views.admin_tablelist, name='admin_tablelist'),
               url(r'^admin_tablelistimg$', admin_views.admin_tablelistimg, name='admin_tablelistimg'),
               url(r'^admin/delete/(\d+)/$', admin_views.delete, name='admin_delete'),
               url(r'^admin/edit/(\d+)/$', admin_views.edit, name='admin_edit'),
               url(r'^upload_avatar/$', admin_views.upload_avatar, name='upload_avatar'),
               # url(r'^user_list/$', admin_views.user_list, name='user_list'),

               ]