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
background = pygame.image.load('images/background.jpg')                                
font = pygame.font.Font(os.path.join(os.getcwd(), 'font.otf'), 42)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))   
lives_icon = pygame.image.load('images/white_lives.png')

def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x' : random.randint(100,500),               
        'y' : 800,
        'speed_x': random.randint(-10,10),    
        'speed_y': random.randint(-80, -60),    
        'throw': False,                       
        't': 0,                               
        'hit': False,
    }
    if random.random() >= 0.75:     
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

font_name = pygame.font.match_font('font.otf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

def draw_lives(display, x, y, lives, image) :
    for i in range(lives) :
        img = pygame.image.load(image)
        img_rect = img.get_rect()      
        img_rect.x = int(x + 35 * i)   
        img_rect.y = y                 
        display.blit(img, img_rect)
def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))

pygame.quit()