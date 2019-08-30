from car_provider import CarProvider
from player import Player
from screen import Screen
import time

class Game:
    def __init__(self, player_names):
        car_provider = CarProvider()
        self.active_player_list = [Player(name, 0, car_provider.give_me_a_car(), 0.6) for name in player_names]
        max_car_len = max([player.car.max_len for player in self.active_player_list])
        max_name_len = max([len(name) for name in player_names])
        self.screen = Screen(max_name_len, max_car_len)
        # ordered list preserve place of competition
        self.finished_player_list = []


    def start(self):
        self.screen.start_screen(self.active_player_list)
        while True:
            for player in self.active_player_list:
                # try move a player if not finished yet
                if not player.finished():
                    player.move()
                if player.pos >= self.screen.columns:
                    player.finish()
                    self.finished_player_list.append(player)
            for finished_player in self.finished_player_list:
                # remove finished player from active player list.
                try:
                    self.active_player_list.remove(finished_player)
                except: ValueError
                pass

            self.screen.display(self.active_player_list, self.finished_player_list)
            self.win_message()
            if (self.all_finished()):
                return
            time.sleep(0.025)


    def win_message(self):
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
        for i in range(len(self.finished_player_list)):
            print ordinal(i+1) + " : " + self.finished_player_list[i].name

    def all_finished(self):
        return len(self.active_player_list) == 0