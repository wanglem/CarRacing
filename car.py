class Car:
    def __init__(self, car_arr):
        self.car_arr = car_arr;
        self.max_len = max([len(line) for line in car_arr])