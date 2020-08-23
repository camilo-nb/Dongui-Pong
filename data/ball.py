#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

class Ball:

    def __init__(self, a):
        self.pos = a
        self.vel = np.array([10, 0, 10, 0])
        self.acc = np.array([0, -1, 0, 0])

    @classmethod
    def tennis(cls):
        return cls(os.chdir("../resources/images/tennis_ball.png"))

    def bounce(self, floor):
        if self.pos[1] < floor:
            self.pos[1] = floor
            self.vel[1] *= -1
            return True
        else:
            return False
            
    def sideline_bounce(self, SIZE, NEAR, SHIFT):
        if abs(self.pos[0]) > SIZE[0] / 2:
            self.pos[0] = SIZE[0] / 2 * np.sign(self.pos[0])
            self.vel[0] *= -1
        if self.pos[2] > SIZE[1] + NEAR + SHIFT:
            self.pos[2] = SIZE[1] + NEAR + SHIFT
            self.vel[2] *= -1
        elif self.pos[2] < NEAR + SHIFT:
            self.pos[2] = NEAR + SHIFT
            self.vel[2] *= -1

    def move(self):
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel