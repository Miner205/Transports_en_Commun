import pygame
from button import Button
from toggle import Toggle


class ToolsMenu:
    # menu déroulant en haut à droite, où on choisit qu'elles lignes affichéés ou non
    def __init__(self, x, y, all_lignes_name):
        self.all_toggle_state = {}
        for name in all_lignes_names:
            self.all_toggle_state[name] = False

