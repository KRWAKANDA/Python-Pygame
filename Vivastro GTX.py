import pygame
from sys import exit

#Display configuration of the game screen 
def display_score():
    current_time =int( pygame.time.get_ticks() /1000) - start_time
    score_surf = test_font.render( f'score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center= (400,50))
    screen.blit(score_surf,score_rect)
    

pygame.init()
screen =pygame.display.set_mode((800,400))
pygame.display.set_caption('')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/pixeltype.ttf',50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert() 
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surf =test_font.render('MAGIC MAN',False, (64,64,64))
#score_rect =score_surf.get_rect(center =(400,50))

#This is the enemy snail added to the game. 

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect =snail_surf.get_rect(bottomright = (600,300))

#This the information containing addition of the main player on the game.
 
player_surf =pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect =player_surf.get_rect(midbottom = (80,300) )

player_gravity = 0

#Thile is a loop event that automates movement on the console through commands that include player interaction

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
        
        
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20 
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True 
                snail_rect.left = 800
                start_time = int( pygame.time.get_ticks() /1000)
    
    # screen blit is used to make rectangles appear as part of simulation
 
    if game_active:  
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,)
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #screen.blit(score_surf,(score_rect))
        display_score()
        
        snail_rect.x -=4
        if snail_rect.right <= 0:snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)
    
        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        
        #Every time the player reaches the ground,i have set for player to have collision on the ground and stand
        
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)
        screen.blit(player_surf,player_rect)
        
        #Colllisions
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill('Yellow')   
         
    #if player_rect.colliderect(snail_rect):
    #   print('collision')
   
           
    pygame.display.update()
    clock.tick(60)   
    
