# Generated by Django 2.2.2 on 2019-07-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
