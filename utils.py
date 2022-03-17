from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController as FPC
from ursina.shaders import lit_with_shadows_shader as LWSS

Button.default_shader = LWSS

color_chosen = 1
colors = {1: color.white, 2: color.blue, 3: color.green, 4: color.yellow, 5: color.red, 6: color.black}
block_list = []
blocks = []

class BuildingBlock(Button):
    def __init__(self, pos = (0, 0, 0)):
        global block_list
        super().__init__(parent = scene, position = pos, model = 'cube', texture = 'white_cube', color = colors[color_chosen], collider='box')
        if len(block_list) > 0:
            self.index = block_list.index(block_list[-1]) + 1
        else:
            self.index = 0
        block_list.append((*self.position, color_chosen))
        blocks.append(self)

    def input(self, key):
        if self.hovered:
            global block_list
            global blocks
            if key == 'left mouse down':
                for block in blocks:
                    if block.index > self.index:
                        block.index -= 1
                del block_list[self.index]
                del blocks[blocks.index(self)]
                destroy(self)
            elif key == 'right mouse down':
                block = BuildingBlock(pos = self.position + mouse.normal)

def update():
    global color_chosen
    if held_keys['escape']: quit()

    if held_keys['1']: color_chosen = 1
    elif held_keys['2']: color_chosen = 2
    elif held_keys['3']: color_chosen = 3
    elif held_keys['4']: color_chosen = 4
    elif held_keys['5']: color_chosen = 5
    elif held_keys['6']: color_chosen = 6

    if held_keys['space']:
        cam.y += 7 * time.dt
    if held_keys['left shift']:
        cam.y -= 7 * time.dt

app = Ursina(fullscreen = True)

cam = FPC(gravity = 0)
cam.y = 1

if __name__ == '__main__':

    block = BuildingBlock(pos = (0, 0, 0))

    app.run()
