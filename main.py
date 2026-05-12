import pygame
from sys import exit
import random

pygame.init()

# screen size
screen_width = 800
screen_height = 400
door_open = False
music_collision_start_time = None

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Schooltale')
clock = pygame.time.Clock()
name_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 18)

#SOUNDS LIST
sound_intro = pygame.mixer.Sound('sounds/intro_soundtrack.mp3')
sound_f1 = pygame.mixer.Sound('sounds/f1_bully.mp3')
sound_d_f1 = pygame.mixer.Sound('sounds/f1_dial_bully.mp3')
sound_cs1 = pygame.mixer.Sound('sounds/cs1_beat.mp3')
sound_death = pygame.mixer.Sound('sounds/death_sound.mp3')
sound_hit = pygame.mixer.Sound('sounds/hit_sound.mp3')

current_state = "OUTSIDE_FREE_ROAM"

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

# SECOND HALL CUTSCENE BLACK
second_hall_cutscene1_surface1_surf = pygame.Surface((700, 100))
second_hall_cutscene1_surface1_surf.fill('black')
pygame.draw.rect(second_hall_cutscene1_surface1_surf, 'white', second_hall_cutscene1_surface1_surf.get_rect(), 3)
cutscene1_surface1_rect = second_hall_cutscene1_surface1_surf.get_rect(topleft=(50, 275))

second_hall_dialogue1 = cutscene_font.render('Phew... got away...', False, 'white')
second_hall_dialogue2 = cutscene_font.render("That idiot can't run even if his life depended on it.", False, 'white')
second_hall_dialogue3 = cutscene_font.render('Anyway, since my classes start later...', False, 'white')
second_hall_dialogue4 = cutscene_font.render('...maybe I can find a club I like.', False, 'white')
second_hall_dialogue5 = cutscene_font.render('The clubrooms should be by the end of this hall.', False, 'white')

second_hall_dialogue_rect = second_hall_dialogue1.get_rect(topleft=(20, 40))

# SECOND HALL CUTSCENE
second_hall_background_surf = pygame.image.load('images/second_hall.png')
second_hall_background_rect = second_hall_background_surf.get_rect()
second_hall_main_character_surf = pygame.image.load('images/main_character.png')
second_hall_main_character_rect = second_hall_main_character_surf.get_rect(center=(650, 200))

second_hall_cutscene_dialogue1 = cutscene_font.render('The clubrooms must be behind these doors...', False, 'white')
second_hall_cutscene_dialogue2 = cutscene_font.render("Let's see who's open...", False, 'white')

second_hall_cutscene_dialogue_rect = second_hall_cutscene_dialogue1.get_rect(topleft=(20, 40))
 
# SECOND HALL FREE ROAM
second_hall_freeroam_background_surf = pygame.image.load('images/second_hall.png')
second_hall_freeroam_background_rect = second_hall_background_surf.get_rect()
second_hall_freeroam_main_character_surf = pygame.image.load('images/main_character.png')
second_hall_freeroam_main_character_rect = second_hall_main_character_surf.get_rect(center=(650, 200))

club_dialogue_surf = pygame.Surface((700, 100))
club_dialogue_rect = club_dialogue_surf.get_rect(topleft=(50, 275))

# MUSIC ROOM
music_room_surf = pygame.image.load('images/music_room.png')
music_room_rect = music_room_surf.get_rect()

music_room_main_character_surf = pygame.image.load('images/main_character.png')
music_room_main_character_rect = music_room_main_character_surf.get_rect(center=(660, 150))

music_girl_surf = pygame.image.load('images/music_girl.png')
music_girl_rect = music_girl_surf.get_rect(center=(150, 220))

# MUSIC ROOM CUTSCENE
music_room_cutscene1_surface1_surf = pygame.Surface((700, 100))
music_room_cutscene1_surface1_surf.fill('black')
pygame.draw.rect(music_room_cutscene1_surface1_surf, 'white', music_room_cutscene1_surface1_surf.get_rect(), 3)
cutscene1_surface1_rect = music_room_cutscene1_surface1_surf.get_rect(topleft=(50, 275))

