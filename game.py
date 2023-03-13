import pygame as pg
from food import *
from snake import *
from screen import *
import random

pg.init()

class Game(object):
    def __init__(self):
        # initialize a clock
        self._clock = pg.time.Clock()
        # track running status of Game/Session
        self._running = True
        # initialize a screen
        self._screen = Screen(self)
        # initialize a snake
        self._snake = Snake(self,0,0)
        # track food objects in list
        self._food = []

    def getScreen(self) -> Screen:
        return self._screen

    def getSnake(self) -> Snake:
        return self._snake

    def getFoodAvailable(self) -> bool:
        return (len(self._food) > 0)

    def popFood(self) -> None:
        if self.getFoodAvailable():
            del self._food[0]

    def getFoodCoordinates(self) -> tuple:
        if self.getFoodAvailable():
            return self._food[0].getCoordinates()
        else: # return unreachable coordinates
            return (self._screen.getWidth(),self._screen.getHeight())

    def setRunning(self,run=True) -> None:
        self._running = run

    def main(self):
        while self._running:
            direction = ''
            self._clock.tick(15)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.setRunning(False)
                    break
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_i or event.key == pg.K_UP:
                        direction = 'up'
                    elif event.key == pg.K_j or event.key == pg.K_LEFT:
                        direction = 'left'
                    elif event.key == pg.K_k or event.key == pg.K_DOWN:
                        direction = 'down' 
                    elif event.key == pg.K_l or event.key == pg.K_RIGHT:
                        direction = 'right' 
            # update and redraw all objects on the screen
            self._screen.update(self._snake.getLength()) # update Screen (score on the top right)
            self._snake.update(direction) # update Snake
            if self.getFoodAvailable(): # update Food
                for food in self._food:
                    food.update()
            elif random.random() > 0.95: # maybe change to instant spawn ???
                rand_x = random.randrange(0,(self._screen.getWidth()-self._screen.getBlocksize()),self._screen.getBlocksize())
                rand_y = random.randrange(0,self._screen.getHeight()-self._screen.getBlocksize(),self._screen.getBlocksize())
                self._food.append(Food(self,rand_x,rand_y))
            pg.display.update()

if __name__ == '__main__':
    game = Game()
    # start game by entering main function
    game.main()

pg.quit()
exit()