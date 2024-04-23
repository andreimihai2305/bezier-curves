import pygame
import random
from settings import *
from point import Point, draw_point, draw_line, draw_points
from sys import exit


pygame.init()


def main() -> None:
    # Game State
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bezier Curves")
    clock = pygame.time.Clock()
    

    points = create_origin_points(3)

    control_points = create_control_points(2)
    curve_points = compute_curve_points(points, control_points)

    all_points = points + control_points
    selected = None
    
    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exit Succesfully")
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, point in enumerate(all_points):
                        if point.rect.collidepoint(event.pos):
                            selected = num

            elif event.type == pygame.MOUSEMOTION:
                if selected != None:
                    if all_points[selected].x + event.rel[0] >= 0 and all_points[selected].x + event.rel[0] <= WIDTH:
                        all_points[selected].x += event.rel[0]
                    
                    if all_points[selected].y + event.rel[1] >= 0 and all_points[selected].y + event.rel[1] <= HEIGHT:
                        all_points[selected].y += event.rel[1]
                    
                    curve_points = compute_curve_points(points, control_points) 

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    selected = None


        screen.fill(BLACK)
        
        draw_curves(screen, points, curve_points)
        draw_points(screen, points)
        draw_points(screen, control_points)
        pygame.display.update()
        clock.tick(FPS)
        

def create_origin_points(num: int) -> list[Point]:
    points = []
    for i in range(num):
        x = random.randrange(0, WIDTH)
        y = random.randrange(0, HEIGHT)
        points.append(Point(x, y, BLUE))

    return points
                      


def create_control_points(num: int) -> list[Point]:
    control_points = []
    for _ in range(num):
        x = random.randrange(0, WIDTH)
        y = random.randrange(0, HEIGHT)
        control_points.append(Point(x, y, GREEN))
                      
    return control_points


def B(start, control, end, t) -> Point:
    xp = 0
    yp = 0
    x0, y0 = start.x, start.y
    x1, y1 = control.x, control.y
    x2, y2 = end.x, end.y

    xp = x1 + (1-t)**2 * (x0 - x1) + t**2 * (x2 - x1)
    yp = y1 + (1-t)**2 * (y0 - y1) + t**2 * (y2 - y1)
    
    return Point(xp, yp, RED)


def compute_curve_points(origin_points: list[Point], control_points: list[Point]) -> list[list[Point]]:
    curve_points = []
    if len(origin_points) != len(control_points) + 1:
        print("Error: Points lists cannot be associated together. Origin points must be equal to control points + 1")
        return [[]]

    for i in range(len(origin_points) - 1):
        current_points = []
        for j in range(50):
            t = j / 50
                              
            start = origin_points[i]
            control = control_points[i]
            end = origin_points[i + 1]
            
            pb = B(start, control, end, t)
            current_points.append(pb)
                              
        curve_points.append(current_points)
    
    return curve_points


def draw_curve(screen: pygame.Surface, start: Point, end: Point, curve_points: list[Point]) -> None:

    draw_line(screen, start, curve_points[0], CYAN)
    for i in range(len(curve_points) - 1):
        draw_line(screen, curve_points[i], curve_points[i + 1], CYAN)

    draw_line(screen, curve_points[-1], end, CYAN)



def draw_curves(screen: pygame.Surface, origin_points: list[Point], curve_points: list[Point]) -> None:
    for i in range(len(origin_points) - 1):
        draw_curve(screen, origin_points[i], origin_points[i + 1], curve_points[i])
                            


if __name__ == "__main__":
    main()


