import pygame as pg

class Food(object):
    def __init__(self,game,startX,startY):
        self._game = game
        self._coords = (startX,startY)
        self._color = (255,0,0)

    def getCoordinates(self) -> tuple:
        return self._coords

    def update(self) -> None:
        pg.draw.rect(self._game.getScreen().getSurface(),self._color,[self._coords[0],self._coords[1],self._game.getScreen().getBlocksize(),self._game.getScreen().getBlocksize()])