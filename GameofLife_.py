import pygame
from random import randint
from itertools import permutations

#Define colors
White =  (255, 255, 255)
Green =  (120, 230, 165)
sc    =  (120, 194, 230)

class GameofLife:
    def __init__(self,rows=10,cols=10):
        self.Cols = cols
        self.Rows = rows
        self.grid = []
        for x in range(self.Rows):
            self.grid.append([])
            for y in range(self.Cols):
                self.grid[x].append(randint(0, 1))
        self.grid2 = self.grid

    def Neighbors(self,xi,yi):
        range_Neighbors = list(set(permutations([-1,-1,1,1,0],2)))

        outside = lambda x,y: not (x in range(self.Rows) and y in range(self.Cols))
        Neighbors = 0.0
        for range_x, range_y in range_Neighbors:
            if not outside(xi+range_x, yi+range_y):
                Neighbors += 1 if self.grid[xi + range_x][yi + range_y] else 0
        return Neighbors

    def Roaming(self):
        for row in range(self.Rows):
            for col in range(self.Cols):
                vec = self.Neighbors(row,col)

                if(vec < 2  or vec >3):
                    self.grid2[row][col] = 0
                elif (vec == 3):
                    self.grid2[row][col] = 1
        self.grid = self.grid2



m = GameofLife(20,20)

# cell
width  = 20
hight = 20
margin = 5

# Init  pygame
pygame.init()
DIM_windows = [ (width+margin)*m.Cols + margin , (hight+margin)*m.Rows +  margin ]
Screen = pygame.display.set_mode(DIM_windows)
Screen.fill(sc )

pygame.display.set_caption("Game of Life")
Finish = False

clock = pygame.time.Clock()

# main
while not Finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finish = True

    # Draw
    for row in range(m.Rows):
        for col in range(m.Cols):
            color = Green if(m.grid2[row][col]==1) else White

            pygame.draw.rect(Screen,
                             color,
                             [(margin+width) * col + margin,
                              (margin+hight) * row + margin,
                              width,
                              hight])

    clock.tick(5)

    pygame.display.flip()
    m.Roaming()

pygame.quit()
