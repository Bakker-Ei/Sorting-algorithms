array = [6, 7, 4, 1]
n= len(array)
i= 0
while True:
    def max_heapify(n, i):
        """Deze functie sorteert dingen met een max-heap"""
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and array[left] < array[smallest]:
            smallest = left

        if right < n and array[right] < array[smallest]:
            smallest = right

        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]
            max_heapify(n, smallest)

max_heapify(n, i)
print(array)