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

class Position_Start(Position_Strategy):
    def init_position(self, unit, screen):
        unit.position = pygame.Vector2(
            screen.get_width() // 2,
            screen.get_height() - 50
        )

class Border_Stop(Border_Strategy):
    def handle_border(self, unit, screen):
        width = screen.get_width()
        if unit.position.x < 0:
            unit.position.x = 0
        if unit.position.x + unit.width > width:
            unit.position.x = width - unit.width

class Paddle:
    def __init__(self, screen, position_strategy, border_strategy, color=(255, 0, 0)):
        self.width = 100
        self.height = 20
        self.speed = pygame.Vector2(0,0)
        self.color = color

        self.position = pygame.Vector2(0, 0)
        self.position_strategy = position_strategy
        self.border_strategy = border_strategy

        self.position_strategy.init_position(self, screen)
    
    def accelerate(self,acceleration):
        self.speed += acceleration
        self.speed *= 0.97

    def plot(self, screen):
        """ Plot a unit """
        pygame.draw.rect(screen, self.color, (self.position.x, self.position.y, self.width, self.height))

    def step(self, screen):
        """ Take a step: move and possibly other actions. """
        self.position += self.speed

   
    








