# Generated by Django 2.0.1 on 2018-01-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0003_website_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='user_id',
            field=models.CharField(max_length=30, verbose_name='Telegram user id'),
        ),
        migrations.AlterField(
            model_name='website',
            name='name',
            field=models.TextField(max_length=50, verbose_name='name of the website'),
        ),
        migrations.AlterField(
            model_name='website',
            name='user_id',
            field=models.CharField(max_length=30, verbose_name='telegram user id'),
        ),
    ]
