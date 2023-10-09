# PyGame Tilemap Grid Maker
# System By: Trentyne Morgan

# Import Libraries
import pygame
import sys
from pygame.locals import *

# Initialize PyGame
pygame.init()

# RGB Color Values
Black  = (0, 0, 0)
Blue   = (32, 0, 240)
Green  = (2, 217, 6)
Red    = (217, 2, 2)
Yellow = (240, 236, 2)
Orange = (240, 117, 2)
Pink   = (240, 2, 204)
Purple = (169, 0, 240)
Teal   = (2, 240, 204)
Grey   = (179, 179, 179)
Brown  = (59, 53, 26)

# RGB Color Table (Array)
Color_Table = [(Black), (Blue), (Green), (Red), (Yellow), (Orange), (Pink), (Purple), (Teal), (Grey), (Brown)]

# Color Index
Color_Table_Index = 0

# Main Window Attributes
Window_Width = 480
Window_Height = 480
Window_Caption = "Tilemap Example"

# Main Window Creation
MainGameWindow = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption(Window_Caption)

# Tile Draw System Values
Tile_Draw_Position_X = 0
Tile_Draw_Position_Y = 0
Tile_Counter = 0

# Tile Monitoring
tileCurrentPosition = (Tile_Draw_Position_X, Tile_Draw_Position_Y)
tileStartPositions = []
tileIndex = 0


# Tile Drawing
def Tile_Draw():

	# Reference Global Variables
  global Tile_Draw_Position_X
  global Tile_Draw_Position_Y
  global Tile_Counter
  global Color_Table_Index
  global Color_Table

  # Draw the Tile
  pygame.draw.rect(MainGameWindow, (Color_Table[Color_Table_Index]), (Tile_Draw_Position_X, Tile_Draw_Position_Y, 32, 32))

  # Increase the Tile X Position
  Tile_Draw_Position_X += 32

  # Increase the Tile Counter
  Tile_Counter += 1

  # Change Tile Color
  Color_Table_Index += 1

  # If the Color_Table_Index Value reaches 11, reset the index value to 0
  if Color_Table_Index == 11:
  	Color_Table_Index = 0

	# Store the current tile position
	try:
		tileStartPositions[tilePosIndex] = tileCurrentPosition
		tilePosIndex += 1
	except TabError:
		tileStartPositions[tilePosIndex] = tileCurrentPosition
		tilePosIndex += 1
				
  # If the Tile Counter equals 15, Move the Y Position down and, reset the X position, and set the tile counter back to 0
  if Tile_Counter == 15:
  	Tile_Draw_Position_Y += 32
    Tile_Draw_Position_X = 0
    Tile_Counter = 0

# Tile Drawing (Since 225 tiles can fit in a 480x480 window, we call this function 225 times. then quit.)
for x in range(0,225):
    Tile_Draw()

# List all tile positions
for i in tileStartPos:
		print(i, "\n")

# Mouse Monitor System
def mouseplacement():
       cursorpos = pygame.mouse.get_pos()
       print('Current Mouse Position:', cursorpos)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mouseplacement()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()