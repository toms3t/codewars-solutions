from numpy import subtract
import time


def attack(start, dest, obstacles):
    """
    Finds the shortest path (in # of hops) a knight can take between 2 squares 
    on a chessboard
    """
    if start == dest:
        return 0
    def verify_coord(coord):
        """
        Verify the coordinates fall within the range of the chessboard
        """
        if (-1 < coord[0]) and (-1 < coord[1]):
            return True

    def find_one_hop_squares(coord, obstacles):
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
            if verify_coord(next_hop) and next_hop not in obstacles:
                one_hop_squares.append(next_hop)
            else:
                continue
        return one_hop_squares

    squares_by_hop_count_dict = {}
    hop_count = 1
    next_hops = find_one_hop_squares(start, obstacles)
    squares_by_hop_count_dict[hop_count] = next_hops
    if dest in next_hops:
        return hop_count
    else:
        while True:
            hop_count += 1
            if hop_count == 9:
                return "None/nil"
            squares_by_hop_count_dict[hop_count] = []
            for coords in next_hops:
                next_hops = find_one_hop_squares(coords, obstacles)
                squares_by_hop_count_dict[hop_count].extend(next_hops)
            if dest in squares_by_hop_count_dict[hop_count]:
                return hop_count
            next_hops = squares_by_hop_count_dict[hop_count]

tic = time.perf_counter()
print(attack((0,0), (7,7), ((5,5),(5,6),(5,7),(5,8),(6,5),(8,6),(6,9),(9,6),(8,5),(7,9),(4,6),(9,8))))
print(attack((7,1), (3,3), ((5,1),(5,2),(5,0),(4,2),(4,4),(7,5))))
print(attack((7,1), (5,2), ()), 1)
print(attack((7,1), (3,3), ()), 2)
print(attack((7,6), (0,5), ()), 4)
print(attack((7,6), (2,1), ()), 4)
print(attack((7,6), (7,6), ()), 0)
print(attack((7,6), (7,7), ()), 3)
print(attack((7,7), (1,0), ()), 5)
print(attack((7,1), (3,3), ((5,1),(5,2),(5,0),(4,2),(4,4),(7,5))), 4)
print(attack((6,7), (7,7), ((5,5),(5,6),(5,7),(8,6),(6,9),(9,6),(7,9),(4,6))), 5)
print(attack((7,1), (3,3), ((5,2),)), 4)
print(attack((7,1), (3,3), ((5,1),(5,2),(5,0),(4,2),(4,4),(7,5),(4,3),(7,4),(3,4),(3,6),(4,7),(6,7),(6,4),(3,6),(4,5))), 4)
print(attack((7,6), (7,7), ((5,5),(5,6),(5,7))), 3)
print(attack((7,1), (3,3), ((5,1),(5,2),(5,0),(4,2),(4,4),(7,5),(4,3),(7,4),(3,4),(3,6),(4,7),(6,7),(6,4),(3,6),(4,5),(4,6),(5,3),(7,3))), 4)
print(attack((7,1), (3,3), ((5,0),(6,3),(5,2),(4,2),(4,4),(7,5),(4,3),(1,3),(3,4),(0,3),(4,7),(0,5),(6,4),(1,7),(4,5),(4,6),(5,3),(7,3))), 4)
print(attack((0,0), (7,7), ((5,5),(5,6),(5,7),(5,8),(6,5),(8,6),(6,9),(9,6),(8,5),(7,9),(4,6),(9,8))), 8)
#answer should be 4, my program is showing 6
# toc = time.perf_counter()
# print(f"Ran in {toc - tic:0.4f} seconds")
#last .1156 seconds
#last .0778

# (2,3),(4,2),(3,4),(5,5),(4,7),(6,8),(7,6),(8,8)
# (3,2), (5,1), (7,2), (5,3), (7,4), (8,6), (6,7)