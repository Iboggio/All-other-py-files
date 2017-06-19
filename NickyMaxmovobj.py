"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PI = 3.14159265

def draw_smiley_face(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, YELLOW, [x,y,100,100], 0)
 
    # Eyes
    pygame.draw.ellipse(screen, BLACK ,[60+x,30+y, 15, 22])
    pygame.draw.ellipse(screen, BLACK, [30+x,30+y, 15, 22])
 
    # Mouth
    pygame.draw.arc(screen, BLACK,  [x+13.5,y+30,75,60],    PI, 2*PI, 4)
    
# Speed in pixels per frame
x_speed = 0
y_speed = 0
     
# Current position
x_coord = 10
y_coord = 10




def draw_mad_face(screen, x_coord, y_coord):

# Head
    pygame.draw.ellipse(screen, YELLOW, [x_coord,y_coord,100,100], 0)
 
    # Eyes
    pygame.draw.ellipse(screen, BLACK ,[60+x_coord,30+y_coord, 15, 22])
    pygame.draw.ellipse(screen, BLACK, [30+x_coord,30+y_coord, 15, 22])
 
    # Mouth
    pygame.draw.line(screen, BLACK, [x_coord+20, y_coord+75], [x_coord+80, y_coord+75], 4)    
 
    




 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
pygame.mouse.set_visible(False)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
     
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
     
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
     
    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed
     
            # Draw the stick figure
              
 
    # --- Game logic should go here
    # Game logic
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    
    if x_coord > 600:
        x_coord = 600
    if y_coord > 400:
        y_coord = 400
    if x_coord < 0:
        x_coord = 0
    if y_coord < 0:
        y_coord = 0
    # Drawing section
   
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)
 
    # --- Drawing code should go here
    draw_smiley_face(screen, x, y)
    draw_mad_face(screen, x_coord, y_coord)
    
    print(x_coord,y_coord)
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()