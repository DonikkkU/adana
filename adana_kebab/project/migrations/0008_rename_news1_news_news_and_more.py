# Generated by Django 4.0.6 on 2022-07-14 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_gallery_url_alter_gallery_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news1',
            new_name='news',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='news1_about',
            new_name='news_about',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='news1_title',
            new_name='news_title',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news2',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news2_about',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news2_title',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news3',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news3_about',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news3_title',
        ),
    ]
