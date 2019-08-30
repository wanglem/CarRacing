import random

class Player:
    def __init__(self, name, pos, car, roll):
        self.name = name
        self.pos = pos
        self.car = car
        self.roll = roll
        self._finished = False

    def move(self):
        prob = random.random()
        if (self.roll >= prob):
            self.pos += 1

    def finish(self):
        self._finished = True

    def finished(self):
        return self._finished