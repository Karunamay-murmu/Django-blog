# Generated by Django 3.0.7 on 2020-08-15 14:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(default=None, max_length=256, unique=True)),
                ('postId', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('authorId', models.CharField(default=None, editable=False, max_length=256)),
                ('tags', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('body', tinymce.models.HTMLField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(max_length=256)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('update_date', models.DateField(blank=True, null=True)),
                ('read_time', models.CharField(default='3 min', max_length=100)),
                ('meta_title', models.CharField(blank=True, max_length=60, null=True)),
                ('slug', models.SlugField(blank=True, max_length=75, null=True, unique=True)),
                ('meta_description', models.CharField(blank=True, max_length=160, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='my_blog.Categorie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('posts', models.ManyToManyField(to='my_blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('title', models.CharField(default=None, max_length=256, unique=True)),
                ('postId', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('authorId', models.CharField(default=None, editable=False, max_length=256)),
                ('tags', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('body', tinymce.models.HTMLField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='my_blog.Categorie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('comment', models.TextField()),
                ('create_date', models.DateField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.Post')),
            ],
        ),
    ]
