##############################################
#              BPy Engine V0.01              # 
#            Basic pygame Engine             #
#           for learning purposes            #
#           Author: Callum Craddock          #
#           Running python 3.5.1             #
#               Version: 0.1                 #
# Subject to GNU General Public License v3.0 #
##############################################

#Import modules
import pygame, sys
from pygame.locals import *
from options import *
from map import *
import random
#from player import *

#initialize pygame
pygame.init()


#Variable for playerScore(must be above the screen setup for video driver reasons)
playerScore = -0
score = str(playerScore)


#screen Setup
screen = pygame.display.set_mode(screenRes)
pygame.display.set_caption('BPy Engine 0.01: Pickin sticks! Score: ' + score)


#player setup
#load player image
player = pygame.image.load('images\player.png').convert_alpha()
#player variable
playerPos = [0,0]



#Objective Setup
object = pygame.image.load('images\object.png').convert_alpha()
objectPos = [0,0]
objectPos[0] = (random.randint(0,19))
objectPos[1] = (random.randint(0,19))



#Game Loop
while 1:
	#Check for game event quit if yes then exit game
	for event in pygame.event.get():
		#If the player exits the game quit the application
		if event.type == QUIT:
			pygame.quit()

		#Player Controller && Basic collision (doesn't leave the window)
		elif event.type == KEYDOWN:
			#Left and right
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
					playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > MAPWIDTH - 20:
				playerPos[0] -= 1
			#Up and Down
			if (event.key == K_UP) and playerPos[1] > MAPHEIGHT - 20:
				playerPos[1] -= 1
			if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
				playerPos[1] += 1
				
		elif (playerPos == objectPos):
			#update Score
			playerScore += 1
			score = str(playerScore)
			pygame.display.set_caption('BPy Engine 0.01: Pickin sticks! Score: ' + score)
			#update object location
			objectPos[0] = (random.randint(0,19))
			objectPos[1] = (random.randint(0,19))

	print(event.type == KEYDOWN)
	print(playerPos)

	#print(event) #Print events(debugging purposes)
	
	#Draw Map
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
		#	pygame.draw.rect(screen, colours[tilemap[row][column]], (column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))
			screen.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))
			
	#Draw the Player to the screen
	screen.blit(player,(playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))
	#draw the object
	screen.blit(object,(objectPos[0]*TILESIZE, objectPos[1]*TILESIZE))
	#finally update the display and repeat the loop
	pygame.display.update()
			
			
