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
triangle(tailleT*2)
t=open("triangle.txt","r")
print(t.read())

triangle_grid = []
triangle_grid_temp=[]
with open("triangle.txt", "r") as f:
    for j in range(tailleT):
        L = f.readline()
        map(int,L)
        triangle_grid = []
        for i in range(len(L)):
            if L[i]== '0':
                type(L)
                x=chr(95)
                triangle_grid.append(x)
            if L[i]=='1':
                p=chr(79)
                triangle_grid.append(p)
        print(triangle_grid)
triangle_grid = []
triangle_grid_temp=[]

with open("triangle.txt", "r") as f:
    with open("path.txt", "w") as t:
        for j in range(tailleT):
            L = f.readline()
            map(int,L)
            triangle_grid = []
            for i in range(len(L)):
                if L[i]== '0':
                    type(L)
                    x=chr(173)
                    t.write(x)
                if L[i]=='1':
                    p=chr(79)
                    t.write(p)
            print (t)







