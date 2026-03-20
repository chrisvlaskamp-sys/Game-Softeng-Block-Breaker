import pygame

class Block:
    """Basis block waar alle andere blocks van erven."""

    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 60, 20)
        self.color = color
        self.alive = True
        self.points = 0

    def hit(self):
        self.alive = False

    def plot(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)


class NormalBlock(Block):
    def __init__(self, x, y):
        super().__init__(x, y, color=(60, 200, 80))
        self.points = 1


class HardBlock(Block):
    def __init__(self, x, y):
        super().__init__(x, y, color=(100, 160, 255))
        self.hits_left = 3
        self.points = 5

    def hit(self):
        self.hits_left -= 1
        if self.hits_left <= 0:
            self.alive = False


class PowerUpBlock(Block):
    def __init__(self, x, y):
        super().__init__(x, y, color=(255, 200, 0))
        self.points = 10