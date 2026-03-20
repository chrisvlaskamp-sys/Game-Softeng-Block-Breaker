import pygame
from ball import Ball, Position_Center_Start, Border_Bounce 
from paddle import Paddle, Position_Start, Border_Stop
from bricks import NormalBlock, HardBlock, PowerUpBlock

# initialize pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Block Breaker")
world_size = pygame.Vector2(800, 600)

# create units
nr_units = 1
balls = [Ball(world_size, Position_Center_Start(), Border_Bounce())]
paddle = Paddle(world_size, Position_Start(), Border_Stop())

bricks = []
for row in range(5):
    for col in range(10):
        x = col * 75 + 50
        y = row * 35 + 50
        if row == 0:
            bricks.append(HardBlock(x, y)) #3
        elif row == 4:
            bricks.append(PowerUpBlock(x, y)) #power
        else:
            bricks.append(NormalBlock(x, y)) #1

running = True
while running:  # run until the user closes the window

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user closed the window
            running = False

    # clear the screen
    screen.fill((0, 0, 0))


    #nieuw toegeveogd want mijn paddle wou niet bewegen 
    #ook heb ik de world size bij wat dingen aangepast.
    keys = pygame.key.get_pressed()
    acceleration = pygame.Vector2(0, 0)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        acceleration.x -= 0.5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        acceleration.x += 0.5
    paddle.accelerate(acceleration)
    paddle.step(world_size)
    paddle.plot(screen)

    for brick in bricks:
        brick.plot(screen)

    #in case there are multiple balls checks if ball is 'alive'(still in game bounds) if not it gets removed from list
    for ball in balls[:]:
        ball.step(world_size)

        ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius, ball.radius * 2, ball.radius * 2)
        paddle_rect = pygame.Rect(paddle.position.x, paddle.position.y, paddle.width, paddle.height)
        if ball_rect.colliderect(paddle_rect):
            ball.speed.y *= -1

        for brick in bricks:
            if brick.alive and ball_rect.colliderect(brick.rect):
                brick.hit()
                ball.speed.y *= -1

        if not ball.alive:
            balls.remove(ball)
            continue
        ball.plot(screen)

    pygame.display.flip()  # update the screen
    clock.tick(60)
pygame.quit()