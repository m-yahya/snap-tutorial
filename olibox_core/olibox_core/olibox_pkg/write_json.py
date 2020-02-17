import json
import os

import click

snap_userdata = os.environ['SNAP_USER_DATA']


def write_values(file, new_data):
    """
    The function uses json.dump method to write the data object to a file.
    """

    if os.path.isfile(f'{snap_userdata}/{file}'):
        with open(f'{snap_userdata}/{file}') as f:
            data = json.load(f)

        data.update(new_data)
        with open(f'{snap_userdata}/{file}', 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        with open(f'{snap_userdata}/{file}', 'w+', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)


def read_values(file):
    """
    The function deserialize the JSON string from a file using json.load method.
    """
    try:
        with open(file) as f:
            data = json.load(f)
            return data
    except IOError:
        print('An IOError has occured!')
