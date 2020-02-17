import json
import os

import click

snap_userdata = os.environ['SNAP_USER_DATA']


def write_values(file, new_data):
    """
    The function uses json.dump method to write the data object to a file.
    """
    file_to_write = os.path.join(f'{snap_userdata}/{file}')
    print(file_to_write)
    if os.path.isfile(file_to_write):
        with open(file_to_write) as f:
            data = json.load(f)

        data.update(new_data)
        with open(file_to_write, 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        with open(file_to_write, 'w+', encoding='utf-8') as f:
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
