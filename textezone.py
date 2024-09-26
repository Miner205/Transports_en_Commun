import pygame


class TextZone:
    def __init__(self, x, y, txt=""):
        super().__init__()
        self.text_font = pygame.font.Font(None, 32)
        self.user_text = txt
        self.width = 100
        self.rect = pygame.Rect(x, y, self.width, 32)
        self.active = False

    def use(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.active:
                    click_effect = pygame.mixer.Sound("musics/Pen_Clicking.mp3")
                    click_effect.play()
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    if len(event.unicode) != 0:   # Pour éviter que les touches comme maj ou alt fasse crasher le jeu.
                        self.user_text += event.unicode

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=2)
            pygame.draw.rect(screen, (255, 220, 0), self.rect, 2, 2)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, 2)
        text_surface = self.text_font.render(self.user_text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
