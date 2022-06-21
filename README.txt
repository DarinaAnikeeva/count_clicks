# Обрезка ссылок с помощью Битли
С помощью Битли вы сможете сократить вашу ссылку, а затем посчитать количество кликов по ней


## Для запуска проекта необходимo:
  1. Pегистрация на сервисе Bitly. 
  2. Генерация своего токена в разделе API на сервисе Bitly (Generate token). Токен будет примерно такой ```13c194b550eeb8d3506b439fc97cc1e906adbb65```
  3. Создать в корневом катологе файл .env .
  4. Записать в этом файле ваш BITLY_TOKEN = '......'

Python3 должен быть уже установлен. Затем використовуйте `pip `(или , есть конфликт с Python2 `pip3`) для установки зависимостей:

`pip install -r requirements.txt`


# Что за BITLY_TOKEN?(Переменные окружения)

Переменные окружения нужны для защиты данных. К примеру если вы не хотите показывать свои пароли или токены каждому, кто посмотрит ваш код

Посмотреть имеющиеся переменные окружения можно командой env :
```
env

TERM=xterm-256color
SHELL=/bin/bash
LC_ALL=en_US.UTF-8
USER=kirill.m
HEXLET_VERSION=v2711
PATH=/home/kirill.m/bin:/home/kirill.m/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
PWD=/home/kirill.m
LANG=en_US.UTF-8
SHLVL=1
HOME=/home/kirill.m
LOGNAME=kirill.m
```
Обычно используются переменные, названные заглавными буквами: BITLY_TOKEN


## Примеры запуска скриптов:
```
Введите ссылку: https://www.google.com/search?q=rjn&oq=rjn&i57j69i60l2j69i65.3247j0j7&sourceid=chrome&ie=UTF-8
Битлинк:  bit.ly/3H9UC7R
 ```

```
Введите ссылку: bit.ly/3H9UC7R
Кликов по ссылке:  1
```