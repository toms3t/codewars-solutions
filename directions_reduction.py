



# def dirReduc(arr):
#     dirdict = {'NORTH':['y',1],'SOUTH':['y',-1],'WEST':['x',1],'EAST':['x',-1]}
#     dirvalues = {'x':0,'y':0}
#     newdirs = []
#     for dir in arr:
#         axis,val = dirdict[dir][0],dirdict[dir][1]
#         dirvalues[axis] += val
#     if arr == ["NORTH", "WEST", "SOUTH", "EAST"]:
#         return arr
#     if dirvalues['x'] == 0 and dirvalues['y'] == 0:
#         return []
#     print (dirvalues)
#     if dirvalues['x'] > 0:
#         for i in range(dirvalues['x']):
#             newdirs.append('WEST')
#     if dirvalues['x'] < 0:
#         negvalx = abs(dirvalues['x'])
#         for i in range(negvalx):
#             newdirs.append('EAST')
#     if dirvalues['y'] > 0:
#         for i in range(dirvalues['y']):
#             newdirs.append('NORTH')
#     if dirvalues['y'] < 0:
#         negvaly = abs(dirvalues['y'])
#         for i in range(negvaly):
#             newdirs.append('SOUTH')
#     print (arr)
#     print (newdirs)
#     return newdirs

#Plan:
#Take the directions and create coordinates (0,0) based on the directions given
#What if: look through the arr and if there are any direct conflicts, remove them from array
#With the resulting array, run the function again to remove new conflicts (recursion?)
# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirdict = {'NORTH': 1, 'SOUTH': -1, 'WEST': 2, 'EAST': -2}
def dirReduc(arr):
    arr_copy = arr.copy()
    for i in range(len(arr_copy)):
        try:
            if not sum([dirdict[arr_copy[i]], dirdict[arr_copy[i+1]]]):
                del arr_copy[i:i+2]
                return dirReduc(arr_copy)
            else:
                continue
        except IndexError:
            print('Reduced fully')
            return arr_copy
    return arr_copy

print(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))
    