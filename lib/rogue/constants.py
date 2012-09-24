from os.path import abspath, dirname

# These are our constants. They can be called from anywhere in the program.
# Here, we're telling Python where to find our image files, how many columns
# and rows our board has, and how many pixels high and wide our tiles are.
IMG_DIR = dirname(dirname(abspath(__file__))) + "/media/"
COLUMNS = 16
ROWS = 21
TILE_SIZE = 48
