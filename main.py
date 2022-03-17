from ursina import *
from utils import BuildingBlock, app, cam
from utils import update as utils_update
import utils
import json

def load_blocks(json_list):
    for block_coords in json_list:
        utils.color_chosen = block_coords[-1]
        block = BuildingBlock(pos = block_coords[:-1])
    utils.color_chosen = 1

def save_blocks():
    with open('data.json', 'w') as f:
        f.write(json.dumps(utils.block_list, indent = 4))

def update():
    if held_keys['enter']:
        save_blocks()
    utils_update()

if __name__ == '__main__':
    try:
        with open('data.json', 'r') as f:
            load_blocks(json.loads(f.read()))
    except FileNotFoundError:
        block = BuildingBlock()

    app.run()
