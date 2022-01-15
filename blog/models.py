from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255) # title Поста, текстовый формат с максимальной длиной 255 символов
    title_tag = models.CharField(max_length=255) # отвечает за название вкладки
    author = models.ForeignKey(User, on_delete=models.CASCADE) # внешний ключ для таблицы User, с каскадным удалением
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) # т.к. author это объект, необходимо преобразовать его в строку

    def get_absolute_url(self): # после заполнения формы для Add Post необходимо назначить этот метод для перенаправляения на страницу
        # return reverse('article_detail', args=(str(self.id))) при переадресации на страницу поста необх.указать args
        return reverse('home') # при переадресации в home не нужны args


