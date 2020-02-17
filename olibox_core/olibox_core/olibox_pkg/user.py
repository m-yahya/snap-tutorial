
import time
from .environments import *

from .write_json import write_values

snap_userdata = os.environ['SNAP_USER_DATA']

# MQTT basic Functions

# dont touch


def get_user():
    print(f'this is working{name}')
    n = name 
    a = age

    payload_power = {'activePower_demand': age}
    write_values('power-data.json', payload_power)

    return(n, a)