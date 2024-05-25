from Displays import *

class Dino:
    DINO_SHAPE = [0x04, 0x0E, 0x0E, 0x04, 0x1F, 0x04, 0x0A, 0x11]

    def __init__(self, x, y, display):
        self.xpos = x
        self.ypos = y
        self.jumping = False
        self.ducking = False
        self.jump_height = 1
        self.duck_height = 1
        self.ground_y = y
        self.display = display
        self.display.addShape(3, Dino.DINO_SHAPE)

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.ypos -= self.jump_height

    def duck(self):
        if not self.ducking:
            self.ducking = True
            self.ypos += self.duck_height

    def move(self):
        if self.jumping:
            self.jumping = False
            self.ypos = self.ground_y
        if self.ducking:
            self.ducking = False
            self.ypos = self.ground_y

    def draw(self):
        self.display.showText(f"{chr(3)}", self.ypos, self.xpos)
