from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# ListView встроенный класс в django, позволяющий просматривать все записи в нашем посте, т.е. делается QuerySet в БД
# для отображения всех записей из таблицы, а DetailView для просмотра только одной записи из одной таблицы
# ListView  - all Posts on our page
# Detail View - one Post on our page
# CreateView = creates things
# UpdateView - update things
from .models import Post

from .forms import PostForm, EditForm

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView): # view для отображения данных на главной странице
    model = Post # прописываем модель, данные мз которой мы будем отображать
    template_name = 'home.html' # html страничка на которой это будет отображаться

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm # Если мы исп. форму для заполнения, то поля во fields не надо прописывать
    template_name = 'add_post.html'
   #fields = '__all__' # если ходим все поля заполнять при добавлении поста
    #fields = ('title', 'body') # для заполнения только определенных полей при добавлении поста

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # Нельзя использовать form_class и fields одновременно.

