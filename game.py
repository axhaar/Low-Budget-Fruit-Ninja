import pygame, sys
import os
import random

WIDTH = 800
HEIGHT = 500                                                
pygame.init()
pygame.display.set_caption('Low Budget Fruit-Ninja')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))  
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
