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
        Board.screen.fill((255, 255, 255))
        #draw - line
        for i in range(4):
            pygame.draw.line(Board.screen, (0, 0, 0), (0, i * 175), (self.height, i * 175), 15)
            #draw smaller lines
        for l in range(10):
            pygame.draw.line(Board.screen, (0, 0, 0), (0, l * 175//3), (self.width, l * 175//3), 2)

        # draw | lines
        for j in range(4):
            pygame.draw.line(Board.screen, (0, 0, 0), (j * 175, 0), (j * 175, self.width), 15)
            #draw smaller lines
        for k in range(10):
            pygame.draw.line(Board.screen, (0, 0, 0), (k * 175//3, 0), (k * 175//3, self.height), 2)
        #for cover up
        Board.screen.fill((0,0,0),(0,520,self.width,self.height))
        Board.screen.fill((0, 0, 0), (520, 0, self.width, self.height))

        #reset/restart/exit buttons
        exit = pygame.image.load("exit.png")
        exit_rect = exit.get_rect(center=(560, 150))
        Board.screen.blit(exit, exit_rect)

        rs = pygame.image.load("restart.png")
        rs_rect = rs.get_rect(center=(560, 300))
        Board.screen.blit(rs, rs_rect)

        r = pygame.image.load("reset.png")
        r_rect = r.get_rect(center=(560, 450))
        Board.screen.blit(r, r_rect)


    # def select(self,row,col):
    #     #marks current cell
    # def click(self,x,y):
    #     #return x,y, else returns None
    # def clear(self):
    #     #removed input from the user
    # def sketch(self,value):
    #     #sets skecth value
    # def place_number(self,value):
    #     #sets seketch vale to user entered function
    # def reset_to_original(self):
    #     # resets all cells
    # def is_full(self):
    #     #bla
    # def find_empty(self):
    #     #s
    # def check_board(self):
    #     #aa

class Cell:
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
def start_screen(screen):
    difficulty=0
    screen.fill((54, 100, 117)) #screen color

    #start screen text
    start_font1 = pygame.font.Font(None, 90)
    start_surf1 = start_font1.render("Welcome to Sudoku", 0, (0, 0, 0))
    start_rect1 = start_surf1.get_rect(center=(300,170))

    start_font=pygame.font.Font(None,40)
    start_surf=start_font.render("Select Game Mode:",0,(0,0,0))
    start_rect=start_surf.get_rect(center=(300,250))

    #loads image
    b1=pygame.image.load("button1.png")
    b1_rect=b1.get_rect(center=(100,350))
    b2=pygame.image.load("button2.png")
    b2_rect=b2.get_rect(center=(300,350))
    b3=pygame.image.load("button3.png")
    b3_rect=b3.get_rect(center=(500,350))

    #postions/draws image/text
    screen.blit(b1,b1_rect)
    screen.blit(b2,b2_rect)
    screen.blit(b3,b3_rect)

    screen.blit(start_surf1, start_rect1)
    screen.blit(start_surf,start_rect)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                #to make it easier to understand
                x=x//10
                y=y//100
                #the x and y values are the max & min of each button area
                if 3<=x<=17 and 3<=y<=4: #b1
                    return 30
                elif 23<=x<=37 and 3<=y<=4: #b2
                    return 40
                elif 43<=x<=57 and 3<=y<=4: #b3
                    return 50

start=True
d=0
#board.screen will be the main screen updated
c=Board(9*600,9*600,d)
while start:
    d=start_screen(Board.screen)
    print(d)
    if d!=0:
        start=False
        c.difficulty = d
        c.draw()
        break
while start==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                x = x // 10
                y = y // 100
                print(x,y)
                if 53<=x<=58 and y==1: #exit button is pressed
                    pygame.quit()
                    sys.exit()
                elif 53<=x<=58 and 2<=y<=3: #restart
                    d=0
                    c = Board(9 * 600, 9 * 600, d)
                    while True:
                        d = start_screen(Board.screen)
                        if d != 0:
                            c.difficulty = d
                            c.draw()
                            break
                # elif 53 <= x <= 58 and y==4: #reset
                #     #reset/clear all user inputted values
                #elif input values
        #3rd event is the movement system


    # a version of c.draw with numbers needed so values gets updated/displayed
    pygame.display.update()