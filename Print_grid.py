import math
def triangle(n) -> None:
    '''
    Fonction permettant de créer le plateau en forme de triangle
    :param n: Taille du plateau
    :return: Un fichier txt contenant le plateu de jeu vierge
    '''
    with open("triangle.txt", "w") as t:
        for i in range(math.ceil(n / 2)):
            for j in range(n):
                if j <= n / 2 + i and j >= n / 2 - i - 1:
                    t.write("1")
                else:
                    t.write("0")
            if i != math.ceil(n / 2) - 1:
                t.write("\n")


tailleT=int(input("Choisis la taille du triangle"))
#triangle(tailleT*2)
t=open("triangle.txt","r")
print(t.read())
with open("triangle.txt", "r") as f:
    for j in range(tailleT):
        L = f.readline()
        map(int, L)
        count = 0
        for i in range(len(L)):
            if L[i] == '0':
                print("  ", end ="")
            if L[i] == '1':
                print("O ", end ="")
            if (tailleT*2) - (count + 1) == 0:
                count = 0
                print()
            count = count + 1
def print_grid(grid):
    for i in range(size_board):
        for j in rn=ange(size_board):
            if grid[i][j] == '0':
                print("  ", end=" ")
            if grid[i][j] == '1':
                print(chr(141), end=" ")
            if (tailleT*2) - (count + 1) == 0:
                count = 0
                print()
            count = count + 1