# Generated by Django 5.0.3 on 2024-03-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_productmodel_newsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='news_description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]