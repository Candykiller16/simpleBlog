from django import forms
from . models import Post, Category

#choices = [('coding', 'coding'), ('anime', 'anime'), ('sports', 'sports'), ('games', 'games')] # список для формы category, так оно работает
# Первый способ создания. В параметры forms.Select() есть параметр choices в который мы может поместить наш список choices
# если бы список назывался cats, то запись бы выглядела так: choices=cats
# Второй способ
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm): # Форма для заполения Add Post. ModelForm позволяет создать поля заполнения для нашей модели
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # {'class':'form-control'} для связи стиля формы Bootstrap с нашей, т.е. это CSS стиль для input
            # Также в attrs можно прописать 'placeholder': 'This is Title PlaceHoleder stuff', т.е. это текст, который
            # исчезает при клике на поле для заполнения
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}), # TextInput для ввода текста
            'author': forms.Select(attrs={'class': 'form-control'}), #для автора необходим выбор в нашей форме
            'category': forms.Select(choices=choice_list, attrs={ 'class': 'form-control'}), #для категории необходим выбор в нашей форме
            'body': forms.Textarea(attrs={'class': 'form-control'}), # Т.к. текст поста это большая область для ввода, то исп. Textarea
        }

class EditForm(forms.ModelForm): # Форма для заполения Update Post. ModelForm позволяет создать поля заполнения для нашей модели
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # {'class':'form-control'} для связи стиля формы Bootstrap с нашей, т.е. это CSS стиль для input
            # Также в attrs можно прописать 'placeholder': 'This is Title PlaceHoleder stuff', т.е. это текст, который
            # исчезает при клике на поле для заполнения
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}), # TextInput для ввода текста
            'body': forms.Textarea(attrs={'class': 'form-control'}), # Т.к. текст поста это большая область для ввода, то исп. Textarea
        }