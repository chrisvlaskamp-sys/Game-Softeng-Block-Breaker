import pygame
import random 

from ball import Ball, Position_Center_Start, Border_Bounce 
from paddle import Paddle, Position_Start, Border_Stop
from bricks import NormalBlock, HardBlock, PowerUpBlock

"""
Part of the code in this file has been adapted from the game_state.py example code. 
"""


class Game_State:

    def __init__(self, world_size):
        self.world_size = world_size
        self.started = False 
        self.players = {} # dictionary of players/paddles with name as key
        self.paddles = [] # list of players/paddles 
        self.balls = [] # list of balls, 
        self.bricks = [] # list of bricks 
        self.units = []
        
    def start_game(self):
        """starts a game with players and a playing field of size world_size, """
        self.started = True 
        self.balls = [Ball(self.world_size, Position_Center_Start(), Border_Bounce())] # starting with one ball

        #Initiate bricks: 
        self.bricks = []
        for row in range(5):
            for col in range(10):
                x = col * 75 + 50
                y = row * 35 + 50
                if row == 0:
                    self.bricks.append(HardBlock(x, y)) #3
                elif row == 4:
                    self.bricks.append(PowerUpBlock(x, y)) #power
                else:
                    self.bricks.append(NormalBlock(x, y)) #1

        self.units = self.balls + self.bricks + self.paddles # list containing all units (balls, players and bricks)


    def __repr__(self):
        """Represents the game_state as a string containing world size and each player"""
        return f"world_size: {self.world_size}\nunits: {self.units}"


    


    def update_player(self, action):
        """Updates the game state by carrying out the action for the corresponding player"""

        if action.action_type == 'start':
            self.start_game()
        
        if action.action_type == 'reset' and self.started == True:
            self.reset_game_state()

      
        name = action.get_name()
        if not name in self.players: 
            self.add_player(name) 
        player = self.players[name]

        if action.action_type == 'accelerate': 
            player.accelerate(action.get_acceleration())
            player.step(self.world_size) 
            

        #in case there are multiple balls checks if ball is 'alive'(still in game bounds) if not it gets removed from list
    def update_rest(self):
        for ball in self.balls:
            ball.step(self.world_size)
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius, ball.radius * 2, ball.radius * 2)
            for paddle in self.paddles: 
                paddle_rect = pygame.Rect(paddle.position.x, paddle.position.y, paddle.width, paddle.height)
                if ball_rect.colliderect(paddle_rect):
                    ball.speed.y *= -1

            for brick in self.bricks:
                if brick.alive and ball_rect.colliderect(brick.rect):
                    brick.hit()
                    ball.speed.y *= -1
                if isinstance(brick, PowerUpBlock):
                    power_up_ball = Ball(self.world_size, Position_Center_Start(), Border_Bounce())
                    power_up_ball.position = pygame.Vector2(brick.rect.center)
                    power_up_ball.speed.x *= -1
                    self.balls.append(power_up_ball)

            if not ball.alive:
                self.balls.remove(ball)
                self.units.remove(ball)
                

    def add_player(self, name, color = None): 
        """ Adds a player/paddle with a name and a color"""

        #random color, excluding black and dark grey 
        if color == None:
            player = Paddle(self.world_size, Position_Start(), Border_Stop(), (random.randint(40, 255), random.randint(40, 255), random.randint(40, 255))) 
        #given color 
        else:
            player = Paddle(self.world_size, Position_Start(), Border_Stop(), color)  # create a new player
        self.paddles.append(player)            # add to paddles 
        self.units.append(player)              # add to units
        self.players[name] = player            # add to players too for fast lookup by name 

    def add_ball(self, color = None):
        """ Adds a ball with a name and a color"""
        if color == None:
            ball = Ball(self.world_size, Position_Center_Start(), Border_Bounce()) 
        else: 
            ball = Ball(self.world_size, Position_Center_Start(), Border_Bounce(), color) 
        self.balls.append(ball)
        self.units.append(ball)

    def draw(self, surface, name_textures):
        """ Visualises all paddles, balls, bricks etc. """
        rect = pygame.Rect(pygame.Vector2(0, 0), self.world_size)
        white = (255, 255, 255)
        pygame.draw.rect(surface, white, rect, 2)
        if self.started == False:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text = font.render('Press S to start', False, (255, 255, 255))
            text_rect = text.get_rect(center=(self.world_size.x // 2, self.world_size.y // 2))
            surface.blit(text, text_rect)

        for unit in self.units:
            unit.plot(surface)
        for name, paddle in self.players.items():
            paddle.plot_text(surface, name, name_textures)

    def reset_game_state(self):
        """ Resets to starting screen"""
        self.started = False 
        self.players = {} # dictionary of players/paddles with name as key
        self.paddles = [] # list of players/paddles 
        self.balls = [] # list of balls, 
        self.bricks = [] # list of bricks 
        self.units = []
       