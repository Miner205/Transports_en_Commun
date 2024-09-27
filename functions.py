# file for definitions of some useful functions
import pygame


def pygame_draw_cross(surface, color, center_point, diameter=5, line_thickness=1):
    """draw X ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d, y-d), (x+d, y+d), line_thickness)
    pygame.draw.line(surface, color, (x+d, y-d), (x-d, y+d), line_thickness)


def pygame_draw_plus(surface, color, center_point, diameter=5, line_thickness=1):
    """draw + ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x, y-d), (x, y+d), line_thickness)
    pygame.draw.line(surface, color, (x-d, y), (x+d, y), line_thickness)


def pygame_draw_minus(surface, color, center_point, diameter=5, line_thickness=1):
    """draw + ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d, y), (x+d, y), line_thickness)


def pygame_draw_star(surface, color, center_point, diameter=5, line_thickness=1):
    """draw X&+ : * ;
    center_point like (x,y)"""
    pygame_draw_cross(surface, color, center_point, diameter, line_thickness)
    pygame_draw_plus(surface, color, center_point, diameter, line_thickness)
