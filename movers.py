from movables import Position, Rotation
from abc import ABC, abstractmethod
import numpy as np


class Mover(ABC):
    @abstractmethod
    def move(self,  pos_ref: Position, rot_ref: Rotation):
        pass


class Still(Mover):
    def move(self, pos_ref: Position, rot_ref: Rotation):
        # doesn't change Position or Rotation
        pass


class ConstVel(Mover):
    def __init__(self, vel):
        self.vel = vel

    def move(self,  pos_ref: Position, rot_ref: Rotation):
        pos_ref.move(self.vel)


class ConstAcc(Mover):
    def __init__(self, acc_const: list, vel_init: list):
        self.vel = np.array(vel_init)
        self.acc = np.array(acc_const)

    def move(self,  pos_ref: Position, rot_ref: Rotation):
        pos_ref.move(self.vel)
        self.vel += self.acc


class ConstTurn(Mover):
    def __init__(self, vel: float, ang_vel: float):
        self.vel = vel
        self.ang_vel = ang_vel

    def move(self,  pos_ref: Position, rot_ref: Rotation):
        direction = np.array([np.sin(rot_ref.angle), 0, np.cos(rot_ref.angle)])
        pos_ref.move(direction * self.vel)
        rot_ref.turn(self.ang_vel)