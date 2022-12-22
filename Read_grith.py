

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