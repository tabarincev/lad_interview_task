# LAD Junior Data Engineer тестовое задание

## Задание 

Написать скрипт, который:
- Из 10 любых заданных по URL резюме сайта hh.ru (например, https://nn.hh.ru/resume/c1e0653900074b39780039ed1f7a4832516453)
соберет данные из разделов **ключевые навыки**, **занятость**, **график работы**, **желаемая зарплата**.
- Спроектировать базу для хранения собранных данных
- Загрузить собранные данные в БД (предпочтительно в PostgreSQL)

## Схема базы данных
![db_schema](https://i.imgur.com/oP6vz2u.jpg)
## Структура скрипта

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Для хранения базы данных используется [Heroku](https://heroku.com/). Скрипт состоит из нескольких модулей:
- parser.py - парсинг данных с hh.ru
- database.py - оболочка для подключения к серверу с базой данных и выполнения query
- main.py - главный файл
- config.py - файл конфигурации с данными для подключения к базе на Heroku
## Установка и запуск
Клонировать репозиторий себе на машину
```sh
$ git clone https://github.com/tabarincev/lad_interview_task.git
```
Установить *virtualenv*
```sh
$ pip install virtualenv
```
После установки создать виртуальное окружение командами:
- Windows
```sh
$ python -m venv venv
$ venv/Scripts/activate.bat
```
- Linux
```sh
$ python -m venv venv
$ source venv/bin/activate
```
Установить библиотеки из *requirements.txt*
```sh
$ pip install -r requirements.txt
```
Для запуска скрипта
```sh
$ python main.py
```
## Используемые библиотеки
 
 
| Библиотека | Документация |
| ------ | ------ |
| requests | https://docs.python-requests.org/en/latest/ |
| bs4 | https://beautiful-soup-4.readthedocs.io/en/latest/ |
| psycopg2 | https://www.psycopg.org/docs/ |


