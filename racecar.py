import pygame
import time
import random

# Initiate pygame
pygame.init()

# Clock
clock = pygame.time.Clock()

# RGB Color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Window size
wn_width = 500
wn_height = 400
wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption('Racing Game')

# Images
bg = pygame.image.load('assets/track.png')
carimg = pygame.image.load('assets/porsche.png')

# Boundary
west_b = 157
east_b = 359

class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = 80
        self.speedy = 3
        self.passed = 0

    def update(self):
        self.y += self.speedy
        if self.y > wn_height:
            self.y = 0 - self.height
            self.width = random.randint(10, 120)
            self.passed += 1

    def draw(self, wn):
        pygame.draw.rect(wn, RED, [self.x, self.y, self.width, self.height])
        right_blk_x = self.x + self.width + self.gap
        right_blk_width = east_b - right_blk_x
        pygame.draw.rect(wn, RED, [right_blk_x, self.y, right_blk_width, self.height])

class Player:
    def __init__(self):
        self.image = carimg
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = int(wn_width * 0.5)
        self.rect.y = int(wn_height * 0.5)

        self.speedx = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5  # Increase this value to make the car move faster to the left
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5   # Increase this value to make the car move faster to the right
        else:
            self.speedx = 0

        self.rect.x += self.speedx

        if self.rect.left < west_b:
            self.rect.left = west_b
        if self.rect.right > east_b:
            self.rect.right = east_b

# Functions
def score_board(passed):
    font = pygame.font.Font(None, 35)
    text = font.render('Passed: ' + str(passed), True, BLACK)
    wn.blit(text, (10, 10))

def crash():
    font = pygame.font.Font(None, 80)
    text = font.render('You crashed!', True, BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    x = int(wn_width / 2 - text_width / 2)
    y = int(wn_height / 2 - text_height / 2)
    wn.blit(text, (x, y))
    pygame.display.update()
    time.sleep(2)
    game_loop()

def game_loop():
    block_width = 60
    block_height = 20
    block_x = west_b
    block_y = -100

    player = Player()
    block = Block(block_x, block_y, block_width, block_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        player.update()
        block.update()

        wn.blit(bg, (0, 0))
        wn.blit(player.image, (player.rect.x, player.rect.y))
        block.draw(wn)

        # Improved collision detection
        if player.rect.colliderect(pygame.Rect(block.x, block.y, block.width, block.height)) or player.rect.colliderect(pygame.Rect(block.x + block.width + block.gap, block.y, east_b - (block.x + block.width + block.gap), block.height)):
            crash()

        score_board(block.passed)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
