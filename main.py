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
    "CLAY_COURT" : (169,115,93),
    "WHITE" : (255, 255, 255)
}

cancha = [WIDTH / 2, HEIGHT / 2, 2400 / 2]

class Ball:

    def __init__(self, image_file):

        self.true_image = pygame.image.load(image_file).convert_alpha()

        self.image = pygame.image.load(image_file).convert_alpha()

        
        self.true_width, self.true_height = self.true_image.get_size()
        self.width, self.height = self.image.get_size()

        
        #propiedades fisicas x, y, z 
        self.pos = [10, 10, 10]
        self.dim = [5, 5, 5]
        self.vel = [20, 10, 10]
        self.acc = [0, -3, 0]
    
    @classmethod
    def tennis(cls):
        return cls("./resources/images/tennis_ball.png")
    
    def move(self):
        for i in [0, 1, 2]:
            self.vel[i] += self.acc[i]
        for i in [0, 1, 2]:
            self.pos[i] += self.vel[i]

    def sideline_bounce(self):
        for i in [0, 1, 2]:
            if self.pos[i] <= -cancha[i]:
                self.vel[i] *= -1
                self.pos[i] = - cancha[i]

            if self.pos[i] + self.dim[i] >= cancha[i]:
                self.vel[i] *= -1

    def print_pos(self, x1, y1):
        self.x = x1
        self.y = y1

    def resize(self, h, w):
        self.image = pygame.transform.scale(self.true_image, (h, w))
        self.width, self.height = self.image.get_size()

def main():

    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(CAPTION)

    tennis_ball = Ball.tennis()

    playing = True

    font = pygame.font.Font(None, 60)
    
    while playing:
        tennis_ball.move()
        tennis_ball.sideline_bounce()

        x, y, z = tennis_ball.pos

        #def ajuste()
        
        tennis_ball.print_pos(z / (cancha[2] + z) * x + 300, HEIGHT - z / (cancha[2] + z) * y - 300)
        
        tennis_ball.resize(int(tennis_ball.true_width * z / (cancha[2] + z)), int(z / (cancha[2] + z) * tennis_ball.true_height))
        
        window.fill(COLOURS["CLAY_COURT"])
        window.blit(tennis_ball.image, (tennis_ball.x, tennis_ball.y))

        for i in [-cancha[0], cancha[0]]:
            for j in [-cancha[1], cancha[1]]:
                for k in [0, cancha[2]]:
                    tennis_ball.print_pos(k / (cancha[2] + k) * i + 300, HEIGHT - k / (cancha[2] + k) * j - 300)
                    tennis_ball.resize(int(tennis_ball.true_width * k / (cancha[2] + k)), int(k / (cancha[2] + k) * tennis_ball.true_height))
                    window.blit(tennis_ball.image, (tennis_ball.x, tennis_ball.y))

        text = "x, y, z: {b.pos[0]}, {b.pos[1]}, {b.pos[2]}".format(b=tennis_ball)
        sign = font.render(text, False, COLOURS["WHITE"])
        window.blit(sign, (WIDTH / 2 - font.size(text)[0] / 2, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
        
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()