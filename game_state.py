import pygame
import random 

from ball import Ball, Position_Center_Start, Border_Bounce 
from paddle import Paddle, Position_Start, Border_Stop
from bricks import NormalBlock, HardBlock, PowerUpBlock
from points import Points

"""
Part of the code in this file has been adapted from the game_state.py example code. 
"""


class Game_State:

    def __init__(self, world_size):
        self.world_size = world_size
        self.started = False 
        self.ended = False 
        self.players = {} # dictionary of players/paddles with name as key
        self.paddles = [] # list of players/paddles 
        self.balls = [] # list of balls, 
        self.bricks = [] # list of bricks 
        self.units = []
        self.points = Points()

        # ball speed options: 
        self.difficulty_options = [("Slow", 2.5), ("Normal", 3.5), ("Fast", 4.5), ("Very fast", 5.5)]
        
        #button 
        button_width = 120
        button_height = 36 
        distance_between_buttons = 16
        first_button_x = (self.world_size.x - (button_width * len(self.difficulty_options) + distance_between_buttons* (len(self.difficulty_options)-1))) // 2
        button_y = self.world_size.y // 2 + 40
        self.difficulty_buttons = []
        for i, (option_name, speed_multiplier) in enumerate(self.difficulty_options):
            rect = pygame.Rect(first_button_x + i * (button_width + distance_between_buttons), button_y, button_width, button_height)
            self.difficulty_buttons.append((rect, option_name, speed_multiplier))
        self.selected_difficulty_index = 1 # normal is default option
        
    def start_game(self):
        """starts a game with players and a playing field of size world_size, """
        self.started = True 
        self.points.reset()
        speed_multiplier = self.difficulty_options[self.selected_difficulty_index][1]
        self.balls = [Ball(self.world_size, Position_Center_Start(), Border_Bounce(), speed_multiplier)]
        self.units = self.paddles[:]  # reset units but keep paddles 
        self.units += self.balls

        #Initiate bricks: 
        percentages = {
        NormalBlock: 60,   # 60%
        HardBlock: 30,     # 30%
        PowerUpBlock: 10,  # 10%
        }

        self.bricks = []
        for row in range(5):
            for col in range(10):
                x = col * 75 + 50
                y = row * 35 + 50
                brick_type = random.choices(
                    list(percentages.keys()),
                    weights=list(percentages.values())
                )[0]
                brick = brick_type(x, y)
                self.bricks.append(brick)
                self.units.append(brick)


    def __repr__(self):
        """Represents the game_state as a string containing world size and each player"""
        return f"world_size: {self.world_size}\nunits: {self.units}"


    def update_player(self, action):
        """Updates the game state by carrying out the action for the corresponding player"""

        # start
        if action.action_type == 'start' and self.started == False:
            self.start_game()
        
        # reset
        if action.action_type == 'reset' and self.started == True:
            self.reset_game_state()

        # choose difficulty
        if action.action_type == 'difficulty':
            self.selected_difficulty_index = action.get_value()
        
        if action.action_type == 'mouse': 
            self.handle_mouse(action.get_value())

        # acceleration 
        name = action.get_name()
        if not name in self.players: 
            self.add_player(name) 
        player = self.players[name]

        if action.action_type == 'accelerate': 
            player.accelerate(action.get_acceleration())
            player.step(self.world_size) 

        if self.started == True and len(self.bricks) == 0:
            self.ended = True 
    


    def update_rest(self):
        for ball in self.balls[:]:
            ball.step(self.world_size)
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius, ball.radius * 2, ball.radius * 2)
            
            for paddle in self.paddles: 
                paddle_rect = pygame.Rect(paddle.position.x, paddle.position.y, paddle.width, paddle.height)
                if ball_rect.colliderect(paddle_rect):
                    ball.speed.y *= -1

            for brick in self.bricks:
                if brick.alive and ball_rect.colliderect(brick.rect):
                    brick.hit()
                    if ball.speed.y > 0:
                        ball.position.y = brick.rect.top - ball.radius
                    else:
                        ball.position.y = brick.rect.bottom + ball.radius
                    ball.speed.y *= -1
                    self.points.add(brick)
                    if isinstance(brick, PowerUpBlock) and not brick.alive:
                        starting_position = pygame.Vector2(brick.rect.center)
                        self.add_ball(position=starting_position)
                    break

            if not ball.alive:
                self.balls.remove(ball)
                self.units.remove(ball)
                continue

        # Opruimen van dode bricks, buiten de ball-loop
        for brick in self.bricks[:]:
            if not brick.alive:
                self.bricks.remove(brick)
                self.units.remove(brick)

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


    def add_ball(self, color = None, position = None):
        """ Adds a ball with a name and a color"""
        speed_multiplier = self.difficulty_options[self.selected_difficulty_index][1]
        if color == None:
            ball = Ball(self.world_size, Position_Center_Start(), Border_Bounce(), speed_multiplier) 
        else: 
            ball = Ball(self.world_size, Position_Center_Start(), Border_Bounce(), speed_multiplier, color) 
        if position != None:
            ball.position = position
        self.balls.append(ball)
        self.units.append(ball)

    def draw(self, surface, name_textures):
        """ Visualises all paddles, balls, bricks etc. """

        # draw starting screen
        if self.started == False:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text = font.render('Press S to start', False, (255, 255, 255))
            text_rect = text.get_rect(center=(self.world_size.x // 2, self.world_size.y // 2))
            surface.blit(text, text_rect)
            button_font = pygame.font.SysFont('Comic Sans MS', 20)
            if hasattr(self, 'difficulty_buttons'):
                for index, (rect, name, speed_multiplier) in enumerate(self.difficulty_buttons):
                    color = (200,180,60) if index == self.selected_difficulty_index else (60,60,60)
                    pygame.draw.rect(surface, color, rect)
                    pygame.draw.rect(surface, (255,255,255), rect, 2)
                    button_label = button_font.render(name, True, (255,255,255))
                    surface.blit(button_label, button_label.get_rect(center=rect.center))
    

        #draw screen and points 
        rect = pygame.Rect(pygame.Vector2(0, 0), self.world_size)
        white = (255, 255, 255)
        pygame.draw.rect(surface, white, rect, 2)
        if self.ended == False and self.started == True: 
            self.points.draw(surface)
            

        #draw units 
        for unit in self.units:
            unit.plot(surface)
        for name, paddle in self.players.items():
            paddle.plot_text(surface, name, name_textures)

        # draw final screen
        if self.ended == True:
            font1 = pygame.font.SysFont('Comic Sans MS', 40)
            font2 = pygame.font.SysFont('Comic Sans MS', 30)
    
            text1 = font1.render('Well Done!', False, (255, 255, 255))
            text2 = font2.render('Press r to go back to start screen', False, (255, 255, 255))
            text3 = font2.render(f"you achieved score {self.points.score}", False, (255, 255, 255))
            text_rect1 = text1.get_rect(center=(self.world_size.x // 2, self.world_size.y // 2))
            text_rect2 = text2.get_rect(center=(self.world_size.x // 2, self.world_size.y // 2 + 40))
            text_rect3 = text3.get_rect(center=(self.world_size.x // 2, self.world_size.y // 2 + 70))
            surface.blit(text1, text_rect1)
            surface.blit(text2, text_rect2)
            surface.blit(text3, text_rect3)

    def reset_game_state(self):
        """ Resets to starting screen"""
        self.started = False 
        self.ended = False 


        # reset list of players/paddles 
        self.balls = [] # reset list of balls, 
        self.bricks = [] # reset list of bricks 
        self.units = self.paddles # remove all units except paddles (= players)
        self.points.reset() # reset points 
       
    
    def handle_mouse(self, pos):
        "Executes actions that are dependent on mouse position"
        if self.started == False:
            for idx, (rect, name, mult) in enumerate(self.difficulty_buttons):
                if rect.collidepoint(pos):
                    self.selected_difficulty_index = idx
       