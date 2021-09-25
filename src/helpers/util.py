import json
from os import walk
from os.path import join
from zipfile import ZipFile

from yaml import safe_load

from src import settings
from . import STATUS_ERROR


def get_config_key(key):
    return safe_load(open(join(settings.RESOURCE_PATH, 'config.yml')))[key]


def get_json_by_json_filename(json_filename):
    with open(json_filename) as json_file:
        return json.load(json_file)


def zip_folder(folder, zip_file):
    with ZipFile(zip_file, 'w') as zip_obj:
        for folder_name, _, file_names in walk(folder):
            for file_name in file_names:
                zip_obj.write(join(folder_name, file_name), join('output-csv', file_name))


def result_format(df):
    str_columns = ''
    result = []

    for column in df.columns:
        str_columns += column.replace('\r\n', '') + ';'
    result.append(str_columns[:-1])

    for row in df.values:
        value = ''
        for row_value in row:
            value += str(row_value).replace('\r\n', '') + ';'
        result.append(value[:-1])

    return result


def response_body(func):
    def wrapper(*args, **kwargs):
        resp = func(**kwargs)
        return json.dumps(resp), (500 if STATUS_ERROR in resp['status'] else 200), {
            'Content-Type': 'application/json; charset=utf-8'}

    wrapper.__name__ = func.__name__
    return wrapper
