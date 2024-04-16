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
    p3 = Point(400, 200, BLUE)
    points= [p1, p2, p3]
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
                            selected = num
                            print(f"Selected Point: {selected}")


            elif event.type == pygame.MOUSEMOTION:
                if selected != None:
                    points[selected].x += event.rel[0]
                    points[selected].y += event.rel[1]


        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and selected != None:
                    print(f"Released Point: {selected}")
                    selected = None


        screen.fill(BLACK)
        
        draw_screen(screen, points)
        
        pygame.display.update()
        clock.tick(FPS)
        

def draw_screen(screen, points):
    for i in range(1, len(points)):
        draw_line(screen, points[i - 1], points[i], BLUE)

    for i in range(len(points)):
        points[i].rect = draw_point(screen, points[i])
        
    


if __name__ == "__main__":
    main()
