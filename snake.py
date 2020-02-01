import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

#A class for each individual cube in the snake
class Cube(object):
    rows = 20       #set rows and columns for game board
    width = 500     #set pixel width and height of game board

    #start at a set position facing right with a set color
    def __init__(self, start, direcX=1, direcY=0, color(200,200,200)):
        self.position = start
        self.direcX = 1
        self.direcY = 0
        self.color = color

    def move(self, direcX, direcY):
        #update the direction the snake is facing
        self.direcX = direcX
        self.direcY = direcY
        #make sure the snake moves in accordance to where it is facing
        self.position = (self.position[0] + self.direcX, self.position[1] + self.direcY)

    def draw(self, surface, eyes=False):
        #get the size the snake should be by finding how big each cube on the board is
        space = self.width // self.rows
        #get the row and column the snake is at
        i = self.position[0]
        j = self.position[1]

        #draw a rectangle on the correct surface with the right color, size, and coordinates, plus some offset to place it correctly
        pygame.draw.rect(surface, self.color, (i * space + 1, j * space +1, space - 2, space - 2))
        #if this is the head of the snake, draw eyes on it
        if eyes:
            center = space // 2
            radius = 3
            circleMiddle0 = (i * space + center - radius, j * space + 8)
            circleMiddle1 = (i * space + space - radius * 2, j * space + 8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle0, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle1, radius)
            

#take all the cube objects of the snake and put them together
class Snake(object):
    #array to hold all cube objects of the snake
    bodyCubes = []
    #keep track of where and which direction every turn is at for the tail of the snake to follow
    turns = {}

    #start the snake 4 cubes big facing right
    def __init__(self, color, position):
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.addCube()
        self.addCube()
        self.addCube()
        self.direcX = 0
        self.direcY = 1
        
    def move(self):
        for event in pygame.event.get():
            #quit the game when told to
            if event.type == pygame.QUIT:
                pygame.quit()
                #always call exit() when quitting to avoid an error
                exit()

            #if we don't quit the game lets see if any keys are pressed and act accordingly
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.direcX = -1
                    self.direcY = 0
                    self.turns[self.head.position[:]] = [self.direcX, self.direcY]
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.direcX = 1
                    self.direcY = 0
                    self.turns[self.head.position[:]] = [self.direcX, self.direcY]
                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.direcX = 0
                    self.direcY = -1
                    self.turns[self.head.position[:]] = [self.direcX, self.direcY]
                elif keys[pygame.K_DOWN] or keys[pygame.K_a]:
                    self.direcX = 0
                    self.direcY = 1
                    self.turns[self.head.position[:]] = [self.direcX, self.direcY]

            #for each cube in our snakes body
            for i, cube in enumerate(self.body):
                position = cube.position[:]
                if position in self.turns:
                    turn = self.turns[position]
                    cube.move(turn[0], turn[1])
                    if i == len(self.body) - 1:
                        self.turns.pop(p)
                else:
                    if cube.direcX == -1 and cube.position[0] <= 0:
                        cube.position = (c.rows - 1, c.position[1])
    def reset(self, position):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(screenWidth, rows, surface):
    pass

def redrawWindow(surface):
    pass

def createSnack(rows, item):
    pass

def main():
    pass

if __name__ == "__main()__":
    main()
