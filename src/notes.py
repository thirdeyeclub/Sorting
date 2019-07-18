aee = [8, 1, 4, 0 , 5 , 12]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        beforeI = i-1
        while arr[beforeI] > arr[beforeI + 1] and beforeI >=0:
            arr[beforeI], arr[beforeI + 1] = arr[beforeI + 1], arr[beforeI]
            beforeI -= 1
    return arr

print('insertion :',insertion_sort(aee))   

def bubble_sort( arr ):
    for i in range(0, len(arr) -1 ):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[j] , arr[i] = arr[i] , arr[j]
    return arr

print('bubble:', bubble_sort(aee))