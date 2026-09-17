import pygame as pg
from sys import exit
from random import randint
from constants import *

place_coin = lambda: randint(0, WIDTH-COIN_DIAMETER)

pg.init()

screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

# Game objects
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

font_small = pg.font.SysFont(None, 36)
font_big = pg.font.SysFont(None, 50)

score = 0
missed = 0
running = True
game_over = False

while running:

    # Eventhandling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Game controls
    keys = pg.key.get_pressed()
    if (keys[pg.K_LEFT] or keys[pg.K_a]) and player.x > 0:
        player.x -= PLAYER_X_SPEED
    if (keys[pg.K_RIGHT] or keys[pg.K_d]) and player.x < WIDTH-PLAYER_WIDTH:
        player.x += PLAYER_X_SPEED

    if not game_over:

        # Coin drop
        coin.y += COIN_Y_SPEED
        if coin.y > HEIGHT:
            coin.x = place_coin()
            coin.y = -COIN_DIAMETER
            missed += 1

        # Check colliders
        if player.colliderect(coin):
            coin.x = place_coin()
            coin.y = -COIN_DIAMETER
            score += 1

        # Check scores
        if missed == 3:
            game_over = True

        # Draw Screen
        screen.fill(WHITE)
        pg.draw.rect(screen, BLACK, player)
        pg.draw.ellipse(screen, COIN_COLOR, coin)

        score_text = font_small.render(f"Score: {score}", True, BLACK)
        missed_text = font_small.render(f"Missed: {missed}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(missed_text, (10, 40))

    else:
        screen.fill(BLACK)
        gameover_text = font_big.render(f"Game Over!", True, WHITE)
        restart_text = font_small.render(f"Press 'R' to restart.", True, WHITE)
        screen.blit(gameover_text, (
            WIDTH // 2 - gameover_text.get_width() // 2,
            HEIGHT // 2 - gameover_text.get_height() - 30
        ))
        screen.blit(restart_text, (
            WIDTH // 2 - restart_text.get_width() // 2,
            HEIGHT // 2 - gameover_text.get_height() +10
        ))

    # Update screen
    pg.display.flip()

    # Set FPS to 60
    clock.tick(60)

pg.quit()
exit()
