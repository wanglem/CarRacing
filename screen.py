import os
import time
import subprocess as sp

class Screen:
    def __init__(self, max_name_len, max_car_len):
        rows, self.columns = os.popen('stty size', 'r').read().split()
        self.max_name_len = max_name_len
        self.max_car_len = max_car_len
        # extra `-1` is for the `:` after player's name
        self.columns = int(self.columns) - max_car_len - self.max_name_len - 3

    def display(self, active_player_list, finished_player_list):
        player_list_sorted = sorted(active_player_list, key=lambda p: -1 * p.pos)
        self.clear()
        for finished_player in finished_player_list:
            self._print_player(finished_player)
        for player in player_list_sorted:
            self._print_player(player)

    def _print_player(self, player):
        for car_line_index in range(len(player.car.car_arr)):
            padding = ""
            if (car_line_index == len(player.car.car_arr) - 1):
                # last line, print  name and `dot` padding
                padding += self.player_name_print_str(player.name) # name padding
                padding += "." * (self.max_car_len - player.car.max_len) # car length, pad "." last row
                padding += "." * player.pos # travel distance padding "." last row
            else:
                padding += " " * len(self.player_name_print_str(player.name)) # only last row pad name, else white space
                padding += " " * (self.max_car_len - player.car.max_len) # car length, pad " " other rows
                padding += " " * player.pos # travel distance pad  " " other rows
            print padding, # print padding
            print player.car.car_arr[car_line_index], # print that line of car
            print "" # print new line
        print "" # extra line between to players

    def start_screen(self, player_list):
        self.clear()
        self.display(player_list, [])
        print "Start In...."
        print "3"
        time.sleep(1.5)
        print "2"
        time.sleep(1.5)
        print "1"
        time.sleep(1.5)

    def player_name_print_str(self, name):
        pad_len = self.max_name_len - len(name)
        return name + " "*pad_len + ":"

    def clear(self):
        sp.call('clear',shell=True)
