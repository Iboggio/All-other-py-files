#IMPORT LIBRARIES
import pygame
import glob
import time
import os.path
from random import randint
from pygame.locals import *

#INITIATE PYGAME
pygame.init()

#SET SCREEN RESOLUTION
global width
width = 800
global height
height = (width /16)*9
screen = pygame.display.set_mode((width,height))

icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)

#SET WINDOW TITLE
pygame.display.set_caption('Press Space')

clock = pygame.time.Clock()
fps_target = 60
fps = fps_target

class enviroment:
    def __init__(self):
        self.x=0
        self.groundy = height*0.75
        self.stars = pygame.image.load("sprites/stars.png")
        self.buildings = pygame.image.load("sprites/buildings.png")
        
    def update(self):
        #SKY
        pygame.draw.rect(screen, (0,51,102),(0,0,width,self.groundy))
        screen.blit(self.stars,(self.x*0.05,0))
        #BUILDINGS
        x=(self.x*0.08)+500
        y=self.groundy-328
        screen.blit(self.buildings,(x,y))
        #GROUND
        pygame.draw.rect(screen, (50,50,50),(0,self.groundy,width,height))
        
        #HIGH SCRORE
        high_score = fetchHigh()
        if len(high_score) == 1:
            high_score = '%s%s' % ("000",high_score)
        elif len(high_score) == 2:
            high_score = '%s%s' % ("00",high_score)
        elif len(high_score) == 3:
            high_score = '%s%s' % ("0",high_score)
        else:
            high_score = str("MAX")
            
        high_score = '%s%s' % ("HIGH:",high_score)
        text(high_score,20,730,2)
        
class player:
    def __init__(self):
        self.sprites = glob.glob("sprites/player/*.png")
        self.h = 68
        self.w = 56
        self.x = 40
        self.y = enviroment.groundy-self.h
        self.oy = self.y
        self.jump = 0
        self.jumptime = 0
        self.animationTime = 0
        self.animationCount = -1
        self.jumHeight = self.oy - self.h*1.2
        self.fallTo = self.oy
        
    def move(self):
        #ON PLATFORM
        if ((self.x + self.w) > (platforms[0].x + enviroment.x) and (self.x + 19) < (platforms[0].x+platforms[0].w) + enviroment.x):
            if self.y + self.h < platforms[0].y:
                onPlatform = "on"
            else:
                onPlatform = "under"
        #NOT ON PLATFORM
        else:
            onPlatform = "else"

        #IF ON PLATFORM
        if onPlatform == "on":
            self.fallTo = 214
            if self.y == 214:
                self.jumpHeight = self.fallTo - self.h*1.2

        #IF UNDER PLATFORM
        elif onPlatform == "under":
            self.fallTo = self.oy
            self.jumpHeight = platforms[0].y

        #IF NOT UNDER NOR PLATFORM
        else:
            self.fallTo = self.oy
            if self.jump == 0:
                self.jumpHeight = self.fallTo - self.h*1.2
            if self.y < self.oy and not self.jump == 1:
                self.jump = 2
        
        #JUMP
        if self.jump == 1 and self.jumptime < time.time():
            self.y -= self.h/7
            self.jumptime = time.time() + 0.01
            #HEIGHT OF JUMP
            if self.y < self.jumpHeight:
                self.jump = 2
        #FALL
        if self.jump == 2 and self.jumptime < time.time():
            self.y += self.h/10
            self.jumptime = time.time() + 0.01
            if self.y > self.fallTo:
                self.y = self.fallTo
                self.jump = 0

        #IF DEAD, LIE ON GROUND
        if self.animationCount == 3:
            player.y = enviroment.groundy-55
                
    def touchingWall(self):
        if ((self.x + self.w) > (walls[0].x + enviroment.x) and (self.x + 19)< (walls[0].x+walls[0].w) + enviroment.x):
            if not (self.y + self.h) < (walls[0].y+10):
                return True
            else:
                return False
        else:
            return False
 
    def update(self):
        player.move()
        #ANIMATION SPEED
        if time.time() > self.animationTime + 0.07:
            self.animationCount += 1
            self.animationTime = time.time()
            if self.animationCount > 3:
                self.animationCount = 3
            elif self.animationCount > 2:
                self.animationCount = 0
        image = pygame.image.load(self.sprites[self.animationCount])
        screen.blit(image,(self.x,self.y))
        
class wall:
    def __init__(self,name):
        self.name = name
        self.x = randint(width,width+(width/2)) - enviroment.x
        self.w = 24
        self.h = 47
        self.y = enviroment.groundy-self.h
        
    def update(self):
        relative_x = self.x + enviroment.x
        pygame.draw.rect(screen, (74,250,115),(relative_x,self.y,self.w,self.h))
  
class platform:
    def __init__(self,name):
        self.name = name
        self.x = randint(width,width+(width/2)) - enviroment.x
        self.w = randint(100,300)
        self.h = 8
        self.y = enviroment.groundy-55
        
    def update(self):
        relative_x = self.x + enviroment.x
        pygame.draw.rect(screen, (250,74,74),(relative_x,self.y,self.w,self.h))

