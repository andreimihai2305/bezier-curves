from settings import * 
import pygame
import pygame.gfxdraw


class Point():
    def __init__(self, x: int, y: int, color: tuple[int, int, int], radius: int = RADIUS) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

def draw_point(surface: pygame.Surface, point: Point) -> None:
    pygame.gfxdraw.filled_circle(surface, point.x, point.y, point.radius, point.color)     


def draw_line(surface: pygame.Surface, point1: Point, point2: Point, line_color: tuple[int, int, int]):
    pygame.draw.aaline(surface, line_color, (point1.x, point1.y), (point2.x, point2.y))

