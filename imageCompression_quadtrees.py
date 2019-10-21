# Anna Krutsinger  
# October 5, 2018  
# hw4pr3.py
# collab. with louis

import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from functools import *

# A sample 8x8 image represented as a sequence of 64 bits
test1 = "0000001100001100000000110000001111111111111111111111111111111111"
test2 = "0101010101010101010101010101010100101010101010101010101010101010"  #worst case scenario
test3 = "0000000000000000000000000000000000000000000000000000000000000000"
test4 = "1110101010101010101000100010110010011001110011010111011100110100"

def powerOfTwo(num):
    """ PROVIDED CODE. """
    """ Takes a positive integer as input and returns True if and only if it is a power of two. """
    if num == 1: return True
    elif num % 2 == 1: return False
    else: return powerOfTwo(num//2)

def pngToArray(filename, threshold=2):
    """ PROVIDED CODE. """
    """ Takes a filename as input, where the file is a .png image, and returns a binary
    2D array as output.  The image must be a square whose dimensions are a power of two. """
    img=mpimg.imread(filename)  # read in the image
    dimensions = img.shape  # Get the dimensions
    rows = dimensions[0]    # Extract the number of rows...
    columns = dimensions[1] # ... and columns
    if rows != columns or not powerOfTwo(rows):  # check if the image is of appropriate dimensions
        return None  
    array = []  # start building the output array
    for r in range(rows):
        row = []
        for c in range(columns):
            if sum(img[r][c]) >= threshold:
                row.append(0)
            else:
                row.append(1)
        array.append(row)
    return array

def renderASCII(array):
    """ PROVIDED CODE. """
    """ Takes a 2D array of 0's and 1's as input and renders it as 0's and 1's on the screen  """
    for row in array:
        stringify = reduce(lambda X, Y: str(X) + str(Y), row)
        print(stringify)
            
def renderImage(array):
    """ PROVIDED CODE. """
    """ Takes a 2D array of 0's and 1's as input and renders it on the screen using matplotlib. """
    dim = len(array)
    image = np.zeros((dim, dim), dtype = np.float)
    for r in range(dim):
        for c in range(dim):
            image[r][c] = float(array[r][c]) 
    plt.imshow(image, cmap="Greys", interpolation='nearest')
    plt.show()
    
def stringToArray(bstring):
    """ PROVIDED CODE. """
    """ Takes a binary string as input and returns the 2D array representation of the image. """
    dim = int(math.sqrt(len(bstring)))
    charArray = [list(bstring[i:i+dim]) for i in range(0, len(bstring), dim)]
    array = [ [int(x) for x in row] for row in charArray ]
    return array

def quadrants(array):
    """ Takes an array of bits as input and returns a list of quadrants
    of the form [NW, NE, SW, SE] where each entry is the array 
    for that quadrant """
    if array == []:
        return []
    else:
        x = len(array)//2
        top = array[:x]
        bot = array[x:]
        NW = [top[i][:x] for i in range(x)] 
        NE = [top[i][x:] for i in range(x)]
        SW = [bot[i][:x] for i in range(x)]
        SE = [bot[i][x:] for i in range(x)]
        return [NW, NE, SW, SE]


def solidzero(array):
    """ Takes a 2D binary array as input and returns True if every bit is a 0 and False otherwise. """
    return min(list(map(lambda x: True if max(x) == 0 else False, array)))

def solidone(array):
    """ Takes a 2D binary array as input and returns True if every bit is a 1 and False otherwise. """
    return min(list(map(lambda x: False if min(x) == 0 else True, array)))

def makeQuadtree(array):
    """ Returns a quadtree representation of the array."""
    if array == []:
        return array
    else:
        quadtree = quadrants(array)
        check = lambda x: 1 if solidone(x) else 0 if solidzero(x) else makeQuadtree(x)
        return list(map(check, quadtree))

def solidArray(value, pixels):
    """ PROVIDED CODE. """
    """ Takes a value (0 or 1) and a number of pixels and retursn a 2D array of picelsxpixels
    bits all of which are set to the given value. """
    return [[value]*pixels for row in range(pixels)]

def makeArray(quadtree, dim):
    """ Takes a quadree and dimension as input and
    returns the 2D array representation of the quadtree """
    # You'll write this code
    if quadtree == []:
        return []
    elif quadtree == 0:
        return solidArray(0, dim)
    elif quadtree == 1:
        return solidArray(1, dim)
    else:
        # goes through each quadtree and as long as dim > 1, more quad trees will be made
        quadrants = list(map(lambda x: makeArray(quadtree[x], dim//2), range(len(quadtree)))) 
        top = list(map(lambda x: quadrants[0][x] + quadrants[1][x], range(len(quadrants[0]))))
        bot = list(map(lambda x: quadrants[2][x] + quadrants[3][x], range(len(quadrants[2]))))
        array = top + bot
        return array

def rotateRight(quadtree):
    """ Takes a quadtuple as input and returns the quadtree that results when rotating that image
    clockwise 90 degrees. """
    if type(quadtree)==int:
        return quadtree
    else:
        return [rotateRight(quadtree[2]), rotateRight(quadtree[0]), 
        rotateRight(quadtree[3]), rotateRight(quadtree[1])]
    

def flipHorizontal(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping the image
    about the horizontal axis of symmetry. """
    if type(quadtree)==int:
        return quadtree
    else:
        return [flipHorizontal(quadtree[2]), flipHorizontal(quadtree[3]), 
        flipHorizontal(quadtree[0]), flipHorizontal(quadtree[1])]


def flipDiagonal(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping the image
    about the diagonal line through the NE and SW corners of the image. """
    if type(quadtree)==int:
        return quadtree
    else:
        return [flipDiagonal(quadtree[3]), flipDiagonal(quadtree[1]), 
        flipDiagonal(quadtree[2]), flipDiagonal(quadtree[0])]

def invert(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping every white
    pixel to a black pixel and vice versa. """
    if quadtree == 0:
        return 1
    elif quadtree == 1:
        return 0
    else: 
        return list(map(lambda x: invert(x), quadtree))