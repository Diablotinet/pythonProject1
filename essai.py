'''def read_grid(path):
    if path == 1:
        with open('cercle.txt', 'r') as f:
            for j in range(22):
                L = f.readline()
                map(int, L)
                grid = []
                count_1=0
                for i in range(22):
                    if L[i] == '0':
                        grid[j][i] = L[i]
                    if L[i] == '1':
                        grid[j][i] = L[i]
                    print(grid)
                return(grid)'''
def read_grid(path):
    grid = []
    with open(path, 'r') as f:
        for line in f:
            L = []
            for element in line:
                if element != " " and element != "\n":
                    L.append(int(element))
            grid.append(L)
    print(len(grid))
    return grid




'''for lin in f
for element'''

