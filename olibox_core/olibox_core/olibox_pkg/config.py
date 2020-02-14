import click
import toml
import os

snap_userdata = os.environ['SNAP_USER_DATA']

@click.command()
@click.option('--name', prompt='enter your name', help='enter user name')
@click.option('--age', prompt='enter your age', help='enter user age')
def init(name,
         age):


    config = f"""

     # This is a OLI Box TOML config file.
     title = "OLI BOX Config"

     [user_data]
     name = '{name}'
     age = '{age}'
     
     """
    parsed_config = toml.loads(config)
    formatted_config = toml.dumps(parsed_config)

    with open(snap_userdata + 'config.toml', 'w') as f:
        f.write(formatted_config)
