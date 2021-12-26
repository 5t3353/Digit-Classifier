import pygame

class Poly(object):

    def __init__(self,screen,points,w):
        self.screen = screen
        self.color = (200,200,200)
        self.points = points
        self.w = w

    def create(self):
        pygame.draw.polygon(self.screen,color=self.color,points=self.points,width=self.w)

class Button(object):

    def __init__(self,screen,x,y,width,height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button = pygame.Rect(self.x,self.y,self.width,self.height)
        self.color = [100, 100, 100]

    def create(self):
        pygame.draw.rect(self.screen, self.color, self.button)

    def pressed(self,click,point,txt):
        self.click = click
        self.point = point
        self.txt = txt

        if self.click[0] and self.button.collidepoint(self.point):
            self.color = [0,0,0]
            self.txt.color  = [200,200,200]
            return True
        else:
            self.color = [200,200,200]
            self.txt.color = [0,0,0]
            return False

class Text(object):

    def __init__(self,screen,text,x,y,size):
        self.text = text
        self.x = x
        self.y = y
        self.font = 'Courier bold'
        self.size = size
        self.color = [200, 200, 200]
        self.screen = screen

    def create(self):
        self.textsurface = pygame.font.SysFont(self.font, self.size).render(self.text, False, self.color)
        self.screen.blit(self.textsurface,(self.x,self.y))
