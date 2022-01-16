Первый commit
1. Создал приложение blog
2. Зарегитсрировал приложение в core/setting.py
3. Спроектировал модель для Post
4. Зарегистрировал модель в core/admin.py 
    admin.site.register(Post)
5. Прописал в core/urls.py URLConf для blog
6. В blog/views.py прописал view для главной страницы с исп. home.html
7. Прописал в blof/urls.py url для view home
8. Проинициализировал git init 
9. Создал .gitignore для игнорирования вирт.среды

Второй commit
Добавил README.md файл

Третий commit

1.В view через импортированные классы ListView and DetailView прописали функционал
 - на главной странице home.html через цикл for вывел все данные из таблицы Post исп. ListView
 - в созд. article_details.html, это инд. страница поста, к которой мы получаем доступ через pk получаем всю инф. о посте

Пятый коммит(4 лишний был)
1. Изменения в html файлах, добавлен шаблон bootstrap в base.html
2. Добавлен title_tag  в model Post для отображения имени вкладки в браузере

Commit 7:
1. Добавлена страница для добавления поста Add Post
2. Созд. страница add_post.html
3. В models добавлена переадресация get_absolute_url после добавления поста
4. В urls добавлена новый адрес для добавления поста
5. В строке навигации добавлена ссылка для добавления поста
6. В views написал класс Add Post для заполнения/добавления поста

Commit 8:
1. Добавлен файл blog/forms.py для создания формы заполнения в Add Post, т.к. Django tag {{from.as_p}} нам не подходит
2. Связал форму с моделью Post в blog/views.py