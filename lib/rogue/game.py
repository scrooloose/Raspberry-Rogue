import pygame, math, sys, random, os
from pygame.locals import *

from game_screen import *
from game import *
from map import *
from constants import *

class Game(object):
    ''' Game is responsible for running most of the game's actions. It's responsible for moving,
        telling GameScreen to draw the screen, and contains the main loop for the game. 

        Think of Game as the thing that coordinates all the parts of the game.
        '''
    def __init__(self):
        ''' This does the initial set-up for the game. It defines the screen and map, then calls 
            the main loop for the game.
        '''
        # Set up the screen
        self.screen = GameScreen()

        # Set up some game components
        self.map = Map()

        # Run the game!
        self.run()

    def move(self, hor, vert):
        ''' This function takes a pair of horizontal and vertical values and moves the rogue a space
            if possible. If the rogue is a the edge of the board, it can't move, so the program returns 
            to the main loop.
        '''
        # Get the current location of the rogue and save the row and column to two variables.
        self.old_row, self.old_col = self.map.player

        # Add the amount we want to move the rogue to the current row and column.
        row = self.old_row + hor
        col = self.old_col + vert

        # Are we running into the edge of the board? If so, go ahead and return to the main loop.
        # We won't move the rogue.
        if row > (ROWS-1) * TILE_SIZE or row < 0 or col > (COLUMNS-1) * TILE_SIZE or col < 0:
            return

        # Set the current position of the rogue to the new row and column values.
        self.map.set_current_position([row, col])

    def run(self):
        ''' The main loop of the game. The block of code under 'while 1' will run until the user
            hits the ESC key.
        '''
        # We need to set the amount we're moving to zero, both for the horizontal and vertical. 
        hor = 0
        vert = 0
        while 1:
            # Every time you hit a key in PyGame, PyGame captures that as an event. The event stores what
            # keys you hit, where you moved your mouse, if you clicked, etc. Here, we're getting those events
            # and only doing something if it's one of the keys we're 'listening' for. In this case, we're listening 
            # for the ESC key and the arrow keys.
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Each keystroke is measured twice. Once for the key being pressed, and once for the key being released.
                    # We're only worried about the data we get when the key is pressed down.
                    if event.key == K_ESCAPE:
                        # If we hit the escape key, quit the game.   
                        sys.exit(0)
                    if event.key == K_LEFT:
                        # If we hit the left arrow, we want to move a negative horizontal value
                        hor = -TILE_SIZE
                        vert = 0
                    if event.key == K_RIGHT:
                        # If we hit the right arrow, we want to move a positive horizontal value
                        hor = TILE_SIZE
                        vert = 0
                    if event.key == K_UP:
                        # If we hit the up arrow, we want to move a negative vertical value
                        vert = -TILE_SIZE
                        hor = 0
                    if event.key == K_DOWN:
                        # If we hit the down arrow, we want to move a positive vertical value
                        vert = TILE_SIZE
                        hor = 0
                if event.type == KEYUP:
                    # We get a KEYUP event when the player has released the key.
                    if vert or hor:
                        # If vert or hor are not zero, then the player wants to move! Go ahead and
                        # move, then reset hor and vert to zero.
                        self.move(hor, vert) 
                        hor = 0
                        vert = 0
            # Draw all the layers once the player has hit a key
            self.screen.draw_screen_layers(self.map)
