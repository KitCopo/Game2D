from Math.vector import *
from Config.constats import *

class Camera: 
    def __init__(self) -> None:
        self.offset: Vector2 = Vector2()

    def move(self, directions: str) -> None:
        if "up" in directions:
            self.offset.y += Velocity
        if "down" in directions:
            self.offset.y -= Velocity
        if "left" in directions:
            self.offset.x += Velocity
        if "right" in directions:
            self.offset.x -= Velocity