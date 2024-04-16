import pygame
from settings import *
from point import Point, draw_point, draw_line
from sys import exit

pygame.init()

def main() -> None:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bezier Curves")
    clock = pygame.time.Clock()
    
    p1 = Point(50, 50, RED)
    p2 = Point(100, 100, GREEN)
    print(p1.rect)
    print(p2.rect)
    points= [p1, p2]
    selected = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                print("Exit Succesfully")
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, point in enumerate(points):
                        if point.rect.collidepoint(event.pos):
                            print(True)
                            selected = num
                            print(f"Selected Point: {selected}")


            elif event.type == pygame.MOUSEMOTION:
                if selected != None:
                    points[selected].x += event.rel[0]
                    points[selected].y += event.rel[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                print(f"Released Point: {selected}")
                selected = None

        screen.fill(BLACK)

        draw_line(screen, p1, p2, BLUE)
        #draw_screen(screen, points)
        draw_point(screen, points[0])
        draw_point(screen, points[1])
        pygame.display.update()
        clock.tick(FPS)
        

def draw_screen(screen, points):
    for i in range(len(points) - 1):
        draw_point(screen, points[i])

    draw_point(screen, points[-1])

if __name__ == "__main__":
    main()
