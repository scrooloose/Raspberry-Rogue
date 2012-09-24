import pygame, math, sys, random, os
from os.path import abspath, dirname
from constants import *

class GameScreen(object):
    ''' This is our screen object! Its job is to draw everything that shows up on our
        monitor. 

        Some vocabulary you might need:
            - blit: An image that we're going to be using in our game. For example, the 
              background is one blit, while the rogue is another blit. Blits are drawn on
              top of one another, so they can cover each other up. If you have a big blit, 
              like the background, you should draw that first! Otherwise, you'll cover up 
              all of the other blits!
            - flip: Once all your blits are drawn, you need to 'flip' the screen. Why?
              Screens aren't drawn all at once: a beam of light draws them on the monitor, 
              one line at a time. To make your game more smooth, PyGame is going to store 
              the screen you're creating without displaying it. Once you're done getting your
              blits in place, you tell PyGame to show the finished screen through the 'flip'
              command.
    '''
    def __init__(self):
        ''' This sets up our game's screen. The rogue is started at block 0,0, we set
            some defaults, like our fonts, and we draw our background and our rogue.
        '''
        # Set up the screen and the fonts we're going to use
        self.screen = pygame.display.set_mode((1280, 832))
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 20)
        self.bg = pygame.image.load(IMG_DIR + 'rainbowbg.png')
        self.screen.blit(self.bg, (0,0))

        # Set up our rogue. We need to place him, load the image we're going to use for him,
        # and draw him.
        self.selected_tile = [0, 0]
        self.player_blit = pygame.image.load(IMG_DIR + 'dude.png')
        self.screen.blit(self.player_blit, self.selected_tile)

        # 'Flip' the screen, so everything we just drew shows now!
        pygame.display.flip()

    def draw_player(self, coord):
        ''' Draws the rogue at a specific coordinate on the screen. 0,0 would be at the top-left corner
            of the screen. If the tile size is 48, then a coordinate of 48, 48 would draw the rogue one block
            down from the top, and one block to the right.
        '''
        self.screen.blit(self.player_blit, coord)

    def draw_background(self):
        ''' Draws my glorious rainbow background. This always starts at 0,0.
        '''
        self.screen.blit(self.bg, (0,0))

    def draw_screen_layers(self, map):
        ''' Draws the layers of the game screen. We need to draw these in the right order
            so they don't block each other! The background is drawn first, then the player.

            Once we're done getting our blits in place, we 'flip' the screen, so Pygame knows
            to display the screen we've been setting up.
        '''
        self.draw_background()
        self.draw_player(coord=map.player)
        pygame.display.flip()
