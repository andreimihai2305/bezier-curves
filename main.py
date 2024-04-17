import pygame
from settings import *
from point import Point, draw_point, draw_line, draw_points
from sys import exit


pygame.init()


def main() -> None:
    # Game State
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bezier Curves")
    clock = pygame.time.Clock()
    
    p1 = Point(100, 200, BLUE)
    p2 = Point(200, 350, GREEN)
    p3 = Point(400, 200, BLUE)
    p4 = Point(800, 500, GREEN)
    p5 = Point(500, 600, BLUE)

    points: list[Point] = [p1, p2, p3, p4, p5]
    curve_points1: list[Point] = compute_curve_points(p1, p2, p3)
    curve_points2: list[Point] = compute_curve_points(p3, p4, p5)  
    
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
                    for num, point in enumerate(points):
                        if point.rect.collidepoint(event.pos):
                            selected = num

            elif event.type == pygame.MOUSEMOTION:
                if selected != None:
                    points[selected].x += event.rel[0]
                    points[selected].y += event.rel[1]
                    curve_points1 = compute_curve_points(p1, p2, p3)
                    curve_points2 = compute_curve_points(p3, p4, p5)
        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    selected = None


        screen.fill(BLACK)
       
        draw_curve(screen, p1, p3, curve_points1)
        draw_curve(screen, p3, p5, curve_points2)
        draw_points(screen, points)

        pygame.display.update()
        clock.tick(FPS)
        


def B(p1, p2, p3, t) -> Point:
    xp = 0
    yp = 0
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y

    xp = x2 + (1-t)**2 * (x1 - x2) + t**2 * (x3 - x2)
    yp = y2 + (1-t)**2 * (y1 - y2) + t**2 * (y3 - y2)
    
    return Point(xp, yp, RED)


def compute_curve_points(p1, p2, p3) -> list[Point]:
    curve_points = []
    for i in range(20):
        t = i / 20
        pb = B(p1, p2, p3, t)
        curve_points.append(pb)
    
    return curve_points


def draw_curve(screen, start, end, points):
    draw_line(screen, start, points[0], CYAN)
    for i in range(1, len(points)):
        draw_line(screen, points[i - 1], points[i], CYAN)

    draw_line(screen, points[-1], end, CYAN)

if __name__ == "__main__":
    main()


