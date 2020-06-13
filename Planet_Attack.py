import pygame
import os

pygame.mixer.init()
pygame.init()
#set display
screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)


#load image & declare variable
background = pygame.image.load('background.png')
spaceship = pygame.image.load("spaceship.png")

#spaceship_x = 170

bullet = pygame.image.load("bullet.png")
#add bullet & fired variable
bullet_y = 500
fired = False

#planets image list & planet index
planets =['p_one.png','p_two.png','p_three.png','p_four.png','p_five.png','p_six.png', 'p_last.png']
p_index = 0
# update the planet loading logic
planet = pygame.image.load(planets[p_index])
planet_x = 140
# change planet position
move_direction = 'right'



#creating a never ending loop
keep_alive = True
# set frame rate with a clock variable
clock = pygame.time.Clock()

while keep_alive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False
    
    #Access Events with get_press method
    pygame.event.get()
    keys = pygame.key.get_pressed()
#Spacebar Event
    if keys[pygame.K_SPACE] == True:
        fired = True

    """
    if keys[pygame.K_RIGHT] == True:
        spaceship_x += 5
    
    if keys[pygame.K_LEFT] == True:
        spaceship_x -= 5
     """
# bullet animation logic here
    if fired is True:
        
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            fired = False
            bullet_y = 500
    
# display image
    screen.blit(background,[0,0])
# new bullet display with dynamic position
    screen.blit(bullet, [180, bullet_y])
    screen.blit(spaceship, [160,500])


# planet animation logic here
    if move_direction == 'right':
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = 'right'
# new planet display with dynamic position
    screen.blit(planet, [planet_x, 50])

#collision condition
    if bullet_y < 80 and planet_x > 120 and planet_x < 180:
# collision effect logic
        p_index = p_index + 1
        if p_index < len(planets):
            planet = pygame.image.load(planets[p_index])
            planet_x = 10
            
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play()
            print("Here comes the new Planet. Attack!")
        else:
            
            print('Congratulation!!! You Win!!!')
           
            keep_alive = False

#update the display
    pygame.display.update()
#add clock tick for fps
    clock.tick(70)
