from django import forms
from . models import Post

class PostForm(forms.ModelForm): # Форма для заполения Add Post. ModelForm позволяет создать поля заполнения для нашей модели
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # {'class':'form-control'} для связи стиля формы Bootstrap с нашей, т.е. это CSS стиль для input
            # Также в attrs можно прописать 'placeholder': 'This is Title PlaceHoleder stuff', т.е. это текст, который
            # исчезает при клике на поле для заполнения
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}), # TextInput для ввода текста
            'author': forms.Select(attrs={'class': 'form-control'}), #для автора необходим выбор в нашей форме
            'body': forms.Textarea(attrs={'class': 'form-control'}), # Т.к. текст поста это большая область для ввода, то исп. Textarea
        }