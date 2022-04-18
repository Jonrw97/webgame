from gothonweb.games import gothons
from gothonweb.planisphere import *
class Player(object):

    def __init__(self, player_name, game_name):
        self.player_name = player_name
        self.game_name = game_name
        self.game_count = 0
        self.reset_current_game()

    def get_current_game_room(self):
        return self.current_game_room

    def save_current_room(self, room):
        self.current_game_room = room

    def reset_current_game(self,game_name):
        self.current_game = game_name
        self.game_count += 1
        self.current_game_room = get_start_room(gothons.START)

players = {

}

def get_or_create_player(player_name):
    if player_name in players:
        return players[player_name]

    players[player_name] = Player(player_name)
    return players[player_name]

#def get_current_game(game_name):
