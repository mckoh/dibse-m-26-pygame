import pygame as pg
from sys import exit
from random import randint
from constants import *

place_coin = lambda: randint(0, WIDTH-COIN_DIAMETER)

pg.init()

screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

player = pg.Rect(
    WIDTH // 2 - PLAYER_WIDTH // 2,
    HEIGHT - PLAYER_HEIGHT - 10,
    PLAYER_WIDTH,
    PLAYER_HEIGHT
)

coin = pg.Rect(
    place_coin(),
    -COIN_DIAMETER,
    COIN_DIAMETER,
    COIN_DIAMETER
)

running = True
while running:

    # Eventhandling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Game controlls
    keys = pg.key.get_pressed()
    if (keys[pg.K_LEFT] or keys[pg.K_a]) and player.x > 0:
        player.x -= PLAYER_X_SPEED
    if (keys[pg.K_RIGHT] or keys[pg.K_d]) and player.x < WIDTH-PLAYER_WIDTH:
        player.x += PLAYER_X_SPEED

    # Coin drop
    coin.y += COIN_Y_SPEED
    if coin.y > HEIGHT:
        coin.x = place_coin()
        coin.y = -COIN_DIAMETER

    # Draw Screen
    screen.fill(WHITE)
    pg.draw.rect(screen, BLACK, player)
    pg.draw.ellipse(screen, COIN_COLOR, coin)

    # Update screen
    pg.display.flip()

    # Set FPS to 60
    clock.tick(60)

pg.quit()
exit()
