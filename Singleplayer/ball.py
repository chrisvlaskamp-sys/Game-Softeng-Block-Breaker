import pygame
from pyparsing import ABC, abstractmethod

class Position_Strategy(ABC):
    @abstractmethod
    def init_position(self, unit, screen):
        """ Initialize position of a unit """
        ...

class Border_Strategy(ABC):
    @abstractmethod
    def handle_border(self, unit, screen):
        """ Handle a unit's movement at the edges of the screen. """
        ...

#change to top of paddle
class Position_Center_Start(Position_Strategy):
    def init_position(self, unit, screen):
        unit.position = pygame.Vector2(
            screen.get_width() // 2,
            screen.get_height() // 2
        )

#for the borders of the game
class Border_Bounce(Border_Strategy):
    def handle_border(self, unit, screen):
        width = screen.get_width()
        height = screen.get_height()

        #left
        if unit.position.x < unit.radius:
            unit.position.x = unit.radius
            unit.speed.x =- unit.speed.x
        #top
        if unit.position.y < unit.radius:
            unit.position.y = unit.radius
            unit.speed.y =- unit.speed.y
        #right
        if unit.position.x > width-unit.radius:
            unit.position.x = width-unit.radius
            unit.speed.x =- unit.speed.x
        #bottom(special)
        if unit.position.y > height: #ball isn't cought and will go out of bounds and be out of the game
            return False
        return True

class Ball():

    def __init__(self, screen, position_strategy, border_strategy, color=(0, 255, 0)):
        """ Initialize a unit """
        self.position = pygame.Vector2(0,0)
        self.speed = pygame.Vector2(4,-4)
        self.color = color
        self.radius = 10

        self.position_strategy = position_strategy
        self.border_strategy = border_strategy

        self.position_strategy.init_position(self, screen)

        #ball is in bounds
        self.alive = True
        

    def plot(self, screen):
        """ Plot a unit """
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def step(self, screen):
        """ Take a step: move and possibly other actions. """
        self.move(screen)

    def move(self, screen):
        """ Move a unit """
        self.position += self.speed
        alive = self.border_strategy.handle_border(self, screen)
        if alive == False:
            self.alive = False



