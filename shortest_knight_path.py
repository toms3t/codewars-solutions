arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]


def verify_coord(coord):
    if (0 < coord[0] < 9) and (0 < coord[1] < 9):
            return True

def convert_notation(notation):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    x, y = d[notation[0]], int(notation[1])
    return x,y

def find_one_hop_squares(coord):
    one_hop_squares = []
    for num in [-2,-1,1,2]:
        if num % 2 == 1:
            coord_next = (coord[0] + num, coord[1] + 2)
            if verify_coord(coord_next):
                one_hop_squares.append(coord_next)
            coord_next = (coord[0] + num, coord[1] - 2)
            if verify_coord(coord_next):
                one_hop_squares.append(coord_next)
        else:
            coord_next = (coord[0] + num, coord[1] + 1)
            if verify_coord(coord_next):
                one_hop_squares.append(coord_next)
            coord_next = (coord[0] + num, coord[1] - 1)
            if verify_coord(coord_next):
                one_hop_squares.append(coord_next)
    return one_hop_squares
    

def knight(p1, p2):
    squares_by_hop_count_dict = {}
    hop_count = 1
    p1, p2 = convert_notation(p1), convert_notation(p2)
    next_hops = find_one_hop_squares(p2)
    squares_by_hop_count_dict[hop_count] = next_hops
    while True:
        if p1 in next_hops:
            return hop_count
        else:
            hop_count += 1
            squares_by_hop_count_dict[hop_count] = []
            for coords in next_hops:
                next_hops = find_one_hop_squares(coords)
                squares_by_hop_count_dict[hop_count].extend(next_hops)
            if p1 in squares_by_hop_count_dict[hop_count]:
                return (hop_count)
            next_hops = squares_by_hop_count_dict[hop_count]
            
