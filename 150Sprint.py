from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import *

class Voxel(Button):
    def __init__(self,position = (0,0,0),color = color.white):
        super().__init__(parent = scene,
                         position = position,
                         model = 'cube',
                         origin_y = 0.5,
                         texture = 'white_cube',
                         color = color,)
    def destroy(self,user_input):
        u = randint(1, user_input)
        if u != 1 and x > 1:
            destroy(voxel)
        else:
            pass

def update():
        if player.x >= 149:
            t2 = time.time()
            tt = int(t2-t1)
            ans = 'Congrats, game finished! Ran in ',tt,'seconds'
            print_on_screen(text = ans,
                            position = (0, 0),
                            scale = 1,
                            duration = 10)
        else:
            pass

        if player.y < -1:
            print_on_screen('Mission Failed! Type cmd Q to leave, no cheating!',
                            position = (0, 0),
                            scale = 1,
                            duration = 5)
        else:
            pass
  
if __name__ == "__main__":
    user_input = int(input("Level?"))

app = Ursina()

window.fullscreen = False
window.color = color.blue


for z in range(3):
    for x in range(150):
        voxel = Voxel((x,0,z),color.white)
        voxel.destroy(user_input)
        
for z in range(3):
    for x in range(150,153):
        voxel = Voxel((x,0,z),color.orange)

player = FirstPersonController()

if player.x == 0:
    print_on_screen(text='w forward, a left, d right, s backwards, e jump',
                    position=(0,0),
                    scale=1,
                    duration=5)
    t1 = time.time()
else:
    pass

update()

app.run()
