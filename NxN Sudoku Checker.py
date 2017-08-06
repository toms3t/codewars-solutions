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
    line_sum = 0
    region = []
    line_length = len(board[0])
    print(line_length)
    for i in range(1, line_length + 1):
        line_sum += i
    print(line_sum)
    print(line_sum)
    for array in board:
        if sum(array) != line_sum:
            return 'Try again!'
    for i in range(line_length):
        colsum = sum([x[i] for x in board])
        if colsum != line_sum:
            return 'Try again!'
        i += 1
    for i in range(3):
        for i in range(3):
            region = []
            for line in board[y:y + 3]:
                region.append(line[x:x + 3])
            flat_region = [x for row in region for x in row]
            x += 3
            if sum(flat_region) != line_sum:
                return 'Try again!'
        y += 3
        x = 0
    return 'Finished!'


print(finished_or_not(board))
