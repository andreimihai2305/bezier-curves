import pygame
from settings import *
from sys import exit

pygame.init()

def main() -> None:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bezier Curves")
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exit Succesfully")
                exit()

        screen.fill(BLACK)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
