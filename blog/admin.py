from django.contrib import admin

from .models import Post # Регистрация наших models в админке

admin.site.register(Post)
