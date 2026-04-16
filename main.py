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
name_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 18)

current_state = "MENU"

# MENU
title_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 55)
title_surf = title_font.render('SCHOOLTALE', False, 'white')
title_rect = title_surf.get_rect(center=(400, 150))

# CUTSCENE1
cutscene1_surface1_surf = pygame.Surface((700, 100))
cutscene1_surface1_surf.fill('black')
pygame.draw.rect(cutscene1_surface1_surf, 'white', cutscene1_surface1_surf.get_rect(), 3)
cutscene1_surface1_rect = cutscene1_surface1_surf.get_rect(topleft=(50, 275))

cutscene_font = pygame.font.Font("fonts/PixelOperator8.ttf", 15)
dialogue_1_surf = cutscene_font.render('I really do not want to be here...', False, 'white')
dialogue_2_surf = cutscene_font.render("Seriously, what does changing schools even do?", False, 'white')
dialogue_3_surf = cutscene_font.render('...', False, 'white')
dialogue_4_surf = cutscene_font.render('Fine, maybe third times the charm...', False, 'white')

dialogue_rect = dialogue_1_surf.get_rect(topleft=(20, 40))

# OUTSIDE_CUTSCENE
outside_background_surf = pygame.image.load('images/outside_bg.png')
outside_background_rect = outside_background_surf.get_rect()

outside_background_open_surf = pygame.image.load('images/Door_Open.png')
outside_background_closed_surf = pygame.image.load('images/outside_bg.png')

prompt_surf = pygame.Surface((300, 100))
prompt_surf_rect = prompt_surf.get_rect(center=(400, 200))
prompt_surf.fill((0, 0, 0, 180))

enter_school = cutscene_font.render('Enter School', False, 'white')
enter_school_rect = enter_school.get_rect(center=(400, 200))
yes_choice = cutscene_font.render('Yes', False, 'white')
yes_choice_rect = yes_choice.get_rect(center=(300, 225))
no_choice = cutscene_font.render('No', False, 'white')
no_choice_rect = no_choice.get_rect(center=(500, 225))

main_character_surf = pygame.image.load('images/main_character.png')
main_character_rect = main_character_surf.get_rect(center=(700, 220))
main_character_rect_reset = main_character_surf.get_rect(center=(700, 220))

outside_dialogue_1 = cutscene_font.render('...', False, 'white')
outside_dialogue_2 = cutscene_font.render('Okay Tomori High...', False, 'white')
outside_dialogue_3 = cutscene_font.render("Let's see what you got.", False, 'white')



# INSIDE_CUTSCENE
inside_background_surf = pygame.image.load('images/inside_bg.png')
inside_background_rect = inside_background_surf.get_rect()

bully_inside_surf = pygame.image.load('images/bully.png')
bully_inside_rect = bully_inside_surf.get_rect(center=(400, 100))

inside_dialogue_1_surf = cutscene_font.render('Hey there chump...', False, 'red')
inside_dialogue_1_rect = inside_dialogue_1_surf.get_rect(topleft=(20, 40))

inside_dialogue_2_surf = cutscene_font.render("You don't belong here.", False, 'red')
inside_dialogue_2_rect = inside_dialogue_2_surf.get_rect(topleft=(20, 40))

inside_dialogue_3_surf = cutscene_font.render("I've heard worse than that.", False, 'white')
inside_dialogue_3_rect = inside_dialogue_3_surf.get_rect(topleft=(20, 40))

inside_dialogue_4_surf = cutscene_font.render("Good. Then let's see how you handle this.", False, 'red')
inside_dialogue_4_rect = inside_dialogue_2_surf.get_rect(topleft=(20, 40))

inside_dialogue_5_surf = cutscene_font.render("Handle what?", False, 'white')
inside_dialogue_5_rect = inside_dialogue_3_surf.get_rect(topleft=(20, 40))

inside_dialogue_6_surf = cutscene_font.render("This!", False, 'red')
inside_dialogue_6_rect = inside_dialogue_2_surf.get_rect(topleft=(20, 40))

# FIGHT1
background_surf = pygame.image.load('images/wall_background.png')
background_rect = background_surf.get_rect()

gaming_surf = pygame.Surface((700, 300), pygame.SRCALPHA)
gaming_surf.fill((106, 103, 103, 128))

# CHARACTER IMAGE
character_surf = pygame.image.load('images/main_character_head.png')
character_surf = pygame.transform.scale(character_surf, (80, 90))
character_rect = character_surf.get_rect(topleft=(350,150))

# BACKPACK IMAGE
backpack_surf = pygame.image.load('images/backpack.png')
backpack_surf = pygame.transform.scale(backpack_surf, (80, 80))
backpack_rect = backpack_surf.get_rect(topleft=(675, 250))

# LIVES IMAGE
heart_surf = pygame.image.load('images/heart.png')
heart_surf = pygame.transform.scale(heart_surf, (30, 30))

