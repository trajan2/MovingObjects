from abc import ABC
import copy

from states import Position, Rotation
from movers import Mover


class Movable(ABC):
    def __init__(self, pos: Position, rot: Rotation, mov: Mover):
        self.position = pos
        self.rotation = rot
        self.mover = mov

    def move(self):
        self.mover.move(self.position, self.rotation)


class Camera(Movable):
    def __init__(self, pos: Position, rot: Rotation, mov: Mover, focal: int = 1):
        assert pos.num_points == 1
        super().__init__(pos, rot, mov)
        self.focal = focal

    def project(self, pos_ref: Position):
        # translate and rotate to camera coordinates
        pos_c = copy.deepcopy(pos_ref)
        pos_c.move(-self.position)
        pos_c.rotate(self.rotation)

        # project to camera plane, (only 2 dimensions, depth (in z) is lost)
        uv = self.focal * pos_c.points[:, :2] / pos_c.points[:, 2].reshape((pos_c.num_points, 1))

        return uv, pos_c.points[:, 2]


class Obj(Movable):
    def __init__(self, pos: Position, mov: Mover, rot: Rotation = None, color: str = "k"):
        if rot is None:
            rot = Rotation()
        super().__init__(pos, rot, mov)
        self.color = color

