#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

import numpy as np

from data.rotation import *
from data.ball import *

# ancho, alto, profundidad
BOX = np.array(
    [823, 3000, 2377]
)

WIDTH = 800
HEIGHT = 600
WINDOW_SIZE = (WIDTH, HEIGHT)

FPS = 30
CAPTION = "Dongui-Pong"

COLORS = {
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255),
    "TENNIS_GREEN" : (201, 243, 100),
    "CLAY" : (173, 80, 73),
    "CLAY_COURT" : (169,115,93),
    "WHITE" : (255, 255, 255)
}

ANGLES = np.array([0, 0, 0])
PHI = 0
SCALE = 1
SPEED = np.array([0, 0, 0])
NEAR = 500 # distance between viewer (origin) and screen
FAR = 10000000
DELTA = -200
POS = np.array([WIDTH // 2, (HEIGHT- DELTA) // 2 ])

TENNIS_COURT = np.array(
    [
        [-823 / 2 , DELTA, NEAR + 100 + 2377, 1],
        [823 / 2, DELTA, NEAR + 100 + 2377, 1],
        [823 / 2, DELTA, NEAR + 100, 1],
        [-823 / 2, DELTA, NEAR + 100, 1],
        [0, 0, 0, 0]
    ]
)

def main():
    global ANGLES

    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(CAPTION)

    running = True

    font = pygame.font.Font(None, 60)

    pelota = Ball([200, DELTA + 500, NEAR + 100 + 2377 / 3, 1])
    
    while running:
        #DELTA = i

        pelota.move()
        pelota.bounce(DELTA)

        TENNIS_COURT[4] = pelota.pos
        
    
        window.fill(COLORS["CLAY_COURT"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        index = 0
        projected_points = [j for j in range(len(TENNIS_COURT))]

        for point in TENNIS_COURT:
            rotated_3D = cartesian_rotation(point[:3], *ANGLES)
            rotated_4D = np.append(rotated_3D, [1])
            projected_2D = perspective_projection(rotated_4D, NEAR, FAR, FOV = np.pi/2)
            #projected_2D = perspective_projection(point, NEAR, FAR, FOV = np.pi/2)
            x = int(projected_2D[0] * SCALE) + POS[0]
            y = int(projected_2D[1] * SCALE) + POS[1]
            projected_points[index] = [x, y]
            pygame.draw.circle(
                window, # surface
                COLORS["TENNIS_GREEN"] if point[2] < FAR else COLORS["CLAY_COURT"], # color
                (x, y), # center
                5 # radius
            )
            index += 1
        pygame.draw.line(window, COLORS["WHITE"], projected_points[0], projected_points[1])
        pygame.draw.line(window, COLORS["WHITE"], projected_points[1], projected_points[2])
        pygame.draw.line(window, COLORS["WHITE"], projected_points[2], projected_points[3])
        pygame.draw.line(window, COLORS["WHITE"], projected_points[3], projected_points[0])

        text = f"FAR, {FAR}"
        sign = font.render(text, False, COLORS["WHITE"])
        window.blit(sign, (WIDTH / 2 - font.size(text)[0] / 2, 50))

        ANGLES = ANGLES + SPEED
        pygame.display.update()

        #pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