GAME_DURATION = 31000
lives = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if current_state == "MENU":
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_state = "CUTSCENE1"
                cutscene_start_time = pygame.time.get_ticks()
                

    # MENU
    if current_state == "MENU":
        screen.fill('black')
        t = pygame.time.get_ticks()
        brightness = (t // 500) % 2
        color = (200, 200, 200) if brightness else (255, 255, 255)

        start_font = pygame.font.Font("fonts/PixelOperator.ttf", 20)
        start_surf = start_font.render('CLICK TO PLAY', False, color)
        start_rect = start_surf.get_rect(center=(400, 300))

        screen.blit(title_surf, title_rect)
        screen.blit(start_surf, start_rect)

    # CUTSCENE1
    if current_state == "CUTSCENE1":
        screen.fill('black')
        elapsed = pygame.time.get_ticks() - cutscene_start_time
        print(elapsed)

        cutscene1_surface1_surf.fill('black')
        pygame.draw.rect(cutscene1_surface1_surf, 'white', cutscene1_surface1_surf.get_rect(), 3)

        if 5000 < elapsed < 10000:
            name_surf = name_font.render('Kirito', False, 'white')
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(dialogue_1_surf, dialogue_rect)
        elif 10000 < elapsed < 15000:
            name_surf = name_font.render('Kirito', False, 'white')
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(dialogue_2_surf, dialogue_rect)
        elif 15000 < elapsed < 20000:
            name_surf = name_font.render('Kirito', False, 'white')
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(dialogue_3_surf, dialogue_rect)
        elif 20000 < elapsed < 25000:
            name_surf = name_font.render('Kirito', False, 'white')
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(dialogue_4_surf, dialogue_rect)
        elif elapsed > 25000:
            current_state = "OUTSIDE_PHASE"

        screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)

    # OUTSIDE PHASE
    if current_state == "OUTSIDE_PHASE":
        elapsed = pygame.time.get_ticks() - cutscene_start_time
        print(elapsed)

        screen.blit(outside_background_surf, outside_background_rect)
        screen.blit(main_character_surf, main_character_rect)

        cutscene1_surface1_surf.fill('black')
        pygame.draw.rect(cutscene1_surface1_surf, 'white', cutscene1_surface1_surf.get_rect(), 3)
        name_surf = name_font.render('Kirito', False, 'white')
        cutscene1_surface1_surf.blit(name_surf, (20, 10))

        if 25000 < elapsed < 30000:
            cutscene1_surface1_surf.blit(outside_dialogue_1, dialogue_rect)
        elif 30000 < elapsed < 35000:
            cutscene1_surface1_surf.blit(outside_dialogue_2, dialogue_rect)
        elif 35000 < elapsed < 40000:
            cutscene1_surface1_surf.blit(outside_dialogue_3, dialogue_rect)
        elif elapsed > 40000:
            current_state = "OUTSIDE_FREE_ROAM"

        screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)

    # FREE ROAM
    if current_state == "OUTSIDE_FREE_ROAM":
        screen.blit(outside_background_surf, outside_background_rect)
        screen.blit(main_character_surf, main_character_rect)

        # controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            main_character_rect.y -= 5
        if keys[pygame.K_a]:
            main_character_rect.x -= 5
        if keys[pygame.K_s]:
            main_character_rect.y += 5
        if keys[pygame.K_d]:
            main_character_rect.x += 5

        # boundaries
        if main_character_rect.top < 0:
            main_character_rect.top = 0
        if main_character_rect.left < 0:
            main_character_rect.left = 0
        if main_character_rect.bottom > screen_height:
            main_character_rect.bottom = screen_height
        if main_character_rect.right > screen_width:
            main_character_rect.right = screen_width

        door_collision_rect = pygame.Rect(270, 100, 180, 20)

        door_collision_rect = pygame.Rect(270, 75, 180, 10)
        if main_character_rect.colliderect(door_collision_rect):
            outside_background_surf = outside_background_open_surf
            screen.blit(prompt_surf, prompt_surf_rect)
            pygame.draw.rect(prompt_surf, 'white', prompt_surf.get_rect(), 3)
            screen.blit(enter_school, enter_school_rect)
            screen.blit(yes_choice, yes_choice_rect)
            screen.blit(no_choice, no_choice_rect)
            mouse_pos = pygame.mouse.get_pos()
            if yes_choice_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                current_state = "INSIDE_CUTSCENE"
                main_character_rect.center = (700, 220)
            elif no_choice_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                main_character_rect.y += 20
                current_state = "OUTSIDE_FREE_ROAM"
                outside_background_surf = outside_background_closed_surf

    if current_state == "INSIDE_CUTSCENE":
        screen.blit(inside_background_surf, inside_background_rect)
        screen.blit(bully_inside_surf, bully_inside_rect)
        screen.blit(main_character_surf, main_character_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            main_character_rect.y -= 5
        if keys[pygame.K_a]:
            main_character_rect.x -= 5
        if keys[pygame.K_s]:
            main_character_rect.y += 5
        if keys[pygame.K_d]:
            main_character_rect.x += 5

        if main_character_rect.top < 75:
            main_character_rect.top = 75
        if main_character_rect.left < 10:
            main_character_rect.left = 10
        if main_character_rect.bottom > 385:
            main_character_rect.bottom = 385
        if main_character_rect.right > 765:
            main_character_rect.right = 765

        if main_character_rect.colliderect(bully_inside_rect):
            dialogue_start_time = pygame.time.get_ticks()
            current_state = "INSIDE_DIALOGUE"
    
    if current_state == "INSIDE_DIALOGUE":
        elapsed = pygame.time.get_ticks() - dialogue_start_time
        

        cutscene1_surface1_surf.fill('black')
        pygame.draw.rect(cutscene1_surface1_surf, 'white', cutscene1_surface1_surf.get_rect(), 3)
        
        if elapsed < 4000:
            name_surf = name_font.render("Ryuga", False, "red")
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(inside_dialogue_1_surf, inside_dialogue_1_rect)
        elif elapsed < 8000:
            name_surf = name_font.render("Ryuga", False, "red")
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(inside_dialogue_2_surf, inside_dialogue_2_rect)
        elif elapsed < 12000:
            name_surf = name_font.render("Kirito", False, "white")
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(inside_dialogue_3_surf, inside_dialogue_3_rect)
        elif elapsed < 16000:
            name_surf = name_font.render("Ryuga", False, "red")
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(inside_dialogue_4_surf, inside_dialogue_4_rect)
        elif elapsed < 19000:
            name_surf = name_font.render("Kirito", False, "white")
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(inside_dialogue_5_surf, inside_dialogue_5_rect)
        elif elapsed < 20000:
            name_surf = name_font.render("Ryuga", False, "red")
            cutscene1_surface1_surf.blit(name_surf, (20, 10))
            cutscene1_surface1_surf.blit(inside_dialogue_6_surf, inside_dialogue_6_rect)
        else:
            current_state = "FIGHT1"
            start_time = pygame.time.get_ticks()
            lives = 3

        screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)

    if current_state == "FIGHT1":
        elapsed_time = pygame.time.get_ticks() - start_time

        screen.blit(background_surf, background_rect)
        screen.blit(gaming_surf, (50, 50)) 

        if elapsed_time < GAME_DURATION and lives > 0:

            screen.blit(character_surf, character_rect)
        
            if elapsed_time < 2000:
                tutorial_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 30)
                tutorial_text = tutorial_font.render("DODGE THE BACKPACKS!", True, 'red')
                tutorial_rect = tutorial_text.get_rect(center=(400, 200))
                screen.blit(tutorial_text, tutorial_rect)    

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
                lives -= 1
                print(f"Collision! Lives left: {lives}")
                backpack_rect.x = 675
                backpack_rect.y = random.randint(100, 250)

        else:
            if lives <= 0:
                current_state = "GAME_OVER"
            elif elapsed_time >= GAME_DURATION:
                current_state = "VICTORY"    
            
            continue  
        
        remaining_time = max(0, (GAME_DURATION - elapsed_time) // 1000)
        timer_font = pygame.font.Font("fonts/PixelOperator8.ttf", 20)
        timer_text = timer_font.render(f"Time left: {remaining_time}", True, (0, 0, 0))
        timer_rect = timer_text.get_rect(center=(400, 30))

        screen.blit(timer_text, timer_rect)

        for i in range(lives):
            screen.blit(heart_surf, (10 + i * 35, 10))

    elif current_state == "VICTORY":
        screen.fill("black")

        victory_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 50)
        victory_text = victory_font.render("Victory!", True, (0, 255, 0))

        victory_font2 = pygame.font.Font("fonts/PixelOperator8.ttf", 20)
        victory_text2 = victory_font2.render("Thanks for playing the demo!", True, (255, 255, 255))

        victory_rect = victory_text.get_rect(center=(400, 150))
        victory_rect2 = victory_text2.get_rect(center=(400, 220))

        screen.blit(victory_text, victory_rect)
        screen.blit(victory_text2, victory_rect2)


    elif current_state == "GAME_OVER":
        screen.fill("black")

        game_over_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 50)
        game_over_text = game_over_font.render("Game Over!", True, (255, 0, 0))

        game_over_font2 = pygame.font.Font("fonts/PixelOperator8.ttf", 20)        
        game_over_text2 = game_over_font2.render("Click to return to menu", True, (255, 255, 255))

        t = pygame.time.get_ticks()
        blink = (t // 500) % 2
        color = (200, 200, 200) if blink else (255, 255, 255)

        game_over_font2 = pygame.font.Font("fonts/PixelOperator8.ttf", 20)
        game_over_text2 = game_over_font2.render("Click to return to menu", True, color)

        game_over_rect = game_over_text.get_rect(center=(400, 150))
        game_over_rect2 = game_over_text2.get_rect(center=(400, 220))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(game_over_text2, game_over_rect2)

        main_character_rect = main_character_rect_reset

        if pygame.mouse.get_pressed()[0]:
            current_state = "MENU"  


    pygame.display.update()
    clock.tick(60)