# Generated by Django 5.0.6 on 2024-07-10 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0004_newsmodel_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
