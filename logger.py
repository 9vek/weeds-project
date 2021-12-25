import datetime
import json
import os


def has_log(file_name):
    file_path = f'{file_name}.json'
    if os.path.exists(file_path):
        return True
    else:
        return False


def write_log(file_name, obj):
    if has_log(file_name):
        return

    file_path = f'{file_name}.json'
    json_str = json.dumps(obj)
    with open(file_path, 'w+') as json_file:
        json_file.write(json_str)


def override_log(file_name, obj):
    file_path = f'{file_name}.json'
    json_str = json.dumps(obj)
    with open(file_path, 'w+') as json_file:
        json_file.write(json_str)


def read_log(file_name):
    if has_log(file_name):
        file_path = f'{file_name}.json'
        with open(file_path, 'r') as json_file:
            obj = json.load(json_file)
        return obj
    else:
        return None

def console_log(info):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {info}")