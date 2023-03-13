import pygame as pg

class Screen(object):
    def __init__(self,game):
        pg.display.init()
        # create a screen
        pg.display.set_mode(size=(800,600))
        pg.display.set_caption('Snake')
        # initialize font
        self._font = pg.font.Font((pg.font.match_font('arialunicode')),21)
        # divide screen into blocks
        self._blocksize = 25 # fix blocksize to 25 at the moment

    # public functions
    def getHeight(self) -> int:
        return pg.display.get_window_size()[1]

    def getWidth(self) -> int:
        return pg.display.get_window_size()[0]

    def getSurface(self) -> pg.Surface:
        # return current surface
        return pg.display.get_surface()

    def getBlocksize(self) -> int:
        return self._blocksize

    # private score
    def __drawScore(self,score: int) -> None:
        text = ('Score: ' + str(score))
        text_draw = self._font.render(text,True,(0,255,0),'black')
        self.getSurface().blit(text_draw,dest=(self.getWidth()-pg.font.Font.size(self._font,text)[0],0))#pg.font.Font.size(self._font,text)[1]))

    def update(self,score: int) -> None:
        self.getSurface().fill('black')
        self.__drawScore(score)