def selectionSort(arr):
    for i in range(len(arr)-1):
        min1 = i
        for j in range(i+1, len(arr)):
            if arr[min1] > arr[j]:
                min1 = j
        arr[min1], arr[i] = arr[i], arr[min1]


a = [2, 1, -1, 8, 3, 10]
selectionSort(a)
print(a)
