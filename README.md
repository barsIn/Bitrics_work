# Проект взаимодействию с bitrix и изменению карточки контакта: 
[Bitrix project](https://github.com/barsIn/Bitrics_work)

<br>

## Оглавление:
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Автор](#автор)

<br>

## Технологии:

<details><summary>Подробнее</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)


**Базы данных и инструменты работы с БД:**
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)

[⬆️Оглавление](#оглавление)
</details>

<br>

## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE.

<details><summary>Локальный запуск</summary> 


1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения:
```bash
git clone https://github.com/barsIn/pretension_work.git
touch .env
```
2. Добавьте переменные в файл .env
2.1 для битрикса бота:
- URL = 'https://your.bitrix24.ru/rest/1/key/' 
2.2 Для бызы данных
- DB_HOST = ''
- DB_PORT = 
- DB_USER = ''
- DB_PASS = ''
- DB_NAME = ''

<details><summary>Локальный запуск:</summary>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python3 -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Запустите приложение:
```bash
python3 main.py
```
 </details>

<h1></h1></details>


[⬆️Оглавление](#оглавление)

<br>

## Описание работы:

Данная программа получает данные контакта (ID, Имя) из Битрикс24 по Webhook проверяет имя контакта на наличие его в БД (PostgreSQL) 
Женские имена таблица names_woman
Мужские имена таблица names_man
Далее, если нашел имя в БД мужчин ставить пол Мужчина, если нашел имя в БД женщин ставить Женщина
Далее передавать данные по гендеру обратно в контакт по ID


[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Gerasimov Igor](https://github.com/barsIn)

[⬆️В начало](#Проект)
