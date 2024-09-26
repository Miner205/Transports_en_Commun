import pygame


class Button:
    def __init__(self, x, y):
        super().__init__()
        self.width = 100
        self.rect = pygame.Rect(x, y, self.width, 32)

    def print(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
