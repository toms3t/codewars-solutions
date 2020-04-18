from numpy import subtract


def knight(p1, p2):
    """
    Finds the shortest path (in # of hops) a knight can take between 2 squares 
    on a chessboard
    """

    def verify_coord(coord):
        """
        Verify the coordinates fall within the range of the chessboard
        """
        if (0 < coord[0] < 9) and (0 < coord[1] < 9):
            return True

    def convert_notation(notation):
        """
        Convert chess notation to coordinate notation
        """
        d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        return d[notation[0]], int(notation[1])

    def find_one_hop_squares(coord):
        """
        Finds all possible 1 hop squares for the knight
        given a specific starting coordinate
        """
        one_hop_squares = []
        movements = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ]
        for movement in movements:
            next_hop = tuple(subtract(coord, movement))
            if verify_coord(next_hop):
                one_hop_squares.append(next_hop)
        return one_hop_squares

    squares_by_hop_count_dict = {}
    hop_count = 1
    p1, p2 = convert_notation(p1), convert_notation(p2)
    next_hops = find_one_hop_squares(p1)
    squares_by_hop_count_dict[hop_count] = next_hops
    if p2 in next_hops:
        return hop_count
    else:
        while True:
            hop_count += 1
            squares_by_hop_count_dict[hop_count] = []
            for coords in next_hops:
                next_hops = find_one_hop_squares(coords)
                squares_by_hop_count_dict[hop_count].extend(next_hops)
            if p2 in squares_by_hop_count_dict[hop_count]:
                return hop_count
            next_hops = squares_by_hop_count_dict[hop_count]

