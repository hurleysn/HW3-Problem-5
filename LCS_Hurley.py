def LCS(x, y):
    
    xlen = len(x)
    ylen = len(y)

    c = [[0]*(ylen) for i in range(xlen)]
    
    for i in range(xlen):
        for j in range(ylen):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1]+1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    

    return c[xlen-1][ylen-1]



print('Length of LCS is', LCS('SPRINGTIME', 'PIONEER'))
        
