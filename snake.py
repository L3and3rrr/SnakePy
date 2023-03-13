import pygame as pg

class Snake(object):
    def __init__(self,game,startX: int,startY: int):
        self._game = game
        self._coords = [(startX,startY)]
        self._direction = 'right'

    def getHeadCoordinates(self) -> tuple:
        return self._coords[0]

    def getLength(self) -> int:
        return len(self._coords)

    def update(self,direction: str) -> None:
        # update: direction, coordinates, check boundaries, check if food is hit (or remove last coordinate tuple)
        blocksize = self._game.getScreen().getBlocksize() # defines blocksize for this method
        # update direction
        if self.getLength() >= 1:
            if (direction == '') or (self._direction == 'right' and direction == 'left') or (self._direction == 'left' and direction == 'right') or (self._direction == 'up' and direction == 'down') or (self._direction == 'down' and direction == 'up'):
                pass
            else:
                self._direction = direction
        # update coordinates by pushing new tuple to self._coords 
        if self._direction == 'up':
            self._coords.insert(0,(self._coords[0][0] ,self._coords[0][1] - blocksize))
        elif self._direction == 'down':
            self._coords.insert(0,(self._coords[0][0] ,self._coords[0][1] + blocksize))
        elif self._direction == 'right':
            self._coords.insert(0,(self._coords[0][0] + blocksize,self._coords[0][1]))
        else: # direction 'left'
            self._coords.insert(0,(self._coords[0][0] - blocksize,self._coords[0][1]))
        # check boundaries
        if (self._coords[0][0] < 0 or self._coords[0][0] >= self._game.getScreen().getWidth() or self._coords[0][1] < 0 or self._coords[0][1] >= self._game.getScreen().getHeight()):
            self._game.setRunning(False)
            return
        # check if collision with tail
        if len(self._coords) > 4:
            for i in range(4,len(self._coords)):
                if self.getHeadCoordinates()[0] == self._coords[i][0] and self.getHeadCoordinates()[1] == self._coords[i][1]:
                    self._game.setRunning(False)
                    return
        # check if food is hit (when not pop last element)
        if not (self._game.getFoodCoordinates()[0] == self._coords[0][0] and self._game.getFoodCoordinates()[1] == self._coords[0][1]):
            self._coords.pop()
        else:
            self._game.popFood()
        # draw snake
        for tup in self._coords:
            pg.draw.rect(self._game.getScreen().getSurface(),(255,255,255),[tup[0],tup[1],blocksize,blocksize])