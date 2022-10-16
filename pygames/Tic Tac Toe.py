import  pygame, sys, time

pygame.init()
clock = pygame.time.Clock()

height = 300
width = 300

Board = [[-1 , -1, -1],[-1, -1, -1],[-1, -1, -1]]

background_color = (0, 0, 0)
black_color = (0, 0, 0)
white_color = (255, 255, 255)
blue_color = (16, 20, 255)
red_color = (255, 20, 16)
grey_color = (20, 20, 20)


font1 = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 18)
text1 = font1.render('Tic Tac Toe', True, white_color)
textRect1 = text1.get_rect()
text2 = font2.render('Press Enter to start', True, white_color)
textRect2 = text2.get_rect()

font3 = pygame.font.Font('freesansbold.ttf', 32)
font4 = pygame.font.Font('freesansbold.ttf', 18)

text3 = font3.render('Game Over', True, white_color)



textRect3 = text3.get_rect()

text4 = font4.render('', True, white_color)
textRect4 = text4.get_rect()

textRect1.center = (width//2 , height//2)
textRect2.center = (width//2 , height//2 + 30)

textRect3.center = (width//2 , height//2)
textRect4.center = (width//2 , height//2 + 30)


def drawIntroText():
  # font = pygame.font.Font('freesansbold.ttf', 32)
  pass
  return 


def drawGameOverText():
  pass
  return




def drawBoard(screen, color, screen_width, screen_height, boarder_thickness = 2):
  width =  screen_width/3
  height = screen_height/3
  for row in range(3):
    for column in range(3): 
        pygame.draw.rect(screen, white_color, pygame.Rect(row*width, column*100, width, height), boarder_thickness)  
  return

def placePiece(screen, x, y, color):
  pygame.draw.rect(screen, color, pygame.Rect(x*100, y*100, 100, 100))
  return

def translateToBoardCordinate(actual_x_pos, actual_y_pos, block_width, block_height):
  x = int(actual_x_pos/block_width)
  y = int(actual_y_pos/block_height)
  return (x, y)

def checkWin(Board, piece):
  
  # Diagonals
  if ((Board[0][0] == piece) and (Board[1][1] == piece) and (Board[2][2] == piece)):
    return True
  elif ((Board[2][0] == piece) and (Board[1][1] == piece) and (Board[0][2] == piece)):
    return True

  # Rows
  elif ((Board[0][0] == piece) and (Board[0][1] == piece) and (Board[0][2] == piece)):
    return True
  elif ((Board[1][0] == piece) and (Board[1][1] == piece) and (Board[1][2] == piece)):
    return True
  elif ((Board[2][0] == piece) and (Board[2][1] == piece) and (Board[2][2] == piece)):
    return True

  # Columns    
  elif ((Board[0][0] == piece) and (Board[1][0] == piece) and (Board[2][0] == piece)):
    return True
  elif ((Board[0][1] == piece) and (Board[1][1] == piece) and (Board[2][1] == piece)):
    return True  
  elif ((Board[0][2] == piece) and (Board[1][2] == piece) and (Board[2][2] == piece)):
    return True    

  #return
  else:
    return False






def winTiles(Board, piece):
  
  # Diagonals
  if ((Board[0][0] == piece) and (Board[1][1] == piece) and (Board[2][2] == piece)):
    return ((0,0),(1,1),(2,2))
  elif ((Board[2][0] == piece) and (Board[1][1] == piece) and (Board[0][2] == piece)):
    return ((2,0),(1,1),(0,2))

  # Rows
  elif ((Board[0][0] == piece) and (Board[0][1] == piece) and (Board[0][2] == piece)):
    return ((0,0),(0,1),(0,2))
  elif ((Board[1][0] == piece) and (Board[1][1] == piece) and (Board[1][2] == piece)):
    return ((1,0),(1,1),(1,2))
  elif ((Board[2][0] == piece) and (Board[2][1] == piece) and (Board[2][2] == piece)):
    return ((2,0),(2,1),(2,2))

  # Columns    
  elif ((Board[0][0] == piece) and (Board[1][0] == piece) and (Board[2][0] == piece)):
    return ((0,0),(1,0),(2,0))
  elif ((Board[0][1] == piece) and (Board[1][1] == piece) and (Board[2][1] == piece)):
    return ((0,1),(1,1),(2,1))  
  elif ((Board[0][2] == piece) and (Board[1][2] == piece) and (Board[2][2] == piece)):
    return ((0,2),(1,2),(2,2))    
  else:
    return ((-1,-1),(-1,-1),(-1,-1))

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(background_color)

def restart(screen, color, screen_width, screen_height):
  screen.fill(background_color)
#  drawBoard(screen, color, screen_width, screen_height)
  return 

running = True
player_color = blue_color
started = False
endgame =  False
while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            started = True
            endgame = False
            restart(screen, white_color, width, height)
        elif (event.type == pygame.MOUSEBUTTONDOWN)   and (started == True):
          mouse_position = pygame.mouse.get_pos()
          translateToBoardCordinate(mouse_position[0], mouse_position[1], 100, 100)
          cordinates = translateToBoardCordinate(mouse_position[0], mouse_position[1], 100, 100)

          if player_color == blue_color:

            if (Board[cordinates[1]][cordinates[0]] == -1):
              placePiece(screen, cordinates[0], cordinates[1], blue_color)
              player_color = red_color
              Board[cordinates[1]][cordinates[0]] = 1
            if checkWin(Board, 1) == True:
              text4 = font4.render('Player 1 wins', True, white_color)
              endgame = True

          else:
            if (Board[cordinates[1]][cordinates[0]] == -1):
              placePiece(screen, cordinates[0], cordinates[1], red_color)
              player_color = blue_color
              Board[cordinates[1]][cordinates[0]] = 0
            if checkWin(Board, 0) == True:
              text4 = font4.render('Player 2 wins', True, white_color)
              endgame = True

    if (started == True) and (endgame == False):
      drawBoard(screen, white_color, width, height)
    elif (started == False) and (endgame == False):
      screen.blit(text1, textRect1)
      screen.blit(text2, textRect2)
    elif (started == True) and (endgame == True):
      drawBoard(screen, white_color, width, height)
      pygame.display.flip()
      time.sleep(0.75)
      restart(screen, white_color, width, height)
      Board = [[-1 , -1, -1],[-1, -1, -1],[-1, -1, -1]]
      pygame.display.flip()
      screen.blit(text3, textRect3)
      screen.blit(text4, textRect4)  
      started = False

    else:
      pass
    
    pygame.display.flip()
    clock.tick(10)