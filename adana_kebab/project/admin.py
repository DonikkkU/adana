from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .models import *


urlpatterns = [
    path('admin/', admin.site.urls),
]
# rasm, fayl, videolarni url orqali ochish uchun
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.register(Profile)
admin.site.register(Users)
admin.site.register(About)
admin.site.register(News)
admin.site.register(Menu)
admin.site.register(Main)
admin.site.register(Gallery)