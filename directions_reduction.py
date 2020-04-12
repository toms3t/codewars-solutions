dirdict = {'NORTH': 1, 'SOUTH': -1, 'WEST': 2, 'EAST': -2}
def dirReduc(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        try:
            if not sum([dirdict[arr[i]], dirdict[arr[i+1]]]):
                del arr[i:i+2]
                return dirReduc(arr)
            else:
                continue
        except IndexError:
            return arr
    return arr

print(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))
    