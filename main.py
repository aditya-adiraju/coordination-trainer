# importing modules
import pygame
import random

# initialising pygame window and elements
pygame.init()
SCREEN_WIDTH = 1152
SCREEN_HEIGHT = 720
bg = pygame.image.load('bg.jpg')
score_overlay = pygame.image.load('ScoreOverlay.png')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font("Roboto-Regular.ttf", 58)

if __name__ == '__main__':
    done = False
    frames = 0    # keeps track of how many frames have passed
    text = pick_random_finger()  # text for the test is selected
    i = 0  # index of words
    freeze = False  # used to see if the timer must be frozen
    color = (0, 0, 0)
    speed = 1
    red = pygame.image.load('Red.png')
    blue = pygame.image.load('Blue.png')
    green = pygame.image.load('Green.png')
    yellow = pygame.image.load('Yellow.png')
    colors = [green, red, yellow, blue]
    color = random.randint(0, 3)
    score = 0
    while not done:
        keys = pygame.key.get_pressed()

        # drawing screen elements
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h and color == 0:
                    color = random.randint(0, 3)
                    score += 1
                elif event.key == pygame.K_j and color == 1:
                    color = random.randint(0, 3)
                    score += 1
                elif event.key == pygame.K_k and color == 2:
                    color = random.randint(0, 3)
                    score += 1
                elif event.key == pygame.K_l and color == 3:
                    color = random.randint(0, 3)
                    score += 1


        points = font.render(str(score), True, (255, 255, 255))
        screen.blit(colors[color], (0,0))
        screen.blit(score_overlay, (0, 0))
        screen.blit(points, (int(SCREEN_WIDTH*0.485), int(SCREEN_HEIGHT//2)))
        clock.tick(60)
        pygame.display.flip()
