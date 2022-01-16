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

Commit 9:
1. Создан update_post.html для станицы с редактированием поста
2. Добавлена view для редактирования поста UpdatePostView
3. В home.html and article_details.html добавлена ссылка для изменения поста
4. Создана EditForm для того, чтобы изменять не все поля при редактировании поста

Commit 10:
1. В HomeView добавлен ordering, чтобы посты отображались в обратном порядке на странице
2. Создана DeletePostView для удаления поста
3. Создана delete_post.html страничка для удаления поста
4. В urls.py прописан пусть для удаления поста
5. Для удаления поста в views.py необходимо указать success_url для перенаправления на главную станицу

Commit 11:
1. Добавлено поле post_date в модель Post
2. В article_details.html добавлено отображение даты
3. В HomeView добавлено ordering с -post_date т.е. самый поздний пост будет вначале

Commit 12:
1. Добавлено новое приложение members, в котором будет реализовано возможность регистрации новых пользователей для блога
2. В members создан файл urls.py
3. В core/setting.py в INSTALLED_APPS зарегситрировали наше приложение members
4. В core/urls.py подключили Django authentication system и app members
5. В members создали urls.py
6. В members создана папка templates/registration в которой созд. файлы login.html and register.html в которой 
будут формы для входа и регистрации
7. В members/views созд. UserRegisterView для регистрации пользователей исп. CreateView из библиотеки generic
8. В navbar в base.html создали ссылку на регистрацию register 
9. В navbar в base.html создали ссылку на вход login, но нам не надо её прописывать в members/urls.py т.к. в core/urls.py
мы подключили django.contrib.auth.urls, а login входит в пакет urls
10. В core/settings.py прописали LOGIN_REDIRECT_URL и LOGOUT_REDIRECT_URL, чтобы после входа нас перенаправляли на главную страницу


