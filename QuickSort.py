def quickSort(arr, low, high):
    if low < high:
        s = partition(arr, low, high)
        quickSort(arr, low, s-1)
        quickSort(arr, s+1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    j = high-1
    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] < pivot:
        arr[i], arr[low] = arr[low], arr[i]
    return i


a = [2, 1, -1, 8, 3, 10]
quickSort(a, 0, len(a)-1)
print(a)
