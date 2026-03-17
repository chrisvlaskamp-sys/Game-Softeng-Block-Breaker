import pygame

class Block:
    """Basis block waar alle andere blocks van erven."""

    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 60, 20)
        self.color = color
        self.alive = True

    def hit(self):
        self.alive = False

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)


class NormalBlock(Block):
    """1 hit"""

    def __init__(self, x, y):
        super().__init__(x, y, color=(60, 200, 80))  # groen


class HardBlock(Block):
    """3 hits."""

    def __init__(self, x, y):
        super().__init__(x, y, color=(100, 160, 255))  # blauw
        self.hits_left = 3

    def hit(self):
        self.hits_left -= 1
        if self.hits_left == 0:
            self.alive = False


class PowerUpBlock(Block):
    """Laat een power-up vallen als het geraakt wordt."""

    def __init__(self, x, y):
        super().__init__(x, y, color=(255, 200, 0))  # geel