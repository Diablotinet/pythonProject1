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



