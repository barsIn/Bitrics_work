import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
conn = psycopg2.connect(dbname=dbname, host=host, user=user, password=password)


def get_postgre_sex(name):
    """

    :param name str: Имя которое проверяется на пол
    :return: 'Мужской' или 'Женский' если такое имя есть в соответсвующе ДБ, 'Пол не определен' если имени в ДБ нет
    None, если хоть одна из таблиц не создана
    """
    conn = psycopg2.connect(dbname=dbname, host=host, user=user, password=password)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                f'''SELECT id
                FROM names_man
                WHERE name = '{name}'
                '''
            )
            result = cursor.fetchone()
        if result:
            return 'Мужской'
        else:
            with conn.cursor() as cursor:
                cursor.execute(
                    f'''SELECT id
                    FROM names_woman
                    WHERE name = '{name}'
                    '''
                )
                result = cursor.fetchone()
            return 'Женский' if result else 'Пол не определен'

    except psycopg2.errors.UndefinedTable as e:
        print('Таблица не создана')
    finally:
        conn.close()

