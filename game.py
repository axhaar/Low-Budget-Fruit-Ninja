import pygame, sys
import os
import random

player_lives = 3                                                
score = 0                                                       
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']    

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

gameDisplay.fill((BLACK))
background = pygame.image.load('back.jpg')                                
font = pygame.font.Font(os.path.join(os.getcwd(), 'font.otf'), 42)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))   
lives_icon = pygame.image.load('white_lives.png')   

pygame.quit()