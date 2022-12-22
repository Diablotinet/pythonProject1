import math


def board() -> int:
    '''
    Function that allow you to choose the size of your board
    :return: Give back a file that contain the board and its size
    '''
    size_board = 0
    while size_board < 21:
        size_board = int(input("Choose the size of your board for this game(It has to be superior or equal to 21):  "))

    select = 0
    while select < 1 or select > 3:
        select = int(input("Choose the shape of your board : \n1-Cercle\n2-Losange\n3-Triangle\n"))

    if select == 1:
        cercle(size_board)
        return ("cercle.txt")
    if select == 2:
        losange(size_board)
        return ("losange.txt")
    if select== 3:
        triangle(size_board)
        return ("triangle.txt")
    return size_board


def cercle(t) -> None:
    '''
    Fonction permettant de créer le plateau en forme de cercle
    :param t: Taille du plateau
    :return: Un fichier txt contenant le plateu de jeu vierge
    '''
    with open("cercle.txt", "w") as f:
        for i in range(t):
            for j in range(t):
                if math.sqrt((i + 0.5 - t / 2) ** 2 + (j + 0.5 - t / 2) ** 2) <= math.ceil(t / 2):
                    f.write("1")
                else:
                    f.write("0")
            if i != t - 1:
                f.write("\n")
        return("cercle.txt")

def losange(t) -> None:
    '''
    Fonction permettant de créer le plateau en forme de losange
    :param t: Taille du plateau
    :return: Un fichier txt contenant le plateu de jeu vierge
    '''
    with open("losange.txt", "w") as f:
        for i in range(t):
            if i <= t // 2:
                for j in range(t):
                    if j <= t / 2 + i and j >= t / 2 - i - 1:
                        f.write("1")
                    else:
                        f.write("0")
            else:
                for j in range(t):
                    if j <= t / 2 + t - i - 1 and j >= t / 2 - t + i:
                        f.write("1")
                    else:
                        f.write("0")
            if i != t - 1:
                f.write("\n")


def triangle(t) -> None:
    '''
    Fonction permettant de créer le plateau en forme de triangle
    :param t: Taille du plateau
    :return: Un fichier txt contenant le plateu de jeu vierge
    '''
    with open("triangle.txt", "w") as f:
        for i in range(t):
            for j in range(t):
                if j <= t / 2 + i and j >= t / 2 - i - 1:
                    f.write("1")
                else:
                    f.write("0")
            if i != math.ceil(t / 2) - 1:
                f.write("\n")




def print_grid(grid):
    print("    ", "="* 3* len(grid))
    for i in range(len(grid)):
        print()
        if i == 0:
            print("   ", end = "   ")
            for m in range(len(grid)):
                print(chr(65 + m), end="  ")
            print()
        if i >= 10 :
            print(i , "", "!", end=" ")
        else:
            print(i, " ", "!", end=" ")
        for j in range(len(grid)):
            if grid[i][j] == 0 :
                print(" ", end="  ")
            if grid[i][j] == 1 :
                    print(chr(141), end="  ")
        print("!", end=" ")
    print()
    print()
    print("    ", "="* 3* len(grid))
def read_grid(path):
    grid = []
    with open(path, 'r') as f:
        for line in f:
            L = []
            for element in line:
                if element != " " and element != "\n":
                    L.append(int(element))
            grid.append(L)
    return grid

def save_grid(path,grid):
    with open (path,"w") as f:
            for i in range(len(grid[i])):
                for j in range (len(grid[j])):
                    append.f(grid[i][j])

def col_state(grid, j):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[j][i] == 1 :
                return False
    return True


def col_clear(grid, j):
    if col_state():
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[j][i] == 2:
                    grid[i][j] = 1


def row_state(grid, i):
    for j in range(size_board):
        if grid[i][j]==0:
            return False
    return True

def row_clear(grid, m):
    temp_var=[]
    if row_state(grid,m):
        for i in range(size_board):
                for j in range(size_board):
                    if i<=m :
                        if grid[i+1][j]!=0 and grid[i][j]!=0:
                            temp_var[j]=grid[i+1][j]
                            grid[i][j]= temp_var[j]
                    if i==0 and grid[i][j]==2:
                        grid[i][j]=0
