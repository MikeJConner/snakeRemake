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
            

class Snake(object):
    def __init__(self, color, position):
        pass

    def move(self):
        pass

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
