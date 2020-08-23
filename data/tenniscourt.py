import numpy as np

class TennisCourt:
    
    def __init__(self, length, singles_width, doubles_width, service_line_length, net_height, net_post_width, FLOOR, NEAR, SHIFT):
        self.length = length
        self.singles_width = singles_width
        self.doubles_width = doubles_width
        self.service_line_length = service_line_length
        self.net_height = net_height
        self.net_post_width = net_post_width
        self.FLOOR = FLOOR
        self.NEAR = NEAR
        self.SHIFT = SHIFT

        self.vertices = np.array(
            [
                #
                [-self.doubles_width / 2 , self.FLOOR, self.NEAR + self.SHIFT + self.length, 1],
                [-self.singles_width / 2 , self.FLOOR, self.NEAR + self.SHIFT + self.length, 1],
                [self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length, 1],
                [self.doubles_width / 2 , self.FLOOR, self.NEAR + self.SHIFT + self.length, 1],
                #
                [-self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2 + self.service_line_length, 1],
                [0, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2 + self.service_line_length, 1],
                [self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2 + self.service_line_length, 1],
                #
                [-self.doubles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2, 1],
                [-self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2, 1],
                [0, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2, 1],
                [self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2, 1],
                [self.doubles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2, 1],
                #
                [-self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2 - self.service_line_length, 1],
                [0, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2 - self.service_line_length, 1],
                [self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT + self.length / 2 - self.service_line_length, 1],
                #
                [-self.doubles_width / 2 , self.FLOOR, self.NEAR + self.SHIFT, 1],
                [-self.singles_width / 2 , self.FLOOR, self.NEAR + self.SHIFT, 1],
                [self.singles_width / 2, self.FLOOR, self.NEAR + self.SHIFT, 1],
                [self.doubles_width / 2 , self.FLOOR, self.NEAR + self.SHIFT, 1],
            ]
        )

        self.lines = np.array(
            [
               #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]#
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#1
                [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#2
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],#3
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#4
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],#5
                [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#6
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],#7
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],#8
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#9
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],#0
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],#1
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],#2
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],#3
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],#4
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],#5
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],#6
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],#7
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]# 8
            ]
        )

        self.area = np.array(
               #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]#
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
        )
    
    @staticmethod
    def ITP_singles(cls, FLOOR, NEAR, SHIFT):
        """https://en.wikipedia.org/wiki/Tennis_court#Dimensions"""
        return cls(
            length=2377,
            singles_width=823,
            doubles_width=1097,
            service_line_length=640,
            net_height=107,
            net_post_width=91,
            FLOOR=FLOOR,
            NEAR=NEAR,
            SHIFT=SHIFT
        )