music_room_cutscene1_dialogue1_surf = cutscene_font.render('Oh hi there!', False, 'lavender')
music_room_cutscene1_dialogue2_surf = cutscene_font.render("I'm Mayumi, vocalist of the music club!", False, 'lavender')
music_room_cutscene1_dialogue3_surf = cutscene_font.render("Are you interested in joining?", False, 'lavender')
music_room_cutscene1_dialogue4_surf = cutscene_font.render("Yeah... seems interesting.", False, 'white')
music_room_cutscene1_dialogue5_surf = cutscene_font.render("Great! Though we only have room for a guitarist...", False, 'lavender')
music_room_cutscene1_dialogue6_surf = cutscene_font.render("You want it?", False, 'lavender')
music_room_cutscene1_dialogue7_surf = cutscene_font.render("Yeah, let's do it.", False, 'white')
music_room_cutscene1_dialogue8_surf = cutscene_font.render("Great! You're trying out... now!", False, 'lavender')
music_room_cutscene1_dialogue9_surf = cutscene_font.render("Wait! Not even any practice?", False, 'white')
music_room_cutscene1_dialogue10_surf = cutscene_font.render("You don't enter the music clubroom...", False, 'lavender')
music_room_cutscene1_dialogue11_surf = cutscene_font.render("...without being prepared, silly!", False, 'lavender')
music_room_cutscene1_dialogue12_surf = cutscene_font.render("Now, let it rip!", False, 'lavender')

