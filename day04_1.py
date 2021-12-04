testdata = {
    "draws": [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1], 
    "boards":   [
                    [22,13,17,11,0,8,2,23,4,24,21,9,14,16,7,6,10,3,18,5,1,12,20,15,19],
                    [3,15,0,2,22,9,18,13,17,5,19,8,7,25,23,20,11,10,24,4,14,21,16,12,6],
                    [14,21,17,24,4,10,16,15,9,19,18,8,23,26,20,22,11,13,6,5,2,0,12,3,7],
                ]
            }

### bingoparser
file = 'input/day04_1.txt'
with open(file, 'r') as reader:
    try:
        raw = reader.readlines()

        draws = [str(raw[0])]
        draws = draws[0].strip().split(',')
        draws = [int(x) for x in draws]

        boards = raw[2:]
        boards = [x.strip().replace('  ', ' ').split(' ') for x in boards if len(x) >= 5]
        boards_flat = []
        for i in range(0,len(boards),5):
            boards_flat.append([val for sublist in boards[i:i+5] for val in sublist])
        
        boards = []
        for board in boards_flat:
            board = [int(item) for item in board]
            boards.append(board)

        data = dict()
        data["draws"] = draws
        data["boards"] = boards
        realdata = data
        
    finally:
        reader.close()

bingo = realdata


def makeBoardRows(flat, size): 
    multiarray = [flat[i:i+size] for i in range(0,len(flat), size)]
    return multiarray

def makeBoardCols(flat, size): 
    rows = makeBoardRows(flat, size)
    multiarray = list(map(list, zip(*rows)))
    return multiarray

def checkftw(board):
    # reshape to multidimensional array
    boardrows = makeBoardRows(board, 5)
    boardcols = makeBoardCols(board, 5)

    line = 1
    for row in boardrows:
        if all(isinstance(x, str) for x in row):
            print(board)
            print(f'board wins on line #{line}')
            return True
        else:
            #print(f'board has not won on line#{line}')
            pass
        line += 1
    # print(f'board has not won on line')
    column = 1
    for col in boardcols:
        if all(isinstance(x, str) for x in col):
            print(board)
            print(f'board wins on column #{column}')
            return True
        else:
            #print(f'board has not won on column#{column}')
            pass
        column += 1
    # print(f'board has not won on columns')

def countPoints(board):
    result = [0 if x == 'x' else x for x in board]
    return sum(result)

### bingo player
# go through draws
draw = 0
winning = False
for number in bingo["draws"]:
    # print(f'draw #{str(draw+1).zfill(3)}:{number}')
    # check off drawn numbers
    boardnum = 0
    for board in bingo["boards"]:
        board = ["x" if item == number else item for item in board]
        bingo["boards"][boardnum] = board
        # print(f'checking board #{str(boardnum+1).zfill(2)}')
        # check for winning ticket if draw >= 5
        if draw >=5:
            winning = checkftw(board)
            points = number * countPoints(board)
        # output winning
        if winning == True:
            print("BINGO!!!")
            print("winning board:")
            print(f'board #{str(boardnum+1).zfill(2)} on draw #{str(draw+1).zfill(3)} ({number})')
            print(f'board #{str(boardnum+1).zfill(2)}:{board}')
            print(f'there are {countPoints(board)} Points left on the board, last drawn number is {number}')
            print(f'resulting points are {points}')
            break
        boardnum += 1
    if winning == True:
        break
    draw +=1

print(f'Thank you for playing')