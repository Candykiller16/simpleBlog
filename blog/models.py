from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255) # title Поста, текстовый формат с максимальной длиной 255 символов
    title_tag = models.CharField(max_length=255, default='My blog') # отвечает за название вкладки
    author = models.ForeignKey(User, on_delete=models.CASCADE) # внешний ключ для таблицы User, с каскадным удалением
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) # т.к. author это объект, необходимо преобразовать его в строку

