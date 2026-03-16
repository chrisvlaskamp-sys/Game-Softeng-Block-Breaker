import pygame
import paddle 
import ball
"""
Part of the code in this file has been adapted from the game_state.py example code. 
"""


class Game_State:

    def __init__(self, world_size):
        """Initiates a game with players and a playing field of size world_size, """
        self.world_size = world_size
        self.players = {} # dictionary of players 
        self.balls = {} # dictionary of balls
        self.units = [] # list containing all balls and players


    def __repr__(self):
        """Represents the game_state as a string containing world size and each player"""
        return f"world_size: {self.world_size}\nunits: {self.units}"



    def update(self, action):
        """Updates the game state with action"""
        name = action.get_name()
        if not name in self.players: 
            player = Paddle(screen, position_strategy, border_strategy, color=(255, 0, 0))
            player = Player(self.world_size, name) # create a new player
            self.units.append(player)              # add to units
            self.players[name] = player            # add to players too for fast lookup by name 
            
        player = self.players[name]
        player.step()
        player.stay_on_screen(self.world_size) 


    def draw(self, name, surface, name_textures):
        rect = pygame.Rect(pygame.Vector2(0, 0), self.world_size)
        white = (255, 255, 255)
        pygame.draw.rect(surface, white, rect, 2)
        for unit in self.units:
            unit.plot(surface)
