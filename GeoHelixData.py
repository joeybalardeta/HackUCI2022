from pygame import Rect
import random

WIDTH = 400
HEIGHT = 600
RECT_MOVE_SPEED = 2

class Rectangle:
    Rects = []

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
        Rectangle.Rects.append(self)

    def move(self, x, y):
        '''
        move rectangle by x and y coordinates
        '''

        self.x += x
        self.y += y


    def destroy(self):
        '''
        remove rectangle from list of all rectangles
        '''
        
        Rectangle.Rects.remove(self)

    def rectCheck():
        for rect in Rectangle.Rects:
            if (rect.y > HEIGHT):
                rect.destroy()

class Player:
    def __init__(self):
        self.w = 20
        self.h = 20
        self.x = 10
        self.y = 550
        self.health = 1


    def swap_sides(self):
        if (self.x == 10):
            self.x = WIDTH - 30
            return
        
        if (self.x == WIDTH - 30):
            self.x = 10
            return

    def collision_check(self):
        for rect in Rectangle.Rects:
            if ((self.x in range(rect.x, rect.x + rect.w)) or ((self.x + self.w) in range(rect.x, rect.x + rect.w))):
                if ((self.y in range(rect.y, rect.y + rect.h)) or ((self.y + self.h) in range(rect.y, rect.y + rect.h))):
                    self.health -= 1


class Obstacle:
    '''
    Form horizontal stacks of rectangles to create wall obstacles
    '''
    def __init__(self, height, side):
        self.height = height
        self.components = []
        for r in range(height):
            if (side % 2 == 0):
                rect = Rectangle((10 + (r * 20)), (-40), 20, 20)
                self.components.append(rect)
            
            else:
                rect = Rectangle((WIDTH - 30 - (r * 20)), (-40), 20, 20)
                self.components.append(rect)


class PhysicsEngine:
    '''
    Costantly move all rectangles (that are part of obstacle objects) downward
    '''
    def __init__(self, player):
        self.player = player
    
    def simulate(self):
        for rect in Rectangle.Rects:
            rect.move(0, RECT_MOVE_SPEED)
        
        Rectangle.rectCheck()
        self.player.collision_check()



class ObstacleGenerator():
    '''
    Randomly generate an Obstacle of random length based on game time
    '''
    def __init__(self):
        self.time_since_last_obstacle = 0
        self.last_obstacle_side = 1
    
    def obstacleConsider(self, game_time):
        self.time_since_last_obstacle += RECT_MOVE_SPEED
        if (game_time % 20 == 0):
            spawnChance = random.randint(100, 500)
            if (spawnChance < self.time_since_last_obstacle):
                self.spawnObstacle()


    def spawnObstacle(self):
        Obstacle(random.randint(2, 10), self.last_obstacle_side)
        self.time_since_last_obstacle = 0
        self.last_obstacle_side = (self.last_obstacle_side + 1) % 2
