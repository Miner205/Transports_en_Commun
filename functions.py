# file for definitions of some useful functions
import pygame


def pygame_draw_cross(surface, color, center_point, diameter=5, width=1):
    """draw X ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d, y-d), (x+d, y+d), width)
    pygame.draw.line(surface, color, (x+d, y-d), (x-d, y+d), width)


def pygame_draw_plus(surface, color, center_point, diameter=5, width=1):
    """draw + ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x, y-d), (x, y+d), width)
    pygame.draw.line(surface, color, (x-d, y), (x+d, y), width)


def pygame_draw_star(surface, color, center_point, diameter=5, width=1):
    """draw X&+ : * ;
    center_point like (x,y)"""
    pygame_draw_cross(surface, color, center_point, diameter, width)
    pygame_draw_plus(surface, color, center_point, diameter, width)
