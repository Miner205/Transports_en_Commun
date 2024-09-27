import pygame
from button import Button
from textezone import TextZone


class ToolsMenu:
    # menu ouvert avec click droit/en haut à droite, où on choisit les actions possibles (créer un station, etc.)
    def __init__(self, x=0, y=0):
        self.which_submenu = ['0']  # 1st char for the actual menu ; next char are for the previous menus
        # ; if num_submenu[0] == '0' : del/reset ToolsMenu
        self.width = 100 + 20
        self.height = 32*4 + 20
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.all_button = {}
        self.all_textzone = {}
        self.button_to_del = []
        self.textzone_to_del = []

    def update(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:  # open menu
            self.rect.x, self.rect.y = event.pos
            self.which_submenu = ['1', '0']
            self.all_button.clear()
            self.all_textzone.clear()
            self.all_button["back"] = Button(self.rect.x + 10, self.rect.y + 10 + 32 * 3)
            self.all_textzone["back"] = TextZone(self.rect.x + 10, self.rect.y + 10 + 32 * 3, False, "back")

        elif self.which_submenu[0] != '0' and event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
            self.exit_menu()

        for button in self.all_button.keys():
            if self.all_button[button].use(event):
                if button == "back":
                    self.which_submenu[0] = self.which_submenu.pop()
                    if self.which_submenu[0] == '0':
                        self.all_textzone.clear()
                else:
                    self.which_submenu.append(button[0])
                    if button == "1menutruc":
                        self.which_submenu[0] = "2menutruc"[0]
                    elif button == "1menutruc2":
                        self.which_submenu[0] = "3menutruc"[0]
                    elif button == "1menutruc3":
                        self.which_submenu[0] = "4menutruc"[0]

        for button in self.all_button.keys():
            if self.which_submenu[0] == '0' or (button != "back" and button[0] != self.which_submenu[0]):
                self.button_to_del.append(button)

        for textzone in self.all_textzone.keys():
            if textzone != "back" and textzone[0] != self.which_submenu[0]:
                self.textzone_to_del.append(textzone)

        if self.button_to_del:
            for elt in self.button_to_del:
                del (self.all_button[elt])
            self.button_to_del.clear()

        if self.textzone_to_del:
            for elt in self.textzone_to_del:
                del (self.all_textzone[elt])
            self.textzone_to_del.clear()

        if self.which_submenu[0] == '1' and "1menutruc" not in self.all_button.keys():
            self.all_button["1menutruc"] = Button(self.rect.x+10, self.rect.y+10)
            self.all_button["1menutruc2"] = Button(self.rect.x+10, self.rect.y+10+32)
            self.all_button["1menutruc3"] = Button(self.rect.x+10, self.rect.y+10+32*2)
            self.all_textzone["1menutruc"] = TextZone(self.rect.x+10, self.rect.y+10, False, "menutruc")
            self.all_textzone["1menutruc2"] = TextZone(self.rect.x+10, self.rect.y+10+32, False, "menutruc2")
            self.all_textzone["1menutruc3"] = TextZone(self.rect.x+10, self.rect.y+10+32*2, False, "menutruc3")

    def exit_menu(self):
        self.which_submenu = ['0']
        self.all_button.clear()
        self.all_textzone.clear()

    def print(self, screen):
        if self.which_submenu[0] != '0':
            pygame.draw.rect(screen, (255, 255, 255), self.rect)

            for textzone in self.all_textzone.values():
                textzone.draw(screen)
