import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)


def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])

pygame.init()

def volume_sphere(radius):
    pi = 3.141592653589
    volume = (4 / 3) * pi * radius ** 3
    print("The volume is", volume)
    
def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    print("The volume is", volume)    

# Add two numbers and return the results
def sum_two_numbers(a, b):
    result = a + b
    return result

# Function that prints the result
def sum_print(a, b):
    result = a + b
    print(result)
 
# Function that returns the results
def sum_return(a, b):
    result = a + b
    return result
 
# This prints the sum of 4+4
sum_print(4, 4)
 
# This does not
sum_return(4, 4)
 
# This will not set x1 to the sum
# It actually gets a value of 'None'
x1 = sum_print(4, 4)
 
# This will
x2 = sum_return(4, 4)
