import pygame

pygame.init()
w, h = 1000, 500
x, y = 500, 300
vx, vy = 1, 1
sy = 50
sx = int(2.28 * sy)

screen = pygame.display.set_mode((w, h))
logo = pygame.image.load('dvd.png')
logo = pygame.transform.scale(logo, (sx, sy))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += vx
    y += vy

    if x <= 0 or x >= w - sx:
        vx = -vx
    if y <= 0 or y >= h - sy:
        vy = -vy

    screen.fill((0, 0, 0))
    screen.blit(logo, (x, y))
    pygame.display.flip()
    clock.tick(120)

pygame.quit()