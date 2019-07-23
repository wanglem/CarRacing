from car_provider import CarProvider
from player import Player
from screen import Screen
import time

class Game:
    def __init__(self, player_names):
        car_provider = CarProvider()
        self.player_list = [Player(name, 0, car_provider.give_me_a_car(), 0.6) for name in player_names]
        max_car_len = max([player.car.max_len for player in self.player_list])
        max_name_len = max([len(name) for name in player_names])
        self.screen = Screen(max_name_len, max_car_len)


    def start(self):
        self.screen.start_screen(self.player_list)
        while True:
            for player in self.player_list:
                player.move()
                if player.pos >= self.screen.columns:
                    self.win_message(player)
                    return
            self.screen.display(self.player_list)
            time.sleep(0.03)


    def win_message(self, player):
        print player.name + " is the winner!"