import pygame

from constants import *
from player import *
from circleshape import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    middle_x = SCREEN_WIDTH / 2
    middle_y = SCREEN_HEIGHT / 2
    player1 = Player(middle_x, middle_y)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        dt = (game_clock.tick(60)/1000)
        

if __name__ == "__main__":
    main()