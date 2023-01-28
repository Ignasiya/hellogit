***Инструкция по GIT***
=========================

Дорожная карта
--------------------------

![Коды GIT](/hellogit/GITcode.jpg)

# Начало

Для начала надо представиться перед GITом, для этого в териминале пишем: 

    git config --global user.name "<ваше_имя>"

    git config --global user.email "<адрес_почты@email.com>"

git init

#Добавим все файлы проекта в нам будующий commit
git add .
#Или так
git add --all

#Если хотим добавить конкретный файл то можно так
git add <имя_файла> 

#Теперь создаем commit. Обязательно указываем комментарий.
#И не забываем про кавычки
git commit -m "<комментарий>"
git help # справка по всем командам
git clone
git status
git branch
git checkout
git merge
git remote
git fetch
git push
git pull
git branch <название_ветки>
# Переключаемся в master
git checkout master
# Обновляем локальную ветку с сервера
git pull origin master

# Делаем merge вашей ветки, в ветку в которой вы находитесь
# В данном примере это master
git merge <название_ветки>

Памятка по git
==============

- [Git для новичков (часть 1)](https://habr.com/ru/post/541258/)

- [Git для новичков (часть 2)](https://habr.com/ru/post/542616/)