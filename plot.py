import matplotlib.pyplot as plt
import numpy as np
from movables import Camera, Obj


def plot(obj_list: list, camera: Camera, show=False):
    # fig, ax = plt.subplots()

    # 8 points binary coded, 000 should be the left bottom front corner
    # connect two points with a binary difference of 1
    for obj in obj_list:
        uv, z = camera.project(obj.position)
        edges = [(0b000, 0b001), (0b000, 0b010), (0b000, 0b100), (0b001, 0b011), (0b001, 0b101),
                 (0b010, 0b011), (0b010, 0b110), (0b011, 0b111), (0b100, 0b101), (0b100, 0b110),
                 (0b101, 0b111), (0b110, 0b111)]
        for p, p2 in edges:
            if z[p] > 0 and z[p2] > 0:
                plt.plot(uv[[p, p2], 0], uv[[p, p2], 1], obj.color+"-", lw=2)
    if show:
        plt.show()
