#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

class Ball:

    def __init__(self, a):
        self.pos = a
        self.vel = np.array([10, 10, 10, 0])
        self.acc = np.array([0, -5, 0, 0])

    @classmethod
    def tennis(cls):
        return cls(os.chdir("../resources/images/tennis_ball.png"))

    def bounce(self, floor):
        if self.pos[1] < floor:
            self.pos[1] = floor
            self.vel[1] *= -1
            
    
    def move(self):
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel
