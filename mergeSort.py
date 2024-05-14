import time

def merge_sort(data, drawData_merge, timeTick):
    merge_sort_algorithm(data, 0, len(data)-1, drawData_merge, timeTick)

def merge_sort_algorithm(data, left, right, drawData_merge, timeTick):
    if left < right:
        middle = (left + right) // 2

        merge_sort_algorithm(data, left, middle, drawData_merge, timeTick)
        merge_sort_algorithm(data, middle+1, right, drawData_merge, timeTick)
        merge(data, left, middle, right, drawData_merge, timeTick)

def merge(data, left, middle, right, drawData_merge, timeTick):
    drawData_merge(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    L = data[left:middle+1]
    R = data[middle+1: right+1]

    i = j = 0

    for k in range(left, right+1):
        if i < len(L) and j < len(R):
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
        elif i < len(L):
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
    
    drawData_merge(data, ['green' if x >= left and x <= right else 'white' for x in range(len(data))])
    time.sleep(timeTick)

# Test:
# data = [20,15,11,10,9,8,7,6,5,4,3,2,1]
# merge_sort(data, 0, 0)
# print(data)

def getColorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append('yellow')
            else:
                colorArray.append('pink')
        else:
            colorArray.append('white')

    return colorArray