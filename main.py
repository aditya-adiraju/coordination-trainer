# importing modules
import pygame
import random
from pygame import mixer
# initialising pygame window and elements
pygame.init()
mixer.init()
mixer.music.set_volume(0.7)
SCREEN_WIDTH = 1152
SCREEN_HEIGHT = 720
bg = pygame.image.load('bg.png')
end = pygame.image.load('GameOver.png')
score_overlay = pygame.image.load('ScoreOverlay.png')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font("Retro Gaming.ttf", 58)


def show_text(t):
    lines = list(t)
    words_per_line = 20
    j = 0
    while j + words_per_line < len(lines):
        line = "".join(lines[j:j + words_per_line])
        if lines[j + words_per_line:].count(' ') > 0:
            t2 = lines[j + words_per_line:]
            k = lines[j + words_per_line:].index(' ')
            line = line + "".join(lines[j + words_per_line:j + words_per_line + k])
            test = "".join(lines[j + words_per_line:k])
            j += k + 1
        display_text = font.render(line, True, (255, 255, 255))
        screen.blit(display_text, (int(SCREEN_WIDTH * 0.05), 70 + 45 * (j // words_per_line)))
        j = j + words_per_line
    line = "".join(lines[j:])
    display_text = font.render(line, True, (255, 255, 255))
    screen.blit(display_text, (int(SCREEN_WIDTH * 0.05), 70 + 45 * (j // words_per_line)))


def mainloop():
    done = False
    freeze = False
    frames = 0  # keeps track of how many frames have passed
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
        screen.fill((0, 0, 0))
        welcome_text = "Welcome to the Reflex Tester"
        # start = font.render(welcome_text, True, (255, 255, 255))
        # screen.blit(start, (int(SCREEN_WIDTH*0.1), int(SCREEN_HEIGHT*0.45)))
        show_text(welcome_text)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        pygame.display.flip()
    done = False
    while not done:
        keys = pygame.key.get_pressed()

        # drawing screen elements
        screen.blit(bg, (0, 0))
        screen.blit(colors[color], (0, 0))
        for event in pygame.event.get():
            if event == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if not freeze:
                    if (event.key == pygame.K_h and color == 0) or (event.key == pygame.K_j and color == 1) \
                            or (event.key == pygame.K_k and color == 2) or (event.key == pygame.K_l and color == 3):
                        color = random.randint(0, 3)
                        score += 1
                        mixer.music.load("beep-07a.mp3")
                        mixer.music.play()
                    else:
                        mixer.music.load("beep-10.mp3")
                        mixer.music.play()
                        freeze = True
                    screen.blit(bg, (0, 0))
                else:
                    mainloop()
        points = font.render(str(score).zfill(3), True, (255, 255, 255))
        screen.blit(score_overlay, (0, 0))
        screen.blit(points, (int(SCREEN_WIDTH * 0.4425), int(SCREEN_HEIGHT * 0.495)))
        if freeze:
            screen.blit(end, (0, 0))
        clock.tick(60)
        pygame.display.flip()
if __name__ == '__main__':
    mainloop()