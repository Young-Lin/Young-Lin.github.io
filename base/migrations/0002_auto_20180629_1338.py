# Generated by Django 2.0.6 on 2018-06-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture_href',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.BigIntegerField(default=1530250708.870302, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.BigIntegerField(default=1530250708.870302, null=True),
        ),
    ]
