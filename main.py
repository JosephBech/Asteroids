import pygame

from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from asteroid import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    dt = 0
    middle_x = SCREEN_WIDTH / 2
    middle_y = SCREEN_HEIGHT / 2

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player1 = Player(middle_x, middle_y)
    asteroid_field = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for obj in updatable:
            obj.update(dt)

        
        for obj in asteroids:

            if obj.Collision_Check(player1) == True:
                print("Game Over!")
                return
            
            for shot in shots:
                if obj.Collision_Check(shot) == True:
                    shot.kill()
                    obj.split()
            
                    




        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = (game_clock.tick(60)/1000)
        

if __name__ == "__main__":
    main()