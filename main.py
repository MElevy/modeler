from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController as FPC

class BuildingBlock(Button):
    def __init__(self, pos=(0, 0, 0)):
        super().__init__(parent=scene, position=pos, model='cube', texture='white_cube', color=color.white)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            elif key == 'right mouse down':
                block = BuildingBlock(pos=self.position + mouse.normal)

def update():
    if held_keys['escape']:
        quit()

    if held_keys['space']:
        cam.y += 7 * time.dt
    if held_keys['left shift']:
        cam.y -= 7 * time.dt

app = Ursina(fullscreen=True)

cam = FPC(gravity=0)
cam.y = 1

block = BuildingBlock(pos=(0, 0, 0))

app.run()
