import pygame

import random

# Initialize pygame

pygame.init()

# Screen settings

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Easy Space Invader")

# Colors

WHITE = (255, 255, 255)

RED = (255, 0, 0)

BLUE = (0, 0, 255)

GREEN = (0, 255, 0)

BLACK = (0, 0, 0)

# Clock

clock = pygame.time.Clock()

# Player

player_width = 50

player_height = 40

player_x = WIDTH // 2

player_y = HEIGHT - 60

player_speed = 6

# Bullet

bullet_width = 5

bullet_height = 10

bullet_x = 0

bullet_y = player_y

bullet_speed = 7

bullet_state = "ready"

# Enemy

enemy_width = 40

enemy_height = 30

enemy2_x = random.randint(0, WIDTH - enemy_width)

enemy2_y = random.randint(50, 150)

enemy2_speed = 3

enemy2_width = 40

enemy2_height = 30

enemy2_x = random.randint(0, WIDTH - enemy_width)

enemy2_y = random.randint(50, 150)

enemy2_speed = 3

# Score

score = 0

font = pygame.font.SysFont(None, 36)

def show_score():
    score_text = font.render(f"Score : {score}", True, WHITE)
    screen.blit(score_text, (10,10))

def player(x,y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def enemy(x,y):
    pygame.draw.rect(screen, RED, (x, y, enemy_width, enemy_height))

def enemy2(x,y):
    pygame.draw.rect(screen, BLUE, (x, y, enemy2_width, enemy2_height))

def fire_bullet(x,y):
    pygame.draw.rect(screen, WHITE, (x + 22, y, bullet_width, bullet_height))

def collisition(ex,ey,bx, by):
    return abs(ex - bx) < 30 and abs(ey - by) < 30



