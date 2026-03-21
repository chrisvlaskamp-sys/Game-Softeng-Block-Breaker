import pygame
from pyparsing import ABC, abstractmethod

class Position_Strategy(ABC):
    @abstractmethod
    def init_position(self, unit, world_size):
        """ Initialize position of a unit """
        ...

class Border_Strategy(ABC):
    @abstractmethod
    def handle_border(self, unit, world_size):
        """ Handle a unit's movement at the edges of the screen. """
        ...

class Position_Start(Position_Strategy):
    def init_position(self, unit, world_size):
        unit.position = pygame.Vector2(
            world_size.x  // 2,
            world_size.y - 50
        )

class Border_Stop(Border_Strategy):
    def handle_border(self, unit, world_size):
        width = world_size.x 
        if unit.position.x < 0:
            unit.position.x = 0
        if unit.position.x + unit.width > width:
            unit.position.x = width - unit.width

class Paddle:
    def __init__(self, world_size, position_strategy, border_strategy, color=(255, 0, 0)):
        self.width = 100
        self.height = 20
        self.speed = pygame.Vector2(0,0)
        self.color = color

        self.position = pygame.Vector2(0, 0)
        self.position_strategy = position_strategy
        self.border_strategy = border_strategy

        self.position_strategy.init_position(self, world_size)
    
    def accelerate(self,acceleration):
        self.speed += acceleration
        self.speed *= 0.95

    def plot(self, surface):
        """ Plot a unit """
        pygame.draw.rect(surface, self.color, (self.position.x, self.position.y, self.width, self.height))
        

    def plot_text(self, surface, name, name_textures):
        name_texture = name_textures.get_texture(name)
        text_offset = pygame.Vector2(name_texture.get_size() )
        text_offset.x = (text_offset.x - self.width ) // 2
        text_offset.y += self.height  
        surface.blit(name_texture, self.position - text_offset )

    def step(self, world_size):
        """ Take a step: move and possibly other actions. """
        self.move(world_size)

    def move(self, world_size):
        self.position += self.speed
        self.border_strategy.handle_border(self, world_size)







