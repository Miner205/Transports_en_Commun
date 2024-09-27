import pygame


class Button:
    def __init__(self, x, y):
        super().__init__()
        self.width = 100
        self.rect = pygame.Rect(x, y, self.width, 32)

    def use(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                click_effect = pygame.mixer.Sound("musics/Pen_Clicking.mp3")
                click_effect.play()
                return True

    def print(self, screen, opacity=255):
        pygame.draw.rect(screen, (0, 0, 255, opacity), self.rect, border_radius=2)
