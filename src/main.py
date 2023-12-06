import pygame


pygame.init()


screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('Dinoboogl')
pygame.display.set_icon(pygame.image.load('assets/images/chrome_dino.png'))


player_x = 100
player_y = 370
player_speed = 50

cactus_x = player_x + 1200
cactus_y = 370


animations = [
    'assets/images/chrome_dino_running1.png',
    'assets/images/chrome_dino_running2.png',
]

now_animation = 0

is_jump = False
jump_count = 9

score = 0
score_font = pygame.font.Font('assets/fonts/Dhurjati-Regular.ttf', 50)

is_player_live = True
game_start = False


while True:
    if not game_start:
        font = pygame.font.Font('assets/fonts/Dhurjati-Regular.ttf', 90)
        screen.fill((100, 100, 100))
        restart = font.render('Play', True, (255, 5, 10))
        restart_rect = restart.get_rect(topleft=(400, 150))
        screen.blit(restart, (400, 150))

        if restart_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                game_start = True

    else:
        if is_player_live:
            screen.fill((155, 155, 155))
            player = pygame.transform.scale(pygame.image.load(animations[now_animation]), (70, 80))
            player_rect = player.get_rect(topleft=(player_x, player_y))
            screen.blit(player, (player_x, player_y))
            screen.blit(pygame.transform.scale(pygame.image.load('assets/images/cactus.png'), (70, 80)), (cactus_x, cactus_y))
            screen.blit(score_font.render(f'Score: {score}', True, (135, 196, 155)), (350, 10))

            if player_rect.collidepoint(cactus_x, cactus_y):
                is_player_live = False

            if now_animation < 1:
                now_animation += 1

            else:
                now_animation = 0

            cactus_x -= player_speed

            if cactus_x < 0:
                cactus_x = player_x + 1200

            keys = pygame.key.get_pressed()

            # Jump
            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True

            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    
                    else:
                        player_y += (jump_count ** 2) / 2

                    jump_count -= 1

                else:
                    is_jump = False
                    jump_count = 9

                    player_x = 100
                    player_y = 370

            score += 1

        else:
            font = pygame.font.Font('assets/fonts/Dhurjati-Regular.ttf', 90)
            screen.fill((100, 100, 100))
            screen.blit(font.render('You lost', True, (5, 5, 5)), (350, 0))
            screen.blit(font.render(f'Your score: {score}', True, (5, 5, 5)), (250, 90))
            restart = font.render('Play again', True, (255, 5, 10))
            restart_rect = restart.get_rect(topleft=(350, 300))
            screen.blit(restart, (350, 300))

            if restart_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    score = 0
                    is_player_live = True

                    player_x = 100
                    player_y = 370
                    cactus_x = player_x + 1200

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

    clock.tick(25)
    pygame.display.update()
