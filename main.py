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
    
    if cam.y < -10:
        cam.y = 10

    if held_keys['space']:
        cam.y += 5 * time.dt
    elif held_keys['left shift']:
        cam.y -= 5 * time.dt

app = Ursina(fullscreen=True)

cam = FPC(gravity=0)
cam.y = 10

for z in range(10):
    for x in range(10):
        for y in range(10):
            block = BuildingBlock(pos=(x - 5, y, z - 5))

app.run()
