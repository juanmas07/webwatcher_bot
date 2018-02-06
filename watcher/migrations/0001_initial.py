# Generated by Django 2.0.1 on 2018-01-21 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(verbose_name='Telegram user id')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(verbose_name='telegram user id')),
                ('last_seen', models.DateTimeField(verbose_name='last time checked')),
                ('last_status', models.IntegerField(verbose_name='last status checked')),
                ('url', models.TextField()),
                ('active', models.IntegerField(default=1)),
                ('telegram_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watcher.TelegramUser')),
            ],
        ),
    ]