import pygame
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pink = (255, 0, 221)
pine = (0, 135, 27)
brown = (77, 45, 11)
light_blue = (49, 211, 232)
dark_blue = (49, 82, 232)
yellow = (255, 238, 0) 
my_pale_ass = (255, 225, 191)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("JAM")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen,pink,[0,0,700,700],0) #background
    pygame.draw.polygon(screen, pine, [[350,100], [250,200], [450,200]])#tree
    pygame.draw.polygon(screen, pine, [[350,150], [200,300], [500,300]])
    pygame.draw.polygon(screen, pine, [[350,250], [150,400], [550,400]])
    
    pygame.draw.rect(screen, brown, [315, 400, 69, 69])#presents
    pygame.draw.rect(screen, light_blue, [300, 500, 69, 69])
    pygame.draw.rect(screen, dark_blue, [500, 460, 69, 69])
    pygame.draw.rect(screen, RED, [200, 480, 69, 69])
    pygame.draw.line(screen, GREEN, [235, 480], [235, 549], 5)
    pygame.draw.line(screen, GREEN, [200, 510], [269, 510], 5)
    pygame.draw.line(screen, dark_blue, [335, 500], [335, 569], 5)
    pygame.draw.line(screen, dark_blue, [300, 530], [369, 530], 5)
    pygame.draw.line(screen, light_blue, [535, 460], [535, 529], 5)
    pygame.draw.line(screen, light_blue, [500, 490], [569, 490], 5)
    
    pygame.draw.ellipse(screen, RED, [320,200,20,20])#ornaments
    pygame.draw.ellipse(screen, RED, [300,300,20,20])
    pygame.draw.ellipse(screen, RED, [200,370,20,20])
    pygame.draw.ellipse(screen, RED, [400,320,20,20])
    pygame.draw.ellipse(screen, RED, [380,150,20,20])
    pygame.draw.ellipse(screen, RED, [350,250,20,20])
    pygame.draw.ellipse(screen, RED, [250,260,20,20])
    pygame.draw.ellipse(screen, RED, [350,370,20,20])
    pygame.draw.ellipse(screen, RED, [290,360,20,20])
    pygame.draw.ellipse(screen, RED, [470,360,20,20])
    pygame.draw.ellipse(screen, RED, [440,270,20,20])
    pygame.draw.ellipse(screen, RED, [300,150,20,20])
    
    pygame.draw.polygon(screen, WHITE, [[350,70], [340,105], [360, 105]])#FUCK MAN IDK
    pygame.draw.ellipse(screen, my_pale_ass, [339,62,25,25])
    pygame.draw.ellipse(screen, yellow, [341,58,20,10], 2)
    pygame.draw.ellipse(screen, BLACK, [343,72,5,5])
    pygame.draw.ellipse(screen, BLACK, [355,72,5,5])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()