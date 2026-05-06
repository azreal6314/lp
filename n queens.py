def solveNqueens(n):
    cols=set()
    upperdiagonal=set()
    lowerdiagonal=set()

    board=[['.']*n for _ in range(n)]
    result=[]

    def backtrack(row):
        if row == n :
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row-col) in lowerdiagonal or (row+col) in  upperdiagonal :
                continue

            cols.add(col)
            upperdiagonal.add(row+col)
            lowerdiagonal.add(row-col)

            board[row][col]='Q'

            backtrack(row+1)

            cols.remove(col)
            upperdiagonal.remove(row+col)
            lowerdiagonal.remove(row-col)

            board[row][col]='.'

    backtrack(0)
    return result


result=solveNqueens(4)
k=1
for i in result:
    print("solution:",k)
    k+=1
    for j in i:
        print(j,end=' ')
        print()
    print()