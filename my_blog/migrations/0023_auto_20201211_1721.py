# Generated by Django 3.0.7 on 2020-12-11 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0022_post_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='liked',
        ),
    ]