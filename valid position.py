def valid_position(grid, bloc, k, s):
    l = 0
    if k < 5 or s < 5:
        return False
    for i in range(k-4, k+1):
        c = 0
        for j in range(s, s+5):
            if (bloc[l][c] == '1') and (grid[i][j] != '1'):
                print(j)
                return False
            c += 1
        l += 1
    return True