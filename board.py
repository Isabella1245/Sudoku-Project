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

    #To be added; a=0 are placeholders
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
    screen.fill((54, 100, 117)) #screen color

    #start screen text
    start_font1 = pygame.font.Font(None, 90)
    start_surf1 = start_font1.render("Welcome to Sudoku", 0, (0, 0, 0))
    start_rect1 = start_surf1.get_rect(center=(300,170))

    start_font=pygame.font.Font(None,40)
    start_surf=start_font.render("Select Game Mode:",0,(0,0,0))
    start_rect=start_surf.get_rect(center=(600//2,600//2-50))

    #loads image
    b1=pygame.image.load("button1.png")
    b2=pygame.image.load("button2.png")
    b3=pygame.image.load("button3.png")

    #postions/draws image/text
    screen.blit(b1,(-200,100))
    screen.blit(b2,(0,100))
    screen.blit(b3,(200,100))
    screen.blit(start_surf1, start_rect1)
    screen.blit(start_surf,start_rect)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if b3.collidepoint((x,y)):
                d=50


    #
    # if a==1:
    #     difficulty=30
    # elif a==1:
    #     difficulty = 40
    # elif a==50:
    #     difficulty = 50
    # return difficulty



while True:
    d=start_screen()
    if d!=0:
        break
c=Board(9*600,9*600,d)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    c.draw()
    pygame.display.update()