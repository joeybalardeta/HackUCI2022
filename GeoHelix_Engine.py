import GeoHelixData
import time, pygame


# Global Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (3, 157, 252)
RED = (255, 54, 54)

class GeoHelix:
    def __init__(self):
        self.WIDTH = GeoHelixData.WIDTH
        self.HEIGHT = GeoHelixData.HEIGHT
        self.time_elapsed = 0
        self.delayHz = 120
        self.running = True
        pygame.init()
        pygame.font.init()
        self.renderer = Renderer(self)
        self.player = GeoHelixData.Player()
        self.physicsEngine = GeoHelixData.PhysicsEngine(self.player)
        self.obstacleGenerator = GeoHelixData.ObstacleGenerator()
        

        # Don't put anything after this, it won't run until the end of the program
        self.start()
              

    def start(self):
        try:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("GeoHelix - HackUCI 2022")
            self.game_loop()
        
        finally:
            pygame.quit()
    
    def game_loop(self):
        self.start_screen()
        while self.running:
            self.handle_events()
            self.renderer.render()
            self.physicsEngine.simulate()
            self.obstacleGenerator.obstacleConsider(self.time_elapsed)
            self.time_elapsed += 1
            self.difficulty_tweak()
            # print(len(GeoHelixData.Rectangle.Rects))
            time.sleep(1.0/self.delayHz)
        
        self.game_end()
            
    def handle_events(self):
        if (self.player.health < 1):
            self.game_stop()
            time.sleep(0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.swap_sides()


    def difficulty_tweak(self):
        newDiff = int(self.time_elapsed / 1000)
        if (newDiff > 2):
            GeoHelixData.RECT_MOVE_SPEED = newDiff

    def start_screen(self):
        self.screen.fill(BLACK)
        welcome = self.renderer.font.render("Welcome to GeoHelix!", False, BLUE)
        welcome2 = self.renderer.font.render("Don't touch the boxes!", False, RED)
        welcome3 = self.renderer.font.render("Press SPACE to switch sides!", False, WHITE)
        welcome_rect = welcome.get_rect(center = (GeoHelixData.WIDTH / 2, (GeoHelixData.HEIGHT / 2) - 25))
        welcome2_rect = welcome2.get_rect(center = (GeoHelixData.WIDTH / 2, GeoHelixData.HEIGHT / 2))
        welcome3_rect = welcome3.get_rect(center = (GeoHelixData.WIDTH / 2, (GeoHelixData.HEIGHT / 2) + 25))
        self.screen.blit(welcome, welcome_rect)
        self.screen.blit(welcome2, welcome2_rect)
        self.screen.blit(welcome3, welcome3_rect)
        pygame.display.flip()
        time.sleep(5)

    def game_stop(self):
        self.running = False
        

    def game_end(self):
        self.screen.fill(BLACK)
        gameOver = self.renderer.font.render("Game Over!", False, RED)
        score = self.renderer.font.render("Final Score: " + str(int(self.time_elapsed / 100)), False, WHITE)
        gameOver_rect = gameOver.get_rect(center = (GeoHelixData.WIDTH / 2, (GeoHelixData.HEIGHT / 2) - 25))
        score_rect = score.get_rect(center = (GeoHelixData.WIDTH / 2, GeoHelixData.HEIGHT / 2))
        self.screen.blit(gameOver, gameOver_rect)
        self.screen.blit(score, score_rect)
        pygame.display.flip()
        time.sleep(2)

class Renderer:
    def __init__(self, GeoHelixObject):
        # Get copy of GeoHelix object in memory
        self.GeoHelixGame = GeoHelixObject
        self.font = pygame.font.SysFont('Calibri', 18)


    # In charge of all display functions
    def render(self):
        # Draw all game objects
        self.GeoHelixGame.screen.fill(BLACK)
        self.draw_sidelines()
        self.draw_player()
        for rect in GeoHelixData.Rectangle.Rects:
            self.draw_rect(rect)
        
        self.draw_score()

        # Refresh display
        pygame.display.flip()


    def draw_score(self):
        score = self.font.render("Score: " + str(int(self.GeoHelixGame.time_elapsed / 100)), False, WHITE)
        speed = self.font.render("Speed: " + str(GeoHelixData.RECT_MOVE_SPEED), False, WHITE)
        self.GeoHelixGame.screen.blit(score, (15, 0))
        self.GeoHelixGame.screen.blit(speed, (15, 20))

    # Draw sidelines with "fade-to-gray" gradient
    def draw_sidelines(self):
        for i in range(10):
            pygame.draw.line(self.GeoHelixGame.screen, (255 - i * 20, 255 - i * 20, 255 - i * 20), (9 - i, 0),(9 - i, self.GeoHelixGame.HEIGHT))
            pygame.draw.line(self.GeoHelixGame.screen, (255 - i * 20, 255 - i * 20, 255 - i * 20), (self.GeoHelixGame.WIDTH - 10 + i, 0),(self.GeoHelixGame.WIDTH - 10 + i, self.GeoHelixGame.HEIGHT))

    def draw_rect(self, rect):
        rectangle = pygame.Rect(rect.x, rect.y, rect.w, rect.h)
        pygame.draw.rect(self.GeoHelixGame.screen, rect.color, rectangle, 1)


    def draw_player(self):
        for i in range(int(self.GeoHelixGame.player.w / 4)):
            rectangle = pygame.Rect(self.GeoHelixGame.player.x + (i * 2), self.GeoHelixGame.player.y + (i * 2), self.GeoHelixGame.player.w - (i * 4), self.GeoHelixGame.player.h - (i * 4))
            pygame.draw.rect(self.GeoHelixGame.screen, WHITE, rectangle, 1)


def main():
    GeoHelixGame = GeoHelix()
    


if __name__ == "__main__":
    main()
