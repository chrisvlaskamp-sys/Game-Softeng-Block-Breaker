import pygame

"""
Part of the code in this file has been adapted from the game_state.py example code. 
"""


class Game_State:

    def __init__(self, world_size):
        """Initiates a game with players and a playing field of size world_size, """
        self.world_size = world_size
        self.players = {}
        self.units = []

    def __repr__(self):
        """Represents the game_state as a string containing world size and each player"""
        return f"world_size: {self.world_size}\nunits: {self.units}"



    def update(self, action):
        """Updates the game state with action"""
        name = action.get_name()
        if not name in self.players: 
            player = Player(self.world_size, name) # create a new player
            self.units.append(player)              # add to units
            self.players[name] = player            # add to players too for fast lookup by name 
            
        player = self.players[name]
        player.accelerate(action.get_acceleration())
        player.step()
        player.stay_on_screen(self.world_size) 