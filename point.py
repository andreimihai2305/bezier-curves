from settings import * 
import pygame


class Point():
    def __init__(self, x: int, y: int, color: tuple[int, int, int], radius: int = RADIUS) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.rect = None


        
def draw_point(surface: pygame.Surface, point: Point) -> pygame.Rect:
    return pygame.draw.circle(surface, point.color, (point.x, point.y), point.radius)


def draw_line(surface: pygame.Surface, point1: Point, point2: Point, line_color: tuple[int, int, int]):
    pygame.draw.aaline(surface, line_color, (point1.x, point1.y), (point2.x, point2.y))

        

def draw_points(surface: pygame.Surface, points: list[Point]) -> None:
    for point in points:
        point.rect = draw_point(surface, point)