music_room_cutscene_dialogue_rect = music_room_cutscene1_dialogue1_surf.get_rect(topleft=(20, 40))


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
            sound_intro.play(-1)
            sound_intro.set_volume(0.7)
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_intro.stop()

                sound_cs1.play(-1)
                sound_cs1.set_volume(0.7)

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
            main_character_rect.center = (700, 220)

        screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)

    # OUTSIDE PHASE
    if current_state == "OUTSIDE_PHASE":
        sound_cs1.stop()
        sound_intro.play()
        sound_intro.set_volume(0.7)
        elapsed = pygame.time.get_ticks() - cutscene_start_time
        print(elapsed)

        screen.blit(outside_background_closed_surf, outside_background_rect)
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
            main_character_rect.center = (700, 220)

        screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)

    # FREE ROAM
    if current_state == "OUTSIDE_FREE_ROAM":
        if door_open:
            screen.blit(outside_background_open_surf, outside_background_rect)
        else:
            screen.blit(outside_background_closed_surf, outside_background_rect)
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
        if main_character_rect.top < 40:
            main_character_rect.top = 40
        if main_character_rect.left < 0:
            main_character_rect.left = 0
        if main_character_rect.bottom > screen_height:
            main_character_rect.bottom = screen_height
        if main_character_rect.right > screen_width:
            main_character_rect.right = screen_width

        door_collision_rect = pygame.Rect(270, 75, 180, 10)
        if main_character_rect.colliderect(door_collision_rect):
            door_open = True

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
                door_open = False
        else:
            door_open = False

    if current_state == "INSIDE_CUTSCENE":
        sound_intro.stop()
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
            sound_d_f1.play()
    
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
            sound_d_f1.stop()
            sound_f1.play(-1)

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
                sound_hit.play(1)
                backpack_rect.x = 675
                backpack_rect.y = random.randint(100, 250)

        else:
            if lives <= 0:
                current_state = "GAME_OVER"
                sound_death.play()
                sound_f1.stop()
            elif elapsed_time >= GAME_DURATION:
                current_state = "SECOND_HALLWAY_CUTSCENE_BLACK"
                second_hall_black_start_time = pygame.time.get_ticks()  
                sound_cs1.play()
            
            continue  
        
        remaining_time = max(0, (GAME_DURATION - elapsed_time) // 1000)
        timer_font = pygame.font.Font("fonts/PixelOperator8.ttf", 20)
        timer_text = timer_font.render(f"Time left: {remaining_time}", True, (0, 0, 0))
        timer_rect = timer_text.get_rect(center=(400, 30))

        screen.blit(timer_text, timer_rect)

        for i in range(lives):
            screen.blit(heart_surf, (10 + i * 35, 10))

    if current_state == "SECOND_HALLWAY_CUTSCENE_BLACK":
        sound_f1.stop()
        screen.fill('black')
        elapsed = pygame.time.get_ticks() - second_hall_black_start_time
        print(elapsed)

        second_hall_cutscene1_surface1_surf.fill('black')
        pygame.draw.rect(second_hall_cutscene1_surface1_surf, 'white', second_hall_cutscene1_surface1_surf.get_rect(), 3)

        if 5000 < elapsed < 10000:
            name_surf = name_font.render('Kirito', False, 'white')
            second_hall_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            second_hall_cutscene1_surface1_surf.blit(second_hall_dialogue1, second_hall_dialogue_rect)
            screen.blit(second_hall_cutscene1_surface1_surf, cutscene1_surface1_rect)
        if 10000 < elapsed < 15000:
            name_surf = name_font.render('Kirito', False, 'white')
            second_hall_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            second_hall_cutscene1_surface1_surf.blit(second_hall_dialogue2, second_hall_dialogue_rect)
            screen.blit(second_hall_cutscene1_surface1_surf, cutscene1_surface1_rect)
        if 15000 < elapsed < 20000:
            name_surf = name_font.render('Kirito', False, 'white')
            second_hall_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            second_hall_cutscene1_surface1_surf.blit(second_hall_dialogue3, second_hall_dialogue_rect)
            screen.blit(second_hall_cutscene1_surface1_surf, cutscene1_surface1_rect)
        if 20000 < elapsed < 25000:
            name_surf = name_font.render('Kirito', False, 'white')
            second_hall_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            second_hall_cutscene1_surface1_surf.blit(second_hall_dialogue4, second_hall_dialogue_rect)
            screen.blit(second_hall_cutscene1_surface1_surf, cutscene1_surface1_rect)
        if 25000 < elapsed < 30000:
            name_surf = name_font.render('Kirito', False, 'white')
            second_hall_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            second_hall_cutscene1_surface1_surf.blit(second_hall_dialogue5, second_hall_dialogue_rect)
            screen.blit(second_hall_cutscene1_surface1_surf, cutscene1_surface1_rect)
        if elapsed > 30000:
            current_state = "SECOND_HALLWAY_CUTSCENE"
            second_hall_cutscene_start_time = pygame.time.get_ticks()
            sound_cs1.stop()
            sound_intro.play(-1)

    if current_state == "SECOND_HALLWAY_CUTSCENE":
        elapsed = pygame.time.get_ticks() - second_hall_cutscene_start_time
        print(elapsed)
        
        screen.blit(second_hall_background_surf, second_hall_background_rect)
        screen.blit(second_hall_main_character_surf, second_hall_main_character_rect)

        cutscene1_surface1_surf.fill('black')
        pygame.draw.rect(cutscene1_surface1_surf, 'white', cutscene1_surface1_surf.get_rect(), 3)
        name_surf = name_font.render('Kirito', False, 'white')
        cutscene1_surface1_surf.blit(name_surf, (20, 10))

        if elapsed < 5000:
            cutscene1_surface1_surf.blit(second_hall_cutscene_dialogue1, second_hall_cutscene_dialogue_rect)
        elif 5000 < elapsed < 10000:
            cutscene1_surface1_surf.blit(second_hall_cutscene_dialogue2, second_hall_cutscene_dialogue_rect)

        screen.blit(cutscene1_surface1_surf, cutscene1_surface1_rect)

        if elapsed > 10000:
            current_state = "SECOND_HALLWAY_FREEROAM"

    if current_state == "SECOND_HALLWAY_FREEROAM":
        screen.blit(second_hall_background_surf, second_hall_background_rect)
        screen.blit(second_hall_main_character_surf, second_hall_main_character_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            second_hall_main_character_rect.y -= 5
        if keys[pygame.K_a]:
            second_hall_main_character_rect.x -= 5
        if keys[pygame.K_s]:
            second_hall_main_character_rect.y += 5
        if keys[pygame.K_d]:
            second_hall_main_character_rect.x += 5

        if second_hall_main_character_rect.top < 45:
            second_hall_main_character_rect.top = 45
        if second_hall_main_character_rect.left < 120:
            second_hall_main_character_rect.left = 120
        if second_hall_main_character_rect.bottom > 385:
            second_hall_main_character_rect.bottom = 385
        if second_hall_main_character_rect.right > 660:
            second_hall_main_character_rect.right = 660

        robotics_door_collision_rect = pygame.Rect(340, 55, 120, 10)    
        esports_door_collision_rect = pygame.Rect(195, 55, 100, 10)
        theater_door_collision_rect = pygame.Rect(500, 55, 100, 10)
        music_door_collision_rect = pygame.Rect(120, 170, 30, 20)

        if second_hall_main_character_rect.colliderect(robotics_door_collision_rect):
            robotics_text = cutscene_font.render("It says: 'Robotics Club: Meeting in progress.'", False, 'white')
            club_dialogue_surf.fill('black')
            pygame.draw.rect(club_dialogue_surf, 'white',club_dialogue_surf.get_rect(), 3)
            name_surf = name_font.render('Kirito', False, 'white')
            club_dialogue_surf.blit(name_surf, (20, 10))
            club_dialogue_surf.blit(robotics_text, (20, 40))
            screen.blit(club_dialogue_surf, club_dialogue_rect)

        if second_hall_main_character_rect.colliderect(esports_door_collision_rect):
            esports_text = cutscene_font.render("It says: 'Esports Club: Sorry, were full.'", False, 'white')
            club_dialogue_surf.fill('black')
            pygame.draw.rect(club_dialogue_surf, 'white',club_dialogue_surf.get_rect(), 3)
            name_surf = name_font.render('Kirito', False, 'white')
            club_dialogue_surf.blit(name_surf, (20, 10))
            club_dialogue_surf.blit(esports_text, (20, 40))
            screen.blit(club_dialogue_surf, club_dialogue_rect)

        if second_hall_main_character_rect.colliderect(theater_door_collision_rect):
            theater_text = cutscene_font.render("It says: 'Theater Club: Tryouts are next week!'", False, 'white')
            club_dialogue_surf.fill('black')
            pygame.draw.rect(club_dialogue_surf, 'white',club_dialogue_surf.get_rect(), 3)
            name_surf = name_font.render('Kirito', False, 'white')
            club_dialogue_surf.blit(name_surf, (20, 10))
            club_dialogue_surf.blit(theater_text, (20, 40))
            screen.blit(club_dialogue_surf, club_dialogue_rect)

        if second_hall_main_character_rect.colliderect(music_door_collision_rect):
            print("collision")
            if music_collision_start_time is None:
                music_collision_start_time = pygame.time.get_ticks()

            elapsed = pygame.time.get_ticks() - music_collision_start_time
            print(elapsed)

            if elapsed < 5000:
                music_text1 = cutscene_font.render("It says: 'Music Club: We're recruiting now!'", False, 'white')
                club_dialogue_surf.fill('black')
                pygame.draw.rect(club_dialogue_surf, 'white',club_dialogue_surf.get_rect(), 3)
                name_surf = name_font.render('Kirito', False, 'white')
                club_dialogue_surf.blit(name_surf, (20, 10))
                club_dialogue_surf.blit(music_text1, (20, 40))
                screen.blit(club_dialogue_surf, club_dialogue_rect)
            elif 5000 < elapsed < 10000:
                music_text2 = cutscene_font.render("Hmm... maybe it could be worth a try...", False, 'white')
                club_dialogue_surf.fill('black')
                pygame.draw.rect(club_dialogue_surf, 'white',club_dialogue_surf.get_rect(), 3)
                name_surf = name_font.render('Kirito', False, 'white')
                club_dialogue_surf.blit(name_surf, (20, 10))
                club_dialogue_surf.blit(music_text2, (20, 40))
                screen.blit(club_dialogue_surf, club_dialogue_rect)
            elif elapsed > 10000:
                current_state = "MUSIC_ROOM"
                screen.fill('black')
        else:
            music_collision_start_time = None

    if current_state == "MUSIC_ROOM":
        screen.blit(music_room_surf, music_room_rect)
        screen.blit(music_room_main_character_surf, music_room_main_character_rect)
        screen.blit(music_girl_surf, music_girl_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            music_room_main_character_rect.y -= 5
        if keys[pygame.K_a]:
            music_room_main_character_rect.x -= 5
        if keys[pygame.K_s]:
            music_room_main_character_rect.y += 5
        if keys[pygame.K_d]:
            music_room_main_character_rect.x += 5

        if music_room_main_character_rect.top < 75:
            music_room_main_character_rect.top = 75
        if music_room_main_character_rect.left < 140:
            music_room_main_character_rect.left = 140
        if music_room_main_character_rect.bottom > 375:
            music_room_main_character_rect.bottom = 375
        if music_room_main_character_rect.right > 660:
            music_room_main_character_rect.right = 660

        if music_room_main_character_rect.colliderect(music_girl_rect):
            current_state = "MUSIC_ROOM_CUTSCENE"
            music_room_cutscene_start_time = pygame.time.get_ticks()
            sound_intro.stop()


    if current_state == "MUSIC_ROOM_CUTSCENE":
        elapsed = pygame.time.get_ticks() - music_room_cutscene_start_time

        music_room_cutscene1_surface1_surf.fill('black')
        pygame.draw.rect(music_room_cutscene1_surface1_surf, 'white', music_room_cutscene1_surface1_surf.get_rect(), 3)

        if elapsed < 4000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue1_surf, music_room_cutscene_dialogue_rect)

        if 4000 < elapsed < 8000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue2_surf, music_room_cutscene_dialogue_rect)
        
        if 8000 < elapsed < 12000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue3_surf, music_room_cutscene_dialogue_rect)
        
        if 12000 < elapsed < 16000:
            name_surf = name_font.render('Kirito', False, 'white')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue4_surf, music_room_cutscene_dialogue_rect)

        if 16000 < elapsed < 20000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue5_surf, music_room_cutscene_dialogue_rect)

        if 20000 < elapsed < 24000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue6_surf, music_room_cutscene_dialogue_rect)

        if 24000 < elapsed < 28000:
            name_surf = name_font.render('Kirito', False, 'white')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue7_surf, music_room_cutscene_dialogue_rect)

        if 28000 < elapsed < 32000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue8_surf, music_room_cutscene_dialogue_rect)

        if 32000 < elapsed < 36000:
            name_surf = name_font.render('Kirito', False, 'white')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue9_surf, music_room_cutscene_dialogue_rect)

        if 36000 < elapsed < 40000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue10_surf, music_room_cutscene_dialogue_rect)

        if 40000 < elapsed < 44000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue11_surf, music_room_cutscene_dialogue_rect)
        
        if 44000 < elapsed < 48000:
            name_surf = name_font.render('Mayumi', False, 'lavender')
            music_room_cutscene1_surface1_surf.blit(name_surf, (20, 10))
            music_room_cutscene1_surface1_surf.blit(music_room_cutscene1_dialogue12_surf, music_room_cutscene_dialogue_rect)
        
        screen.blit(music_room_cutscene1_surface1_surf, cutscene1_surface1_rect)

        if elapsed > 48000:
            current_state = "FIGHT_2"

    if current_state == "FIGHT_2":
        screen.fill('black')

    if current_state == "VICTORY":
        screen.fill("black")

        victory_font = pygame.font.Font("fonts/PixelOperatorHB8.ttf", 50)
        victory_text = victory_font.render("VICTORY!", True, (0, 255, 0))

        victory_font2 = pygame.font.Font("fonts/PixelOperator8.ttf", 20)
        victory_text2 = victory_font2.render("Thanks for playing the demo!", True, (255, 255, 255))

        # blinking text
        t = pygame.time.get_ticks()
        blink = (t // 500) % 2
        color = (200, 200, 200) if blink else (255, 255, 255)

        victory_text3 = victory_font2.render("Click to return to menu", True, color)

        victory_rect = victory_text.get_rect(center=(400, 150))
        victory_rect2 = victory_text2.get_rect(center=(400, 220))
        victory_rect3 = victory_text3.get_rect(center=(400, 280))

        screen.blit(victory_text, victory_rect)
        screen.blit(victory_text2, victory_rect2)
        screen.blit(victory_text3, victory_rect3)

        if pygame.mouse.get_pressed()[0]:
            current_state = "MENU"
            door_open = False
            outside_rect = main_character_surf.get_rect(center=(700, 220))
            inside_rect = main_character_surf.get_rect(center=(700, 220))

    if current_state == "GAME_OVER":
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

        if pygame.mouse.get_pressed()[0]:
            current_state = "MENU"  
            outside_rect = main_character_surf.get_rect(center=(700, 220))
            inside_rect = main_character_surf.get_rect(center=(700, 220))
            door_open = False

    pygame.display.update()
    clock.tick(60)