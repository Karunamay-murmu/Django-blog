# Generated by Django 3.0.7 on 2020-10-12 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0016_auto_20201011_1906'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subsriber',
            new_name='Subscriber',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='subsriber_email',
            new_name='subscriber_email',
        ),
    ]
