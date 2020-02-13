
import atexit

import toml


import olibox_core.olibox_core.olibox_pkg as pkg


def init():
    pkg.init()


def print_user():
    user = pkg.get_user()
    print(user)

@atexit.register
def main():
    print_user()


if __name__ == '__main__':
    init()