from django.shortcuts import render
from django.views.generic import ListView, DetailView
# ListView встроенный класс в django, позволяющий просматривать все записи в нашем посте, т.е. делается QuerySet в БД
# для отображения всех записей из таблицы, а DetailView для просмотра только одной записи из одной таблицы
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView): # view для отображения данных на главной странице
    model = Post # прописываем модель, данные мз которой мы будем отображать
    template_name = 'home.html' # html страничка на которой это будет отображаться

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'