import numpy as np


class Rotation:
    def __init__(self, y_angle=0):
        # angle around y axis
        self.angle = y_angle

    def __matmul__(self, other: np.array):
        return self.matrix() @ other

    def transpose(self):
        return self.matrix().T

    def matrix(self):
        return np.array([[np.cos(self.angle), 0, np.sin(self.angle)],
                         [0, 1, 0],
                         [-np.sin(self.angle), 0,  np.cos(self.angle)]])

    def turn(self, angle):
        self.angle += angle


class Position:
    def __init__(self, points: np.array, num_points: int = 8, wdh=None):
        self.num_points = num_points
        points = np.array(points)
        if wdh is None:  # use points as input for num_points values
            assert points.shape == (num_points, 3)
            self.points = points
        else:
            wdh = np.array(wdh)
            points.reshape((1, 3))
            wdh.reshape((1, 3))
            assert num_points == 8

            #       011 --------- 111
            #     /  |           / |
            #  001 --+------- 101  |
            #   |    |         |   |
            #   |   010  ------|-110
            #   |  /           | /
            #  000   -------  100
            self.points = np.empty((num_points, 3))
            for i in range(num_points):
                bit_list = np.array([i & 1 << j != 0 for j in range(3)])  # split into bits, e.g. 5 =[1,0,1]
                self.points[i, :] = points + wdh/2 * (2 * bit_list - 1)

    def move(self, vec: np.array):
        vec = np.array(vec).reshape(1,3)
        self.points += np.repeat(vec, self.num_points, axis=0)

    def rotate(self, rot: Rotation):
        self.points = self.points @ rot.transpose()  # TODO: should rot be inverted here?

    def __neg__(self):
        return -1 * np.copy(self.points)
