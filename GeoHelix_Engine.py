from sre_parse import WHITESPACE
import GeoHelixData
import time, pygame


# Global Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class GeoHelix:
    def __init__(self):
        self.WIDTH = 400
        self.HEIGHT = 600
        self.time_elapsed = 0
        self.running = True
        self.renderer = Renderer(self)

        # Don't put anything after this, it won't run until the end of the program
        self.start()
        
        

    def start(self):
        pygame.init()
        try:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            self.game_loop()
        
        finally:
            pygame.quit()
    
    def game_loop(self):
        while self.running:
            self.events()
            self.renderer.render()
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()

    def _end_game(self):
        self.running = False


class Renderer:
    def __init__(self, GeoHelixObject):
        # Get copy of GeoHelix object in memory
        self.GeoHelixGame = GeoHelixObject


    # In charge of all display functions
    def render(self):
        # Draw all game objects
        self.draw_sidelines()
        self.draw_rect()
        self.draw_player()

        # Refresh display
        pygame.display.flip()


    # Draw sidelines with "fade-to-gray" gradient
    def draw_sidelines(self):
        for i in range(10):
            pygame.draw.line(self.GeoHelixGame.screen, (255 - i * 20, 255 - i * 20, 255 - i * 20), (10 - i, 0),(10 - i, self.GeoHelixGame.HEIGHT))
            pygame.draw.line(self.GeoHelixGame.screen, (255 - i * 20, 255 - i * 20, 255 - i * 20), (self.GeoHelixGame.WIDTH - 11 + i, 0),(self.GeoHelixGame.WIDTH - 11 + i, self.GeoHelixGame.HEIGHT))

    def draw_rect():
        pass


    def draw_player():
        pass


def main():
    GeoHelixGame = GeoHelix()
    


if __name__ == "__main__":
    main()
