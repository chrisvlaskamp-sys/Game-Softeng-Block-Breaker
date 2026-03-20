class Points:
    def __init__(self):
        self.score = 0

    def add(self, brick):
        if not brick.alive:
            self.score += brick.points

    def reset(self):
        self.score = 0

    def draw(self, surface):
        import pygame
        font = pygame.font.SysFont('Comic Sans MS', 25)
        score_text = font.render(f'Score: {self.score}', False, (255, 255, 255))
        surface.blit(score_text, (10, 10))