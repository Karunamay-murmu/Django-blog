# Generated by Django 3.0.7 on 2020-08-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_draft_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='meta_description',
            field=models.TextField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='draft',
            name='meta_title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='draft',
            name='slug',
            field=models.SlugField(blank=True, max_length=75, null=True, unique=True),
        ),
    ]
