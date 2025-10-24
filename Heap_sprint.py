array = []

def arrayinput():
    """Deze functie vraagt wat de array moet zijn"""
    while True:
        print (array)
        arraynumber = input("add elements to the array and press enter to continue, press enter twice to save the array: ")
        if arraynumber == "":
            break
        elif arraynumber == "stop":
            break
        elif arraynumber.startswith ("remove "):
            try:
                num_to_remove = int(arraynumber[len("remove "):])
                if num_to_remove in array:
                    array.remove(num_to_remove)
                else:
                    print("{int(arraynumber)} is not in the array.")
            except ValueError:
                print("Please enter a valid integer to remove.")
        else:
            try:
                int(arraynumber)
                array.append(int(arraynumber))
            except ValueError:
                print("Please enter a valid integer, 'stop' to finish or 'remove ...' to remove a number.")
    print("Array saved to heapsortarray.txt")

def min_heapify(n, i):
    """Deze functie sorteert dingen met een min-heap"""
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        min_heapify(n, largest)

while True:
    arrayinput()
    if array:
        min_heapify(len(array), 0)