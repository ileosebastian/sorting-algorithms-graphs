import time

def insertion_sort(A, drawData_insertion, timeTick):
    length = len(A)
    for j in range(1,len(A)):
    
        key = A[j]

        i = j - 1
        while i >= 0 and A[i] > key:
            drawData_insertion(A, ['green' if x == i+1 else 'red' for x in range(length)])
            time.sleep(timeTick)
            A[i+1] = A[i]
            drawData_insertion(A, ['green' if x == i+1 else 'red' for x in range(length)])
            time.sleep(timeTick)
            i = i - 1 
        A[i+1] = key
        drawData_insertion(A, ['green' if x == i+1 else 'red' for x in range(length)])
        time.sleep(timeTick)
    drawData_insertion(A, ['green' for x in range(length)])
        