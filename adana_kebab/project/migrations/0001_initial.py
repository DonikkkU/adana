# Generated by Django 4.0.6 on 2022-07-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(null=True)),
                ('location', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, default='empty.png', upload_to='portfolio')),
                ('social_github', models.CharField(blank=True, default='men va sen', max_length=100, null=True)),
                ('social_telegram', models.CharField(blank=True, max_length=100, null=True)),
                ('social_instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('social_website', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateField(auto_now=True)),
                ('file', models.FileField(null=True, upload_to='files')),
                ('video', models.FileField(null=True, upload_to='videos')),
                ('audio', models.FileField(null=True, upload_to='audios')),
            ],
        ),
    ]
