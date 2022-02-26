import pygame
import time

# Global Variables
REFRESH_RATE = 240
RUNNING = True
WIDTH, HEIGHT = 600, 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RECTS = []
MOVE_SPEED = 1
FRAME = 0


# Rectangle Class
class Rectangle:

    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        RECTS.append(self)

    def move(self, x, y):
        self.x += x
        self.y += y

    def self_check(self):
        if (self.y > HEIGHT):
            RECTS.remove(self)

    def destroy(self):
        RECTS.remove(self)



def spawn_obstacle(height, side):
    if (side % 2 == 0):
        for i in range(height):
            rect = Rectangle(11 + (i * 20), -40, 20, 20)

    else:
        for i in range(height):
            rect = Rectangle(WIDTH - 30 - (i * 20), -40, 20, 20)


# Global Functions
def draw(screen):
    screen.fill(BLACK)
    draw_sides(screen)
    for rect in RECTS:
        rectangle = pygame.Rect(rect.x, rect.y, rect.w, rect.h)
        pygame.draw.rect(screen, WHITE, rectangle, 1)


def physX():
    for rect in RECTS:
        rect.move(0, MOVE_SPEED)
        rect.self_check()

def draw_sides(screen):
    for i in range(5):
        pygame.draw.line(screen, WHITE,(10 - i, 0),(10 - i, HEIGHT))
        pygame.draw.line(screen, WHITE,(WIDTH - 11 + i, 0),(WIDTH - 11 + i, HEIGHT))

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#init pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))         
spawn_obstacle(8, 0)

#main game loop
while RUNNING:
    event_handler()
    draw(screen)
    physX()
    pygame.display.flip()
    FRAME += 1
    # print("Frame number:", FRAME)
    time.sleep(1.0/REFRESH_RATE)
    
