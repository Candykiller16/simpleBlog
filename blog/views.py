from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# ListView встроенный класс в django, позволяющий просматривать все записи в нашем посте, т.е. делается QuerySet в БД
# для отображения всех записей из таблицы, а DetailView для просмотра только одной записи из одной таблицы
# ListView  - all Posts on our page
# Detail View - one Post on our page
# CreateView = creates things
# UpdateView - update things
from .models import Post, Category

from .forms import PostForm, EditForm

from django.urls import reverse_lazy


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):  # view для отображения данных на главной странице
    model = Post  # прописываем модель, данные мз которой мы будем отображать
    template_name = 'home.html'  # html страничка на которой это будет отображаться
    # ordering = ['-id'] # посты будут отображаться в обратном порядке сверху вниз
    ordering = ['-post_date']  # посты отображаются по дате создания

    def get_context_data(self, *args, **kwargs):  # функция, что вставлять категории на нашу страницу в строке навигации
        cat_menu = Category.objects.all()  # нам необходимо сделать запрос в таблицу Category, чтобы прилинковать их
        context = super(HomeView, self).get_context_data(*args, **kwargs) # куда мы будем его отдавать в виде словаря
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):  # сюда мы добавили, чтобы видеть cat_menu в этой view
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm  # Если мы исп. форму для заполнения, то поля во fields не надо прописывать
    template_name = 'add_post.html'


# fields = '__all__' # если ходим все поля заполнять при добавлении поста
# fields = ('title', 'body') # для заполнения только определенных полей при добавлении поста

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # Нельзя использовать form_class и fields одновременно.


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    # в models.py был прописан get_absolute_url для перенаправления после созд. и удаления поста
    # но это не работает при удалении поста, для этого надо указать success_url


class AddCategotyView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories)  # в фильтре category- это поле в таблице Post,
    # categories - параметр функции. replace заменяет - в url адресе на пробел, чтобы мы могли увидеть категорию сост. из 2-ух слов
    return render(request, 'categories.html', {'categories': categories.title(), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})
