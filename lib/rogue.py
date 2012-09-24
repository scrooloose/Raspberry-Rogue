# We have to import some code in order to make our game work.
# This cuts down on the amount of code we have to write ourselves.
import pygame, math, sys, random, os
from os.path import abspath, dirname
from pygame.locals import *

sys.path.append(os.path.join("rogue"))
from game import *

def main():
    ''' This is the main loop of the program. It's responsible for initializing PyGame and creating a
        new game.
    '''
    while True:
        pygame.init()
        game = Game()

if __name__ == "__main__":
    # Python doesn't run any of the classes or functions when it loads a new program. That would be a 
    # mess! Instead, it looks for a bit of code that isn't a class or function and runs that. 
    #
    # This bit of code tells Python to go ahead and run the 'main' function.
    main()
