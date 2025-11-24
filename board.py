import pygame,sys
pygame.init()

class Board:
    screen = pygame.display.set_mode((600, 600))
    #initalize width/height/screen/difficulty
    def __init__(self,width,height,difficulty):
        self.width=width
        self.height=height
        self.difficulty=difficulty #easy=30; medium=40;hard=50

    #draws the grid & cells: 2x2 bold lines; 3x3 each square
    #in total: 9x9 grid
    def draw(self):
        #fills screen color
        self.screen.fill((255, 255, 255))
        #draw - line
        for i in range(4):
            pygame.draw.line(Board.screen, (0, 0, 0), (0, i * 200), (self.height, i * 200), 15)
            #draw smaller lines
        for l in range(10):
            pygame.draw.line(Board.screen, (0, 0, 0), (0, l * 200//3), (self.width, l * 200//3), 2)

        # draw | lines
        for j in range(4):
            pygame.draw.line(Board.screen, (0, 0, 0), (j * 200, 0), (j * 200, self.width), 15)
            #draw smaller lines
        for k in range(10):
            pygame.draw.line(Board.screen, (0, 0, 0), (k * 200//3, 0), (k * 200//3, self.height), 2)

class Cell:
    screen = pygame.display.set_mode((600, 600))
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen

    #To be added
    def set_cell_value(self,value):
        a=0
        #setter for this cell's value
    def set_sketched_value(self,value):
        a=0
        #sett for this cell's skecthed value
    def draw(self):
        a=0
        #draws the cell with value; if no value -> no value should be showen


# I will create pngs of the buttons
# that when the player clicks on, it will set the diffculty/gamemode
#-------------------------------------------------------------------
#Starting Menu UI - returns diffculuty:
def start_screen():
    difficulty=0
    screen = pygame.display.set_mode((600, 600))
    screen.fill((255, 255, 255))

    #loads image
    b1=pygame.image.load("button1.png")
    b2=pygame.image.load("button2.png")
    b3=pygame.image.load("button3.png")
    screen.blit(b1,(-200,100))
    screen.blit(b2,(0,100))
    screen.blit(b3,(200,100))

    # for event in pygame.event.get():
    #     if event.type==pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()
    #     elif event.type==pygame.MOUSEBUTTONDOWN:

    #
    # if a==1:
    #     difficulty=30
    # elif a==1:
    #     difficulty = 40
    # elif a==50:
    #     difficulty = 50
    # return difficulty


c=Board(9*600,9*600,3)
while True:
    d=start_screen()
    if d!=0:
        break
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()