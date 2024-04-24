import os
from dotenv import load_dotenv
import requests
from pprint import pprint
from sqlcomands import get_postgre_sex

load_dotenv()
token = os.getenv('BITRICS')
url = os.getenv('URL')


def bitrics_get_contact(url, id):
    """
    Получает данные контакта по id
    :param url: Вебхук для вызова rest api
    :param id: Искомый id контакта
    :return: Имя контакта (str), если контакт с таким id есть в системе и None, если такого контакта нет
    """
    method = 'crm.contact.get'
    parametr = {
        'id': id
    }
    url = url + method
    response = requests.post(url, parametr).json()
    try:
        name = response['result']['NAME']
        return name
    except KeyError:
        print(f'Нет контакта с id {id}')
        return None


def bitrics_add_contact(url, name, second_name, last_name):
    """
    Создает новый контакт
    :param url: Вебхук для вызова rest api
    :param name: Имя контакта
    :param second_name: Отчество
    :param last_name: Фамилия
    :return: response
    """
    parametr = {
        'fields':
            {
                "NAME": name,
                "SECOND_NAME": second_name,
                "LAST_NAME": last_name,
                "OPENED": "Y",
                "ASSIGNED_BY_ID": 1,
                "TYPE_ID": "CLIENT",
                "SOURCE_ID": "SELF",
            },
        'params': {"REGISTER_SONET_EVENT": "N"}
    }
    method = 'crm.contact.add'
    url = url + method
    response = requests.post(url, json=parametr).json()
    return response


def get_fields(url):
    """

    :param url: Вебхук для вызова rest api
    :return: json с полями контакта
    """
    method = 'crm.contact.fields'
    url = url + method
    response = requests.post(url).json()
    return response


def add_field(url, field_name, rus_fieldname):
    """
    Добавляет пользовательское полу
    :param url: Вебхук для вызова rest api
    :param field_name: Имя поля
    :param rus_fieldname: Имя поля для отображения
    :return: результат
    """
    parametr = {
        'fields':
            {
                "FIELD_NAME": field_name,
                "EDIT_FORM_LABEL": rus_fieldname,
                "LIST_COLUMN_LABEL": rus_fieldname,
                "USER_TYPE_ID": "string",
                "XML_ID": field_name,
            },
    }
    method = 'crm.contact.userfield.add'
    url = url + method
    response = requests.post(url, json=parametr).json()
    return response


def update_sex_info(url, sex, id):
    """

    :param url: Вебхук для вызова rest api
    :param sex str: Пол 'Мужской' или 'Женский'
    :param id: id сонтакта
    :return: результат запроса
    """
    method = 'crm.contact.update'
    parametr = {
        'id': id,
        'fields': {
            'UF_CRM_SEX': sex
        },
        'params': { "REGISTER_SONET_EVENT": "N" }
    }
    url = url + method
    response = requests.post(url, json=parametr).json()
    return response


def make_sex_by_id(url):
    try:
        id = int(input('ВВеди номер id контакта '))
    except ValueError:
        print('Неверный ввод, должно быть число')
        return None
    name = bitrics_get_contact(url, id)
    if not name:
        return 'Нет контакта с таким id'
    sex = get_postgre_sex(name)
    if not sex:
        return 'Проблема с таблицами, проверьте БД'
    update_sex_info(url, sex, id)


if __name__ == '__main__':
    while True:
        make_sex_by_id(url)


    # bitrics_add_contact(url, 'Елена', "Васильевна", "Петрова")


