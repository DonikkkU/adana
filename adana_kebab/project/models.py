from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.
from rest_framework.exceptions import ValidationError
def validate_file_extension(value):
    """
    Agar fayl kengaytmasi berilganlarning orasida bo'lmasa, xatolik beradi
    """
    # [0]  yo'li + fayl nomi
    # [1] fayl kengaytmasi,: .docx, .jpg

    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.MP4']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_audies_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.MP3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Users(models.Model):
    email = models.EmailField(blank=True, null=False)
    firs_name = models.CharField(max_length=50, blank=True, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=False)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()



class Profile(models.Model):
    bio = models.TextField(blank=False, null=True)
    location = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='portfolio', blank=True, default='empty.png')
    social_github = models.CharField(max_length=100, blank=True, null=True, default='men va sen')
    social_telegram = models.CharField(max_length=100, blank=True, null=True)
    social_instagram = models.CharField(max_length=100, blank=True, null=True)
    social_youtube = models.CharField(max_length=100, blank=True, null=True)
    social_website = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateField(auto_now=True)
    file = models.FileField(upload_to='files', null=True)
    video = models.FileField(upload_to='videos', null=True)
    audio = models.FileField(upload_to='audios', null=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)



# class Users(models.Model):
#     email = models.EmailField(blank=True, null=False)
#     firs_name = models.CharField(max_length=50, blank=True, null=False)
#     last_name = models.CharField(max_length=50, blank=True, null=False)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()



class About(models.Model):
    title = models.CharField(blank=True, max_length=200, null=False)
    about = models.TextField(blank=True, max_length=500, null=False)
    details = models.CharField(blank=True, max_length=100, null=False)
    image = models.ImageField(upload_to='portfolio', blank=True, default='')


class News(models.Model):
    title_1 = models.CharField(blank=True, max_length=100, null=False)
    title_2 = models.CharField(blank=True, max_length=100, null=False)
    news = models.CharField(blank=True, max_length=100, null=False)
    news_title = models.CharField(blank=True, max_length=100, null=False)
    news_about = models.TextField(blank=True, max_length=500, null=False)


class Menu(models.Model):
    header = models.CharField(blank=True, max_length=50, null=False)
    title = models.CharField(blank=True, max_length=100, null=False)
    categories = models.CharField(blank=True, max_length=100, null=False)
    product_name = models.CharField(blank=True, max_length=100, null=False)
    product_price = models.IntegerField(blank=True, null=False)
    product_about = models.TextField(blank=True, null=False, max_length=300)
    product_image = models.ImageField(upload_to='portfolio', blank=True, default='')


class Main(models.Model):
    header = models.CharField(blank=True, max_length=50, null=False)
    title = models.CharField(blank=True, max_length=100, null=False)
    categories = models.CharField(blank=True, max_length=100, null=False)
    product_image = models.ImageField(upload_to='portfolio', blank=True, default='')
    product_name = models.CharField(blank=True, max_length=100, null=False)
    product_date_added = models.DateField(auto_now=True)
    product_about = models.TextField(blank=True, null=False, max_length=300)


class Gallery(models.Model):
    header = models.CharField(blank=True, max_length=50, null=False)
    title = models.CharField(blank=True, max_length=100, null=False)
    image = models.ImageField(upload_to='portfolio', blank=True, default='')
    video = models.FileField(upload_to='video', null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)




