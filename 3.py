import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))
done = False
x = 30
y = 30

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            if y-20>=25: y-=20
        if pressed[pygame.K_DOWN]:
            if y+20<=275: y+=20
        if pressed[pygame.K_LEFT]:
            if x-20>=25: x-=20
        if pressed[pygame.K_RIGHT]:
            if x+20<=375: x+=20  

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen,"Red",(x,y),25)
        
        pygame.display.flip()
        clock.tick(30)