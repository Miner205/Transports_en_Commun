import pygame
from button import Button


class ToolsMenu:
    # menu ouvert avec click droit/en haut à droite, où on choisit les actions possibles (créer un station, etc.)
    def __init__(self):
        self.num_image = 0
        self.rect =


    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pressed())


    def print(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


