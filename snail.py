array = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]
         ]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]


def snail(arr):
    newarr = []
    rside = []
    lside = []
    newarr.append(arr[0])
    for l in arr[1:]:
        rside.append(l[-1])
    newarr.append(rside)
    bottom = arr[-1][::-1][1:]
    newarr.append(bottom)
    for x in array[1:-1]:
        for y in x[:-1]:
            lside.append(y)
    newarr.append(lside)
    finalarr = [x for row in newarr for x in row]
    print('array given', array)
    print('my answer', finalarr)
    return finalarr

print(snail(array))