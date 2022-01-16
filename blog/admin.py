from django.contrib import admin

from .models import Post, Category # Регистрация наших models в админке

admin.site.register(Post)
admin.site.register(Category)
