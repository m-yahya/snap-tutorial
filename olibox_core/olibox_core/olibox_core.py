
import atexit

import toml


import olibox_core.olibox_core.olibox_pkg as pkg


def init():
    pkg.init()


def print_user():
    test = 'This is test var'
    user = pkg.get_user()
    print(f'This is test print of {test}')
    print(f'this is {user}')

@atexit.register
def main():
    print_user()


if __name__ == '__main__':
    init()