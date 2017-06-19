import pygame

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 190, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BROWN = (165, 42, 32)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Picture")

done = False

clock = pygame.time.Clock()


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
  
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    #tree
    pygame.draw.polygon(screen, DARK_GREEN, [[350,50], [200,200], [500,200]])
    pygame.draw.polygon(screen, DARK_GREEN, [[350,100], [150,300], [550,300]])
    pygame.draw.polygon(screen, DARK_GREEN, [[350,150], [100,400], [600,400]])
    pygame.draw.rect(screen,BROWN,[300,400,100,200])
    
    #ornaments
    pygame.draw.ellipse(screen, RED, [450,300,30,30])
    pygame.draw.ellipse(screen, BLUE, [425,234,30,30])
    pygame.draw.ellipse(screen, YELLOW, [200,300,30,30])
    pygame.draw.ellipse(screen, RED, [340,75,30,30])
    pygame.draw.ellipse(screen, BLUE, [300,300,30,30])
    pygame.draw.ellipse(screen, BLUE, [200,195,30,30])
    pygame.draw.ellipse(screen, YELLOW, [530,300,30,30])
    pygame.draw.ellipse(screen, RED, [320,200,30,30])
    
    #presents
    pygame.draw.rect(screen, RED, [450, 420, 75, 75])
    pygame.draw.rect(screen, GREEN, [100, 420, 75, 75])
    pygame.draw.rect(screen, BLUE, [200, 410, 75, 75])
    pygame.draw.line(screen, YELLOW, [450, 457.5], [525, 457.5], 10)
    pygame.draw.line(screen, YELLOW, [487.5, 420], [487.5, 495], 10)
    pygame.draw.line(screen, BLUE, [100, 457.5], [175, 457.5], 10)
    pygame.draw.line(screen, BLUE, [137.5, 420], [137.5, 495], 10)    
    pygame.draw.line(screen, RED, [237.5, 410], [237.5, 485], 10)
    pygame.draw.line(screen, RED, [200, 447.5], [275, 447.5], 10)       
    
    pygame.display.flip()
 
 
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

   




