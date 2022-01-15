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
