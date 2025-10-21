import time

array = []

def txtexport():
    """Deze functie export txt wanner je hem roept"""
    with open("heapsortarray.txt", "w") as f:
        f.write("Array: " + str(array) + "\n")

def arrayinput():
    """Deze functie vraagt wat de array moet zijn"""
    while True:
        print (array)
        arraynumber = input("add elements to the array and press enter to continue, press enter twice to save the array: ")
        if arraynumber == "":
            txtexport()
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
    time.sleep(1)
    print("Array saved to heapsortarray.txt")

def min_heapify(n, i):
    """Deze functie sorteert dingen met een min-heap"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        min_heapify(n, largest)

def max_heapify(n, i):
    """Deze functie sorteert dingen met een max-heap"""
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] < array[smallest]:
        smallest = left

    if right < n and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        max_heapify(n, smallest)

# hier worden alle functies geroepen. 
while True:
    arrayinput()
    n = len(array)
    min_max = input("van klein naar groot sorteren, druk op enter om te beginnen, anders typ 'groot naar klein' voor andersom: ")
    if min_max == "":
        for i in range(n // 2 - 1, -1, -1):
            min_heapify(n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            min_heapify(i, 0)

        print("Sorted array is:", array)
        time.sleep(2)
    elif min_max == "groot naar klein":
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            max_heapify(i, 0)

        print("Sorted array is:", array)
        time.sleep(2)