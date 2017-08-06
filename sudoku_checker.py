
# Checks:
# 1. Sum of each column/row is 45
# 2. All integers in the column/row is unique
# 3. #1 and #2 for regions as well

# board = [
#     [1, 3, 2, 5, 7, 9, 4, 6, 8],
#     [4, 9, 8, 2, 6, 1, 3, 7, 5],
#     [7, 5, 6, 3, 8, 4, 2, 1, 9],
#     [6, 4, 3, 1, 5, 8, 7, 9, 2],
#     [5, 2, 1, 7, 9, 3, 8, 4, 6],
#     [9, 8, 7, 4, 2, 6, 5, 3, 1],
#     [2, 1, 4, 9, 3, 5, 6, 8, 7],
#     [3, 6, 5, 8, 1, 7, 9, 2, 4],
#     [8, 7, 9, 6, 4, 2, 1, 5, 3]
# ]

board = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

def finished_or_not(board):
    i = 0
    x = 0
    y = 0
    region = []
    for array in board:
        if sum(array) != 45:
            return 'Try again!'
    for i in range(9):
        colsum = sum([x[i] for x in board])
        if colsum != 45:
            return 'Try again!'
        i += 1
    for i in range(3):
        for i in range(3):
            region = []
            for line in board[y:y+3]:
                region.append(line[x:x+3])
            flat_region = [x for row in region for x in row]
            x += 3
            if sum(flat_region) != 45:
                return 'Try again!'
        y += 3
        x = 0
    return 'Finished!'

print (finished_or_not(board))
