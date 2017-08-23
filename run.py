from movables import Camera, Position, Rotation, Obj
from movers import Still, ConstVel, ConstTurn
import plot
import numpy as np

camera = Camera(Position([[0, 0, 0]], 1), Rotation(), Still())
obj1 = Obj(Position([1, 1, 1], 8, [0.1, 0.1, 0.1]), ConstVel([-1, 0, 0]))
obj2 = Obj(Position([-1, -1, 1], wdh=[0.2, .2, .2]), ConstTurn(1, 0.4))

for i in range(10):
    plot.plot([obj1, obj2], camera, True)
    camera.move()
    obj1.move()
    obj2.move()