import pygame
from button import Button
from toggle import Toggle
import functions as fct


class ToggleLignesMenu:
    # menu déroulant en haut à droite, où l'on choisit qu'elle lignes afficher ou non
    def __init__(self, x, y, all_lignes):
        self.width = 15 * 9
        self.height = 32
        self.nb_of_toggles_by_page = 20
        self.border_margin = 3
        self.rect = pygame.Rect(x, y, self.width + self.border_margin * 2,
                                self.height * self.nb_of_toggles_by_page + self.border_margin * 2)
        self.show_menu = Toggle(self.rect.x+self.border_margin, self.rect.y-self.height-self.border_margin,
                                "SeeLines", False, self.width, self.height)
        self.left_arrow_button = Button(self.rect.centerx-41-self.border_margin+1, self.rect.y+self.rect.h+self.border_margin, 41, 41)
        self.right_arrow_button = Button(self.rect.centerx+self.border_margin-1, self.rect.y+self.rect.h+self.border_margin, 41, 41)
        self.which_page = 1
        self.nb_of_page = 1
        self.all_toggle = {}
        self.all_toggle_state = {}
        self.all_lines_infos = []
        self.update_all_lignes_toggles(all_lignes)

    def update_all_lignes_toggles(self, all_lignes):  # to do, after adding or removing a ligne, or when initializing the menu
        for ligne in all_lignes.all_lignes:
            self.all_lines_infos.append((ligne.id, ligne.color))
        self.all_lines_infos.sort(key=fct_for_the_sort)
        for l_i in self.all_lines_infos:
            self.all_toggle_state[l_i[0]] = True

        self.nb_of_page = 1+len(self.all_toggle_state.keys())//self.nb_of_toggles_by_page

    def update(self, event):
        self.show_menu.use(event)

        if self.show_menu.toggle_state:
            for toggle in self.all_toggle.keys():
                self.all_toggle[toggle].use(event)
                self.all_toggle_state[toggle] = self.all_toggle[toggle].toggle_state

            if self.which_page != 1:
                if self.left_arrow_button.use(event):
                    self.which_page -= 1

            if self.which_page != self.nb_of_page:
                if self.right_arrow_button.use(event):
                    self.which_page += 1

        tmp = {}
        i = 0
        for lines_i in self.all_lines_infos[(self.which_page-1)*self.nb_of_toggles_by_page:self.nb_of_toggles_by_page*self.which_page]:  # to verify the range !!
            tmp[lines_i[0]] = Toggle(self.rect.x+self.border_margin, self.rect.y+self.border_margin+32*i,
                                     lines_i[0], self.all_toggle_state[lines_i[0]], self.width, self.height, lines_i[1])
            i += 1
        self.all_toggle = tmp
        del tmp

    def print(self, screen):
        self.show_menu.print(screen)

        if self.show_menu.toggle_state:
            pygame.draw.rect(screen, (230, 230, 230), self.rect)

            for toggle in self.all_toggle.values():
                toggle.print(screen)

            if self.which_page != 1:
                self.left_arrow_button.print(screen)
                fct.pygame_draw_left_arrow(screen, (130, 0, 0),
                                           (self.left_arrow_button.rect.midleft[0]+self.left_arrow_button.rect.w*1/4, self.left_arrow_button.rect.midleft[1]),
                                           (self.left_arrow_button.rect.midright[0]-self.left_arrow_button.rect.w*1/4, self.left_arrow_button.rect.midright[1]))

            if self.which_page != self.nb_of_page:
                self.right_arrow_button.print(screen)
                fct.pygame_draw_right_arrow(screen, (130, 0, 0),
                                            (self.right_arrow_button.rect.midleft[0]+self.right_arrow_button.rect.w*1/4, self.right_arrow_button.rect.midleft[1]),
                                            (self.right_arrow_button.rect.midright[0]-self.right_arrow_button.rect.w*1/4, self.right_arrow_button.rect.midright[1]))


def fct_for_the_sort(elt):
    return elt[0]
