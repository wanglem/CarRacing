from game import Game
def load_players():
    return [line.rstrip('\n') for line in open("players.txt")]

def main():
    player_names = load_players()
    game = Game(player_names)
    game.start()

main()