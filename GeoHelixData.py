class Rectangle:
    Rects = []

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
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