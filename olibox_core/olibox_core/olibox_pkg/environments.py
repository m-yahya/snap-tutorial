import os

import toml

snap_userdata = os.environ['SNAP_USER_DATA']

if os.path.isfile(snap_userdata + 'config.toml'):
    f = toml.load(snap_userdata + 'config.toml')

    items = f.keys()
    unique_dict = {}
    for item in items:
        if type(f[item]) is not str:
            for i in f[item].keys():
                unique_dict[i] = f[item][i]
        else:
            unique_dict[item] = f[item]

    locals().update(unique_dict)

    # for key, val in new_dict.items():
    #     exec(key + '=val')

else:
    print('file not found')
