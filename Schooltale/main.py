import pygame
from sys import exit
import random

pygame.init()

# screen size
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Schooltale')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

current_state = "MENU"

#MENU
title_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 55)
title_surf = title_font.render('SCHOOLTALE', False, 'white')
title_rect = title_surf.get_rect(center=(400, 150))

#CUTSCENE1
cutscene1_surface1_surf = pygame.Surface((700, 100))
cutscene1_surface1_surf.fill('black')
pygame.draw.rect(cutscene1_surface1_surf, 'white', cutscene1_surface1_surf.get_rect(), 3)
cutscene1_surface1_rect = cutscene1_surface1_surf.get_rect(topleft=(50, 275))

cutscene_font = pygame.font.Font("fonts/PixelOperator8.ttf", 15)
dialogue_1_surf = cutscene_font.render('I really do not want to be here...', False, 'white')
dialogue_1_rect = dialogue_1_surf.get_rect(topleft=(20, 20))

dialogue_2_surf = cutscene_font.render("Seriously, what does changing schools even do?", False, 'white')
dialogue_2_rect = dialogue_2_surf.get_rect(topleft=(20, 20))

dialogue_3_surf = cutscene_font.render('...', False, 'white')
dialogue_3_rect = dialogue_3_surf.get_rect(topleft=(20, 20))

dialogue_4_surf = cutscene_font.render('Fine, maybe third times the charm...', False, 'white')
dialogue_4_rect = dialogue_3_surf.get_rect(topleft=(20, 20))

#FIGHT1
# background image
background_surf = pygame.image.load('images/background.png')
background_rect = background_surf.get_rect()

gaming_surf = pygame.Surface((700, 300), pygame.SRCALPHA)
gaming_surf.fill((106, 103, 103, 128))

# character image 
character_surf = pygame.image.load('images/main_character_head.png')
character_surf = pygame.transform.scale(character_surf, (80, 90))  # width x height
character_rect = character_surf.get_rect(topleft=(350,150))

# backpack image
backpack_surf = pygame.image.load('images/backpack.png')
backpack_surf = pygame.transform.scale(backpack_surf, (80, 80)) # width x height
backpack_rect = backpack_surf.get_rect(topleft=(675, 250))

# lives image
heart_surf = pygame.image.load('images/heart.png')
heart_surf = pygame.transform.scale(heart_surf, (30, 30)) # width x height

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 

        if current_state == "MENU":
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_state = "CUTSCENE1"
                cutscene_start_time = pygame.time.get_ticks()
                GAME_DURATION = 31000 # 1s = 1000
                lives = 3  

    t = pygame.time.get_ticks()
    brightness = (t // 500) % 2
    color = (200, 200, 200) if brightness else (255, 255, 255)

    start_font = pygame.font.Font("fonts/PixelOperator.ttf", 20)
    start_surf = start_font.render('CLICK TO PLAY', False, color)
    start_rect = start_surf.get_rect(center=(400, 300))

    if current_state == "MENU":
        screen.blit(title_surf, title_rect)
        screen.blit(start_surf, start_rect)
    
    if current_state == "CUTSCENE1":    
        screen.fill('black')
        elapsed_time = pygame.time.get_ticks() - cutscene_start_time
        if elapsed_time > 5000:
            cutscene1_surface1_surf.blit(dialogue_1_surf, dialogue_1_rect)
            screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)
        if elapsed_time > 10000:
            cutscene1_surface1_surf.fill('black')
            pygame.draw.rect(cutscene1_surface1_surf,'white', cutscene1_surface1_surf.get_rect(), 3)
            cutscene1_surface1_surf.blit(dialogue_2_surf, dialogue_2_rect)
            screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)
        if elapsed_time > 15000:
            cutscene1_surface1_surf.fill('black')
            pygame.draw.rect(cutscene1_surface1_surf,'white', cutscene1_surface1_surf.get_rect(), 3)
            cutscene1_surface1_surf.blit(dialogue_3_surf, dialogue_3_rect)
            screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)
        if elapsed_time > 20000:
            cutscene1_surface1_surf.fill('black')
            pygame.draw.rect(cutscene1_surface1_surf,'white', cutscene1_surface1_surf.get_rect(), 3)
            cutscene1_surface1_surf.blit(dialogue_4_surf, dialogue_4_rect)
            screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)
        if elapsed_time > 25000:
            current_state = "FIGHT1"
            start_time = pygame.time.get_ticks()
        
    if current_state == "FIGHT1":
        # elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time

        # draw background first
        screen.blit(background_surf, background_rect)
        screen.blit(gaming_surf, (50, 50))

        if elapsed_time < GAME_DURATION and lives > 0:
            # character
            screen.blit(character_surf, character_rect)

            # spawn backpack
            spawn_delay = 3000
            if elapsed_time > spawn_delay:
                screen.blit(backpack_surf, backpack_rect)

                right_speed = random.randint(7, 9)
                backpack_rect.right -= right_speed
                if backpack_rect.left < 50:
                    backpack_rect.x = 675
                    backpack_rect.y = random.randint(100, 250)

            # controls
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                character_rect.y -= 5
            if keys[pygame.K_a]:
                character_rect.x -= 5
            if keys[pygame.K_s]:
                character_rect.y += 5
            if keys[pygame.K_d]:
                character_rect.x += 5

            # boundaries
            if character_rect.top < 35:
                character_rect.top = 35
            if character_rect.left < 35:
                character_rect.left = 35
            if character_rect.bottom > 365:
                character_rect.bottom = 365
            if character_rect.right > 765:
                character_rect.right = 765

            # collision
            if character_rect.colliderect(backpack_rect):
                lives -= 1  # lose a life
                print(f"Collision! Lives left: {lives}")
                # reset backpack position
                backpack_rect.x = 675
                backpack_rect.y = random.randint(100, 250)

        else:
            # show success or game over
            if lives > 0:
                message = "Level Success! Time up!"
                end_text = font.render(message, True, (0, 0, 0))
                screen.blit(end_text, (250, 180))
            else:
                message = "Game Over!"
                end_text = font.render(message, True, (255, 0, 0))
                screen.blit(end_text, (300, 180))

        # timer display
        remaining_time = max(0, (GAME_DURATION - elapsed_time) // 1000)
        timer_text = font.render(f"Time left: {remaining_time}", True, (0, 0, 0))
        screen.blit(timer_text, (300, 10))

        # lives display 
        for i in range(lives):
            screen.blit(heart_surf, (10 + i*35, 10))  # spacing 35 px between hearts

    pygame.display.update()
    clock.tick(60)
    
    
    