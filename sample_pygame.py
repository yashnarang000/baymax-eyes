import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

running = True
dt = 0.1

pupil_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")

    pygame.draw.circle(screen, "black", pupil_pos, 40)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        pupil_pos.y -= 300 * dt

    if keys[pygame.K_s]:
        pupil_pos.y += 300 * dt

    if keys[pygame.K_a]:
        pupil_pos.x -= 300 * dt
    
    if keys[pygame.K_d]:
        pupil_pos.x += 300 * dt

    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()