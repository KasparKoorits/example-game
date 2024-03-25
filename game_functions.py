import sys
import pygame
from bubble import Bubble

#add additional user event
pygame.init()
ADDBUBBLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBUBBLE, 250)

def check_events(game_settings, screen, player, bubbles):
    """Check keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
        elif event.type == ADDBUBBLE:
            create_bubble(game_settings, screen, bubbles)

def create_bubble(game_settings, screen, bubbles):
    new_bubble = Bubble(screen, game_settings)
    bubbles.add(new_bubble)
            

def update_screen(game_settings, screen, player, bubbles):
    """Update image on screen and draw new screen"""
    #background
    screen.fill(game_settings.bg_color)
    
    #add player to screen
    player.blit_me()
    
    #add bubbles to screen
    for bubble in bubbles:
        bubble.blit_me()
    
    #display the last screen
    pygame.display.flip()
    
