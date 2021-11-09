


class Agent:
    def __init__(self, type, position, orientation, speed, size=10):
        self.type = type
        self.position = position
        self.orientation = orientation
        self.size = size
        self.speed = speed
        self.action = None
        self.motor_output = [0, 0, 0]
        self.food_eaten = 0

    def process_observation(self):
        """Implements an action vector, with three elements:"""
        """(1) forward/backward"""
        """(2) left/right"""
        """(3) orientation"""
        self.motor_output = [5, 1, 2]
