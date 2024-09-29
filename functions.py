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
    """draw - ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d, y), (x+d, y), line_thickness)


def pygame_draw_star(surface, color, center_point, diameter=5, line_thickness=1):
    """draw X&+ : * ;
    center_point like (x,y)"""
    pygame_draw_cross(surface, color, center_point, diameter, line_thickness)
    pygame_draw_plus(surface, color, center_point, diameter, line_thickness)


def pygame_draw_check(surface, color, center_point, diameter=5, line_thickness=1):
    """draw check mark ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x+d, y-d), (x-d+d*1/2, y+d), line_thickness)
    pygame.draw.line(surface, color, (x-d*5/3+d*1/2, y), (x-d+d*1/2, y+d), line_thickness)


def pygame_draw_left_arrow(surface, color, left_middle_pos, right_middle_pos, line_thickness=0):
    """draw a left arrow ;
        left_middle_pos & right_middle_pos like (x,y) & (x2,y)"""
    (x, y), x2 = left_middle_pos, right_middle_pos[0]
    d = (x2-x)//2
    pygame.draw.polygon(surface, color, [(x, y), (x2, y-d), (x2, y+d)], line_thickness)


def pygame_draw_right_arrow(surface, color, left_middle_pos, right_middle_pos, line_thickness=0):
    """draw a right arrow ;
        left_middle_pos & right_middle_pos like (x,y) & (x2,y)"""
    (x, y), x2 = left_middle_pos, right_middle_pos[0]
    d = (x2-x)//2
    pygame.draw.polygon(surface, color, [(x2, y), (x, y-d), (x, y+d)], line_thickness)
