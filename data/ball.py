#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

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
        return cls(os.chdir("../resources/images/tennis_ball.png"))

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y