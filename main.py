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
SCALE = -1
SPEED = np.array([0.001, 0, 0.001])
NEAR = 100 # distance between viewer (origin) and screen
FAR = 10000
POS = np.array([WIDTH // 2, HEIGHT // 2])

TENNIS_COURT = np.array(
    [
        [-823 / 2 , -100, NEAR + 2377 / 2, 1],
        [823 / 2, -100, NEAR + 2377 / 2, 1],
        [823 / 2, -100, NEAR - 2377 / 2, 1],
        [-823 / 2, -100, NEAR - 2377 / 2, 1]
    ]
)

def main():
    global ANGLES

    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(CAPTION)

    running = True

    while running:
        
        window.fill(COLORS["CLAY_COURT"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        index = 0
        projected_points = [j for j in range(len(TENNIS_COURT))]

        for point in TENNIS_COURT:
            projected_2D = perspective_projection(point, NEAR, FAR, FOV = np.pi/6)
            x = int(projected_2D[0] * SCALE) + POS[0]
            y = int(projected_2D[1] * SCALE) + POS[1]
            projected_points[index] = [x, y]
            pygame.draw.circle(
                window, # surface
                COLORS["TENNIS_GREEN"], # color
                (x, y), # center
                5 # radius
            )
            index += 1
        pygame.draw.line(window, COLORS["WHITE"], projected_points[0], projected_points[1])
        pygame.draw.line(window, COLORS["WHITE"], projected_points[1], projected_points[3])
        pygame.draw.line(window, COLORS["WHITE"], projected_points[2], projected_points[3])
        pygame.draw.line(window, COLORS["WHITE"], projected_points[2], projected_points[0])

        pygame.display.update()
        # break
        #pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()