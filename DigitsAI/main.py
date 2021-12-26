import sys
import pygame
import numpy as np
from tensorflow import keras
from models.grid import Button , Poly , Text



def create_grid(screen, poly : object , n : int) -> np.ndarray:

    MAPW , MAPH = 500 ,500

    polys = np.ndarray(shape = (n,n),dtype = 'object')

    cx ,cy = MAPW//n, MAPH//n

    st = 50

    for i in range(n):
        for j in range(n):

                points = [(i*cx + st, j*cy + st),
                        ( (i + 1)*cx + st,j*cy + st),
                        ( (i + 1)*cx + st , (j + 1)*cy + st),
                        (i*cx + st, (j + 1)*cy + st)]

                poly = Poly(screen,points,0)
                polys[i,j] = poly

    return polys


def classify(digit : np.ndarray) -> int:

     digit = digit.T

     y_hat = model.predict(digit.reshape(1,28,28,1))

     return np.argmax(y_hat)


model = keras.models.load_model('model1.h5')

params = {'WIDTH':900,
         'HEIGHT':600,
         'BGCOLOR':(0,0,100),
         'N':28,
         'FRAMES':60}


pygame.init()

screen = pygame.display.set_mode((params['WIDTH'],params['HEIGHT']))

pygame.display.set_caption("DIGITS CLASSIFIER")

clock = pygame.time.Clock()

grid = create_grid(screen, Poly, params['N'])

matrix = np.zeros(shape = (params['N'],params['N']),dtype = 'float32')

predbutton = Button(screen,600,100,250,80)
predtxt = Text(screen,'  PREDICT  ',predbutton.x + 30 ,predbutton.y + 20,50)

clearbutton = Button(screen,600,250,250,80)
cleartxt = Text(screen,'  CLEAR  ',clearbutton.x + 30 ,clearbutton.y + 20,50)

pred = Text(screen,' PREDICTION ->',550 ,450 ,45)
num = Text(screen,'',800 ,440 ,70)

def run() -> None:

    while True:

        screen.fill(params['BGCOLOR'])

        x,y = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        predbutton.create()
        predtxt.create()

        clearbutton.create()
        cleartxt.create()

        pred.create()
        num.create()

        if predbutton.pressed(click,(x,y),predtxt):

                y_hat = classify(matrix)

                num.text = '{p}'.format(p = y_hat)


        if clearbutton.pressed(click,(x,y),cleartxt):

            for i in range(params['N']):

                for j in range(params['N']):

                    grid[i,j].w = 0
                    matrix[i,j] = 0.0


        for i in range(params['N']):

            for j in range(params['N']):

                grid[i,j].create()

                if click[0] and (x > grid[i,j].points[0][0] and x  < grid[i,j].points[1][0]) and (y > grid[i,j].points[0][1] and y < grid[i,j].points[2][1]):
                    grid[i,j].w = 2
                    matrix[i,j] = 255.0

                elif click[2] and (x > grid[i,j].points[0][0] and x  < grid[i,j].points[1][0]) and (y > grid[i,j].points[0][1] and y < grid[i,j].points[2][1]):
                    grid[i,j].w = 0
                    matrix[i,j] = 0.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        pygame.display.update()

        clock.tick(params['FRAMES'])





if __name__ == '__main__':

    run()
