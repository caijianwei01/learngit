# Generated by Django 2.1.2 on 2018-11-10 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('comment_text', models.CharField(max_length=500, verbose_name='内容')),
                ('comment_user', models.CharField(max_length=20, verbose_name='用户')),
                ('comment_date', models.CharField(max_length=30, verbose_name='日期')),
            ],
            options={
                'verbose_name': '歌曲点评',
                'verbose_name_plural': '歌曲点评',
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('dynamic_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('dynamic_play', models.IntegerField(verbose_name='播放次数')),
                ('dynamic_search', models.IntegerField(verbose_name='搜索次数')),
                ('dynamic_down', models.IntegerField(verbose_name='下载次数')),
            ],
            options={
                'verbose_name': '歌曲动态',
                'verbose_name_plural': '歌曲动态',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('label_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('label_name', models.CharField(max_length=10, verbose_name='分类标签')),
            ],
            options={
                'verbose_name': '歌曲信息',
                'verbose_name_plural': '歌曲信息',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('song_name', models.CharField(max_length=30, verbose_name='歌名')),
                ('song_singer', models.CharField(max_length=30, verbose_name='歌手')),
                ('song_time', models.CharField(max_length=10, verbose_name='时长')),
                ('song_album', models.CharField(max_length=30, verbose_name='专辑')),
                ('song_languages', models.CharField(max_length=20, verbose_name='语种')),
                ('song_type', models.CharField(max_length=20, verbose_name='类型')),
                ('song_release', models.CharField(max_length=20, verbose_name='发行时间')),
                ('song_img', models.CharField(max_length=50, verbose_name='歌曲图片')),
                ('song_lyrics', models.CharField(default='暂无歌词', max_length=50, verbose_name='歌词')),
                ('song_file', models.CharField(max_length=50, verbose_name='歌曲文件')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Label', verbose_name='歌曲分类')),
            ],
            options={
                'verbose_name': '歌曲信息',
                'verbose_name_plural': '歌曲信息',
            },
        ),
        migrations.AddField(
            model_name='dynamic',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名'),
        ),
        migrations.AddField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名'),
        ),
    ]
