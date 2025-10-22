import time
import os

array = []

LOG_FILE = "heapsortarray.txt"

def clear_log():
    """Start met een lege log file."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("Heapsort steps log\n\n")

def append_log(text):
    """Voeg tekst toe aan de log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def txtexport():
    """Deze functie export txt wanner je hem roept"""
    clear_log()
    append_log("Initial array: " + str(array))

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

def clear_screen():
    """Leeg het scherm voor betere visualisatie"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tree(arr, highlights=None, msg=None, pause=0.6):
    """print de binary tree."""
    if highlights is None:
        highlights = set()
    else:
        highlights = set(highlights)

    clear_screen()
    if msg:
        print(msg)
    n = len(arr)
    level = 0
    i = 0

    tree_lines = []
    if msg:
        tree_lines.append(msg)
    while i < n:
        level_count = 2 ** level
        line_elems = []
        for j in range(level_count):
            idx = i + j
            if idx < n:
                val = str(arr[idx])
                if idx in highlights:
                    line_elems.append(f"*{idx}:{val}*")
                else:
                    line_elems.append(f"{idx}:{val}")
            else:
                line_elems.append("   ")
        line = "   ".join(line_elems)
        print(line)
        tree_lines.append(line)
        i += level_count
        level += 1
    print()

    append_log("\n".join(tree_lines))
    append_log("-" * 40)

    time.sleep(pause)

def min_heapify(n, i):
    """Deze functie sorteert dingen met een min-heap"""
    left = 2 * i + 1
    right = 2 * i + 2
    print_tree(array, highlights=(i, left, right), msg=f"min_heapify start: i={i}")
    largest = i

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        print_tree(array, highlights=(i, largest), msg=f"swapped i={i} and largest={largest}")
        min_heapify(n, largest)

def max_heapify(n, i):
    """Deze functie sorteert dingen met een max-heap"""
    left = 2 * i + 1
    right = 2 * i + 2
    print_tree(array, highlights=(i, left, right), msg=f"max_heapify start: i={i}")
    smallest = i

    if left < n and array[left] < array[smallest]:
        smallest = left

    if right < n and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        print_tree(array, highlights=(i, smallest), msg=f"swapped i={i} and smallest={smallest}")
        max_heapify(n, smallest)

# hier worden alle functies geroepen. 
while True:
    arrayinput()
    n = len(array)
    min_max = input("van klein naar groot sorteren, druk op enter om te beginnen, anders typ 'groot naar klein' voor andersom: ")
    if min_max == "":
        clear_log()
        append_log("Starting min-heap sort")
        append_log("Initial array: " + str(array))
        for i in range(n // 2 - 1, -1, -1):
            min_heapify(n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            print_tree(array, msg=f"after swap with i={i}")
            min_heapify(i, 0)

        append_log("Sorted array is: " + str(array))
        print("Sorted array is:", array)
        time.sleep(2)
    elif min_max == "groot naar klein":
        clear_log()
        append_log("Starting max-heap sort")
        append_log("Initial array: " + str(array))
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            print_tree(array, msg=f"after swap with i={i}")
            max_heapify(i, 0)

        append_log("Sorted array is: " + str(array))
        print("Sorted array is:", array)
        time.sleep(2)