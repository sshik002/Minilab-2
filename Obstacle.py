from Displays import *

class Obstacle:
    TREE_SHAPE = [0x0E, 0x0A, 0x0E, 0x04, 0x0E, 0x04, 0x04, 0x0E]
    BIRD_SHAPE = [0x00, 0x0A, 0x15, 0x11, 0x1F, 0x04, 0x00, 0x00]

    def __init__(self, x, y, type, display):
        self.xpos = x
        self.ypos = y
        self.type = type
        self.display = display
        if self.type == 'tree':
            self.display.addShape(1, Obstacle.TREE_SHAPE)
        elif self.type == 'bird':
            self.display.addShape(2, Obstacle.BIRD_SHAPE)

    def move(self):
        self.xpos -= 1

    def draw(self):
        if self.type == 'tree':
            self.display.showText(f"{chr(1)}", self.ypos, self.xpos)
        elif self.type == 'bird':
            self.display.showText(f"{chr(2)}", self.ypos, self.xpos)
