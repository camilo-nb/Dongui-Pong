#!/usr/bin/python
# -*- coding: utf-8 -*-

# VSCODE TEST
# TEST 2

import pygame

import numpy as np

from data.rotation import *

from data.ball import *
from data.tenniscourt import *

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
    "TENNIS_BALL_GREEN" : (201, 243, 100),
    "CLAY" : (173, 80, 73),
    "CLAY_COURT" : (169,115,93),
    "WHITE" : (255, 255, 255),
    "BLACK" : (0, 0, 0),
    "LIGHT_SKY_BLUE" : (153, 204, 255),
    "TENNIS_COURT_GREEN" : (113, 142, 50)
}

ANGLES = np.array([0, 0, 0])
PHI = 0
SCALE = 1
SPEED = np.array([0, 0, 0])
NEAR = 250 # distance between viewer (origin) and screen
FAR = 10000000
FLOOR = -200
SHIFT = 100
POS = np.array([WIDTH // 2, (HEIGHT- FLOOR) // 2 ])

def connect_points(window, color, vertices, lines):
    for j in range(len(lines)):
        for i in range(len(lines[j])):
            if lines[j][i] == 1:
                pygame.draw.line(window, color, vertices[j], vertices[i])

def fill_area(window, color, vertices, area):
    points = []
    for i in range(len(area)):
        if area[i] == 1:
            points.append(vertices[i])
    points.append(points.pop(-2))
    pygame.draw.polygon(window, color, points)


def main():
    global ANGLES

    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(CAPTION)

    running = True

    font = pygame.font.Font(None, 60)

    tennis_court = TennisCourt.ITP_singles(cls=TennisCourt, FLOOR=FLOOR, NEAR=NEAR, SHIFT=SHIFT)
    tennis_ball = Ball([0, FLOOR + 100, NEAR + SHIFT + tennis_court.length, 1])

    while running:

        window.fill(COLORS["TENNIS_COURT_GREEN"])
        XD = [(HEIGHT/2, -WIDTH/2), (HEIGHT/2, WIDTH/2), (0, WIDTH/2), (0, -WIDTH/2)]
        pygame.draw.polygon(window, COLORS["LIGHT_SKY_BLUE"], [(0, 0), (WIDTH, 0), (WIDTH, HEIGHT/2), (0, HEIGHT/2)])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ####################
        ### TENNIS COURT ### 
        index = 0
        projected_points = [j for j in range(len(tennis_court.vertices))]

        for vertex in tennis_court.vertices:
            #rotated_3D = cartesian_rotation(vertex[:3], *ANGLES)
            #rotated_4D = np.append(rotated_3D, [1])
            #projected_2D = perspective_projection(rotated_4D, NEAR, FAR, FOV = np.pi/2)
            projected_2D = perspective_projection(vertex, NEAR, FAR, FOV = np.pi/2)
            x = int(projected_2D[0] * SCALE) + POS[0]
            y = int(projected_2D[1] * SCALE) + POS[1]
            projected_points[index] = [x, y]
            pygame.draw.circle(
                window, # surface
                COLORS["WHITE"] if vertex[2] < FAR else COLORS["CLAY_COURT"], # color
                (x, y), # center
                1 # radius
            )
            index += 1

        fill_area(window, COLORS["CLAY_COURT"], projected_points, tennis_court.area)
        connect_points(window, COLORS["WHITE"], projected_points, tennis_court.lines)
        ### TENNIS COURT ###
        ####################

        ###################
        ### TENNIS BALL ### 
        tennis_ball.move()
        tennis_ball.sideline_bounce((tennis_court.doubles_width, tennis_court.length), NEAR, SHIFT)

        projected_2D = perspective_projection(tennis_ball.pos, NEAR, FAR, FOV = np.pi/2)
        x = int(projected_2D[0] * SCALE) + POS[0]
        y = int(projected_2D[1] * SCALE) + POS[1]
        pygame.draw.circle(
            window, # surface
            COLORS["TENNIS_BALL_GREEN"] if vertex[2] < FAR else COLORS["CLAY_COURT"], # color
            (x, y), # center
            5 # radius
        )
        # tennis_ball.bounce(FLOOR)
        if tennis_ball.bounce(FLOOR):
            pygame.draw.circle(
                window, # surface
                COLORS["RED"], # color
                (x, y), # center
                5 # radius
            )

        text = f"x, y, z: {tennis_ball.pos[:3]}"
        sign = font.render(text, False, COLORS["WHITE"])
        window.blit(sign, (WIDTH / 2 - font.size(text)[0] / 2, 50))
        ### TENNIS BALL ### 
        ###################

        ANGLES = ANGLES + SPEED

        #pygame.display.update()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()