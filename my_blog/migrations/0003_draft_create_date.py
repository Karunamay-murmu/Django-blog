# Generated by Django 3.0.7 on 2020-08-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_auto_20200816_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='create_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
