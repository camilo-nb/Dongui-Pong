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

        self.image = pygame.image.load(image_file).convert_alpha()

        self.width, self.height = self.image.get_size()

        self.x = WIDTH / 2 - self.width / 2
        self.y = HEIGHT / 2 - self.height / 2

        self.delta_x = 2
        self.delta_y = 2
    
    @classmethod
    def tennis(cls):
        return cls("./resources/images/tennis_ball.png")
    
    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y

def main():

    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(CAPTION)

    tennis_ball = Ball.tennis()

    playing = True

    while playing:

        tennis_ball.move()

        window.fill(COLOURS["CLAY_COURT"])
        window.blit(tennis_ball.image, (tennis_ball.x, tennis_ball.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
        
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()