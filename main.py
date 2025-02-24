import pygame
import random
w, h = 1000, 800

class Circle:
    def __init__(self):
        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)
        self.w = random.randint(30, 50)
        self.h = int(2.28 * self.w)
        self.x = random.randint(0, w - self.h)
        self.y = random.randint(0, h - self.w)
        self.logo = pygame.image.load('dvd.png')
        self.logo = pygame.transform.scale(self.logo, (self.h, self.w))

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.bounce()

    def bounce(self):
        if self.x <= 0 or self.x >= w - self.h:
            self.vx = -self.vx
        if self.y <= 0 or self.y >= h - self.w:
            self.vy = -self.vy

    def handle_collision(self, circle):
        if self.x < circle.x + circle.h and self.x + self.h > circle.x and self.y < circle.y + circle.w and self.y + self.w > circle.y:
            self.vx, circle.vx = circle.vx, self.vx
            self.vy, circle.vy = circle.vy, self.vy

    def draw(self):
        screen.blit(self.logo, (self.x, self.y))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.h, self.w), 1)


pygame.init()
circles = []
n = 6
for i in range(n):
    circles.append(Circle())

screen = pygame.display.set_mode((w, h))


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for circle in circles:
        circle.move()

        for other_circle in circles:
            if circle != other_circle:
                circle.handle_collision(other_circle)

        circle.draw()

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
