import random
countBlack=0
countWhite=0

board =[
                    [[1,1,"--"],[1,2,"--"],[1,3,"--"],[1,4,"--"],[1,5,"--"],[1,6,"--"],[1,7,"--"],[1,8,"--"]],
                    [[2,1,"--"],[2,2,"--"],[2,3,"--"],[2,4,"--"],[2,5,"--"],[2,6,"--"],[2,7,"--"],[2,8,"--"]],
                    [[3,1,"--"],[3,2,"--"],[3,3,"--"],[3,4,"--"],[3,5,"--"],[3,6,"--"],[3,7,"--"],[3,8,"--"]],
                    [[4,1,"--"],[4,2,"--"],[4,3,"--"],[4,4,"--"],[4,5,"--"],[4,6,"--"],[4,7,"--"],[4,8,"--"]],
                    [[5,1,"--"],[5,2,"--"],[5,3,"--"],[5,4,"--"],[5,5,"--"],[5,6,"--"],[5,7,"--"],[5,8,"--"]],
                    [[6,1,"--"],[6,2,"--"],[6,3,"--"],[6,4,"--"],[6,5,"--"],[6,6,"--"],[6,7,"--"],[6,8,"--"]],
                    [[7,1,"--"],[7,2,"--"],[7,3,"--"],[7,4,"--"],[7,5,"--"],[7,6,"--"],[7,7,"--"],[7,8,"--"]],
                    [[8,1,"--"],[8,2,"--"],[8,3,"--"],[8,4,"--"],[8,5,"--"],[8,6,"--"],[8,7,"--"],[8,8,"--"]],
]

for k in range(100):
    wR=[0.0]
    wB=[0.0]
    bQ=[0.0]
    chessBoard = board
    if k == 1:
        for l in range(len(chessBoard)):
            print(chessBoard[l])
        print("\n")
    if k == 99:
        for l in range(len(chessBoard)):
            print(chessBoard[l])
        print("\n")
        print("\n")
        print("\n")

    wR= [random.randint(0, 7),random.randint(0, 7)]

    wB= [random.randint(0, 7),random.randint(0, 7)]
    while wR == wB:
        wB[0] = random.randint(0, 7)
        wB[1] = random.randint(0, 7)

    bQ= [random.randint(0, 7),random.randint(0, 7)]
    while bQ == wR or bQ == wB:
        bQ[0] = random.randint(0,7)
        bQ[1] = random.randint(0,7)

    if bQ == wR:
        print("TRUE")
    elif bQ==wB:
        print("TRUE")
    elif wR==bQ:
        print("TRUE")

    chessBoard[wR[0]][wR[1]][2] = "wR"
    chessBoard[wB[0]][wB[1]][2] = "wB"
    chessBoard[bQ[0]][bQ[1]][2] = "bQ"

    if bQ[0]+bQ[1] == wR[0]+wR[1]:
        countBlack += 1
    elif bQ[0]-bQ[1] == wR[0]-wR[1]:
        countBlack += 1
    elif bQ[0] == wR[0]:
        countWhite += 1
        countBlack += 1
    elif bQ[1] == wR[1]:
        countWhite += 1
        countBlack += 1
    elif bQ[0]+bQ[1] == wB[0]+wB[1]:
        countWhite += 1
        countBlack += 1
    elif bQ[0]-bQ[1] == wR[0]-wR[1]:
        countWhite += 1
        countBlack += 1


print("points for black are:",countBlack)
print("points for white are", countWhite)



if countBlack > countWhite:
    print("Black pawns win!")
elif countWhite > countBlack:
    print("Black pawns win!")
else:
    print("peace love and equality! :) ")







