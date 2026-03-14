import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

VERSION = pygame.version.ver

def main():

    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # instantiate before the loop
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass

        screen.fill("black")
        ship.draw(screen)  # draw after fill, before flip

        pygame.display.flip()
        
        milliseconds_passed = clock.tick(60)
        dt = milliseconds_passed / 1000


if __name__ == "__main__":
    main()

