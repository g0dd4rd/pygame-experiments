import pygame, sys
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load('graphics/ball.gif') #.convert()
ball_rect = ball.get_rect()
mouse_enabled = False

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.MOUSEMOTION:
      mouse_enabled = True

  if mouse_enabled:
    ball_rect = ball_rect.move(pygame.mouse.get_rel())
    if ball_rect.left < 0 or ball_rect.right > width:
      speed[0] = -speed[0]

    if ball_rect.top < 0 or ball_rect.bottom > height:
      speed[1] = -speed[1]

  screen.fill(black)
  screen.blit(ball, ball_rect)
  pygame.display.flip()
#  pygame.time.delay(25)

