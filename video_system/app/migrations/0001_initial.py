# Generated by Django 3.1.1 on 2021-06-10 19:38

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('channel_art', models.ImageField(default='default_art.jpg', upload_to='channel/')),
                ('channel_icon', models.ImageField(default='default_icon.png', upload_to='profile/')),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('subcribers', models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoFiles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to=app.models.channel_directory_path)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.channel')),
                ('dislikes', models.ManyToManyField(related_name='video_disliked', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='video_loved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=50)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_count', to='app.videofiles')),
            ],
        ),
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('visibility', models.BooleanField(choices=[(False, 'private'), (True, 'public')])),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('videofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.videofiles')),
            ],
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.videofiles')),
            ],
        ),
    ]