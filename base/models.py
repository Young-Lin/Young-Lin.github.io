from django.db import models
import time


class Article(models.Model):
    title = models.CharField(max_length=255, null=True, db_index=True)
    author = models.CharField(max_length=255, default="LL", null=True)
    tags = models.CharField(max_length=255, null=True)
    brief = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)

    picture_href = models.TextField(null=True)
    view_count = models.IntegerField(default=0, null=True)
    comment_count = models.IntegerField(default=0, null=True)
    create_date = models.BigIntegerField(default=time.time(), null=True)
    publish_date = models.BigIntegerField(default=time.time(), null=True)

    class Meta:
        db_table = "t_article"

class Archives(models.Model):
    year = models.CharField(max_length=255, null=True)
    month = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True, db_index=True)
    author = models.CharField(max_length=255, default="LL", null=True)
    tags = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "t_archives"