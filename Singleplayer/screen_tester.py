import pygame
from ball import Ball, Position_Center_Start, Border_Bounce 
from paddle import Paddle, Position_Start, Border_Stop

# initialize pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Block Breaker")

#change to only have one kind of unit
# create units
nr_units = 1
balls = [Ball(screen, Position_Center_Start(), Border_Bounce())]
paddle = Paddle(screen, Position_Start(), Border_Stop())

running = True
while running:  # run until the user closes the window

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user closed the window
            running = False

    # clear the screen
    screen.fill((0, 0, 0))

    paddle.step(screen)
    paddle.plot(screen)
    #in case there are multiple balls checks if ball is 'alive'(still in game bounds) if not it gets removed from list
    for ball in balls[:]:
        ball.step(screen)

        ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius, ball.radius * 2, ball.radius * 2)
        paddle_rect = pygame.Rect(paddle.position.x, paddle.position.y, paddle.width, paddle.height)
        if ball_rect.colliderect(paddle_rect):
            ball.speed.y *= -1

        if not ball.alive:
            balls.remove(ball)
            continue
        ball.plot(screen)
    pygame.display.flip()  # update the screen
    clock.tick(60)
pygame.quit()