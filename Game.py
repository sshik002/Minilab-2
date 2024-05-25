import time
import random
from Displays import LCDDisplay
from LightStrip import LightStrip
from Button import Button
from Buzzer import PassiveBuzzer
from Dino import Dino
from Obstacle import Obstacle

class Game:
    def __init__(self):
        self._buzzer = PassiveBuzzer(16)
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._lightstrip = LightStrip(name='Neo', pin=2, numleds=16)
        self.button_jump = Button(10, 'jump', buttonhandler=self.handle_button)
        self.button_duck = Button(11, 'duck', buttonhandler=self.handle_button)
        self.dino = Dino(x=0, y=1, display=self._display)
        self.obstacles = []
        self.score = 0

    def handle_button(self, pin):
        if pin == 10:
            self.dino.jump()
        elif pin == 11:
            self.dino.duck()

    def start(self):
        self._display.showText("Welcome to Dino Game")
        time.sleep(2)
        self._display.clear()
        while True:
            self.update()
            self._display.clear()
            self.display_game()
            self._display.display()
            time.sleep(0.1)

    def update(self):
        self.dino.move()
        for obstacle in self.obstacles:
            obstacle.move()
            if self.check_collision(self.dino, obstacle):
                self.game_over()
        self.add_obstacle_if_needed()
        self.score += 1

    def check_collision(self, dino, obstacle):
        return dino.xpos == obstacle.xpos and dino.ypos == obstacle.ypos

    def game_over(self):
        self._buzzer.beep(1000, 1)
        print("Game Over! Your score is:", self.score)
        time.sleep(2)
        self.__init__()

    def add_obstacle_if_needed(self):
        if len(self.obstacles) == 0 or self.obstacles[-1].xpos < 10:
            type = random.choice(['tree', 'bird'])
            y = 1 if type == 'tree' else 0
            self.obstacles.append(Obstacle(x=16, y=y, type=type, display=self._display))

    def display_game(self):
        self.dino.draw()
        for obstacle in self.obstacles:
            obstacle.draw()
        self._display.showText(f'Score: {self.score}', 0, 0)
