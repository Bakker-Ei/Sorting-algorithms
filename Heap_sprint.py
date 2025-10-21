from Heap_sort import min_heapify, arrayinput, txtexport

array = []

while True:
    arrayinput
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        min_heapify(i, 0)
    print("Sorted array is:", array)
    txtexport()
    print("Array saved to heapsortarray.txt")