def updateLabels():
    font = pygame.font.Font(None, 15)
    
    colour=(255,255,255)
    text = '%s%s' % ( fps," fps")
    label = font.render(text, 1, colour)
    screen.blit(label, (5,2))
    
    colour=(255,255,255)
    text = '%s%s' % ( "Enviroment x: ",int(enviroment.x))
    label = font.render(text, 1, colour)
    screen.blit(label, (5,12))
    
    colour=(255,255,255)
    text = '%s%s%s%s' % ( "Walls: ",len(walls),", Platforms: ",len(platforms))
    label = font.render(text, 1, colour)
    screen.blit(label, (5,22))
    
    colour=(255,255,255)
    text = '%s%s' % ( "player.y:",player.y)
    label = font.render(text, 1, colour)
    screen.blit(label, (5,32))
    
    pygame.draw.rect(screen, (0,255,0),((player.x + 19),(player.y + 17),(player.w-19),51),1)

def text(text,size,x,y):
    startfont = pygame.font.SysFont("gillsansmt", size)
    label = startfont.render(text, 1, (255,255,255))
    screen.blit(label, (x,y))

walls = []
def newWall():
    name = '%s%s' % ("wall",time.time())
    name = wall(name)
    walls.append(name)
    
platforms = []
def newPlatform():
    name = '%s%s' % ("platform",time.time())
    name = platform(name)
    platforms.append(name)
    
def updateScreen():
    enviroment.update()

    for i in range(len(walls)):
        walls[i].update()
        
    for i in range(len(platforms)):
        platforms[i].update()
        
    player.update()
    
    if label_toggle:
        updateLabels()

def reset():
    enviroment.x = 0
    walls[0].x = randint(width,width+(width/2)) - enviroment.x
    platforms[0].x = randint(width,width+(width/2)) - enviroment.x
    player.jump = 0
    player.y = enviroment.groundy-player.h
    updateScreen()

def fetchHigh():
    if os.path.isfile("bin/high_score.bin"):
        file = open("bin/high_score.bin","r")
        score = file.read()
        file.close
    else:
        saveHigh(0)
        score = fetchHigh()
    return score

def saveHigh(score):
    score = str(score)
    file = open("bin/high_score.bin","w")
    file.write(score)
    file.close()

def endGameMessage():
    if os.path.isfile("bin/end_game_messages.txt"):
        f = open("bin/end_game_messages.txt","r")
        messages = []
        for line in f:
             messages.append(line.rstrip('\n'))
        f.close
        message = messages[randint(0,len(messages)-1)]
    else:
        message = "Now you're dead"
    return message
    
#INIT CLASSES AND VARIABLES
enviroment = enviroment()
newWall()
newPlatform()
player = player()
label_toggle = False
game_over = False
main_loop = True
main_game = False
#reset()
while main_loop:
    #START SCREEN
        reset()
        text("Press Space.",101,(player.x + 70), (player.y + 12))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_loop = False

            if event.type == KEYDOWN and event.key == K_SPACE:
                main_game = True
                player.jump = 1
                
            if event.type == KEYDOWN and event.key == K_l:
                if label_toggle == False:
                    time.sleep(0.1)
                    label_toggle = True
                else:
                    time.sleep(0.1)
                    label_toggle = False
                updateScreen()

        #MAIN GAME
        while main_game:
            #QUIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_loop = False
                    main_game = False

            #INPUT
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if player.jump == 0:
                        player.jump = 1
                    
                if event.type == KEYDOWN and event.key == K_p:
                    #PAUSE
                        pause = True
                        while pause:
                            text("Paused, Press Space.",90,(player.x + 70), (player.y + 19))
                            pygame.display.flip()
                            updateScreen()
         
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pause = False
                                    main_game = False
                                    main_loop = False

                                if event.type == KEYDOWN and event.key == K_SPACE:
                                    pause = False
                                    
                                if event.type == KEYDOWN and event.key == K_p:
                                    pause = False
                                        
                                if event.type == KEYDOWN and event.key == K_r:
                                    reset()

            #lOGIC
            #SCROLL SPEED 8 IS OPTIMUM
            enviroment.x -=8
            
            #CREATE NEW OBSTACLES
            if walls[-1].x + enviroment.x < width*0.66:
                    newWall()
                
            if platforms[-1].x + enviroment.x < width*0.10:
                newPlatform()
                
            #DELETE OFF SCREEN OBSTACLES
            if walls[0].x + enviroment.x < 0:
                del walls[0]

            if (platforms[0].x + platforms[0].w) + enviroment.x < 0:
                del platforms[0]

            if player.touchingWall():
                main_game = False
                game_over = True
                message = endGameMessage()

            #DRAW SCREEN
            updateScreen()
            label = '%s%s' % (int(enviroment.x*-0.01), "m")
            text(label,120,(width*0.5-80), (height*0.13))
            pygame.display.flip()

            #CLOCK
            clock.tick(fps_target)
            fps = int(clock.get_fps())
            
        #GAME OVER
        while game_over:
            if int(enviroment.x*-0.01) > int(fetchHigh()):
                   saveHigh(int(enviroment.x*-0.01))
            
            player.animationCount = 3
            player.jump = 0
            text(message,101,(player.x + 70), (player.y - 1))
            
            label = '%s%s' % (int(enviroment.x*-0.01), "m")
            text(label,120,(width*0.5-80), (height*0.13))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_loop = False
                    game_over = False
                    
                if event.type == KEYDOWN and event.key == K_SPACE:
                    player.animationCount = -1
                    walls = []
                    newWall()
                    game_over = False
            updateScreen() 

pygame.quit()

