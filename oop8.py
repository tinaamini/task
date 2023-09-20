# ارث بری __________________________________
class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color


class Cars(Vehicle):
    def __init__(self, speed, color, engine, wheels, window):
        super().__init__(speed, color)
        self.engine = engine
        self.wheels = wheels
        self.window = window


class Bicycle(Vehicle):
    def __init__(self, speed, color, chair, pedal):
        super().__init__(speed, color)
        self.chair = chair
        self.pedal = pedal