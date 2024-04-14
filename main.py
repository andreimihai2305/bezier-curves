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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exit Succesfully")
                exit()

        screen.fill(BLACK)
        draw_line(screen, p1, p2, BLUE)
        draw_point(screen, p1)
        draw_point(screen, p2)
        pygame.display.update()
        clock.tick(FPS)




if __name__ == "__main__":
    main()
