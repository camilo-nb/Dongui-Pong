import pygame

from pygame.locals import QUIT

WIDTH = 800
HEIGHT = 600
WINDOW_SIZE = (WIDTH, HEIGHT)

FPS = 30
CAPTION = "Dongui-Pong"

COLOURS = {
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255),
    "TENNIS_GREEN" : (201, 243, 100),
    "CLAY" : (173, 80, 73),
    "CLAY_COURT" : (169,115,93)
}

class Ball:

    def __init__(self, image_file):

        self.true_image = pygame.image.load(image_file).convert_alpha()

        self.image = pygame.image.load(image_file).convert_alpha()

        self.width, self.height = self.image.get_size()

        self.x = WIDTH / 2 - self.width / 2
        self.y = HEIGHT / 2 - self.height / 2

        self.delta_x = 0
        self.delta_y = 0
    
    @classmethod
    def tennis(cls):
        return cls("./resources/images/tennis_ball.png")
    
    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y

    def sideline_bounce(self):
        if self.x <= 0:
            self.delta_x = -self.delta_x
        if self.x + self.width >= WIDTH:
            self.delta_x = -self.delta_x
        if self.y <= 0:
            self.delta_y = -self.delta_y
        if self.y + self.height >= HEIGHT:
            self.delta_y = -self.delta_y

    def move_to(self, x1, y1):
        self.x = x1
        self.y = y1

    def resize(self, h, w):
        self.image = pygame.transform.scale(self.true_image, (h, w))

x_c = WIDTH / 2
y_c = HEIGHT / 2
z_c = 1200

def main():

    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(CAPTION)

    tennis_ball = Ball.tennis()

    playing = True

    i = 0
    while playing:
        i += 1
        tennis_ball.move()
        tennis_ball.sideline_bounce()
        # tennis_ball.resize(32, 32)
        # tennis_ball.move_to(10, 10 * (i % 2))

        window.fill(COLOURS["CLAY_COURT"])
        window.blit(tennis_ball.image, (tennis_ball.x, tennis_ball.y))

        for event in pygame.event.get():
            
            if event.type == QUIT:
                playing = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    tennis_ball.delta_x = -5
                if event.key == pygame.K_d:
                    tennis_ball.delta_x = 5
                if event.key == pygame.K_w:
                    tennis_ball.delta_y = -5
                if event.key == pygame.K_s:
                    tennis_ball.delta_y = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    tennis_ball.delta_x = 0
                if event.key == pygame.K_d:
                    tennis_ball.delta_x = 0
                if event.key == pygame.K_w:
                    tennis_ball.delta_y = 0
                if event.key == pygame.K_s:
                    tennis_ball.delta_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()