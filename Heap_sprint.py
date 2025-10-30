import sys
import random

# Genereer X unieke getallen in willekeurige volgorde
cijfers = list(range(1, 10_00001))
random.shuffle(cijfers)

array = (cijfers)
n= len(array)
i= 0

def min_heapify(n, i):
    """Deze functie sorteert dingen met een min-heap"""
    #dit stukje code kijk wat de children zijn met de som, en maakt de parent "largest" {
    largest = i 
    left = 2 * i + 1
    right = 2 * i + 2
#   }
    
    # Dit stukje code kijkt of "largest" ook wel de grootste is, door hem te vergelijken met de twee children ervan 
    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right
#   }
    # Als een van de children groter blijkt te zijn dan wisselt hij ze om, en dan kijkt hij daarna naar de children van de omgewisselde
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        min_heapify(n, largest)


while True: 
    n = len(array)
    while True:
        for i in range(n // 2 - 1, -1, -1): #// voor af te ronden naar beneden als N oneven is, loopt alle parents door van onder naar boven
            min_heapify(n, i)

        for i in range(n - 1, 0, -1): # Pluk het grootste element eruit en voer de code opnieuw uit
            array[i], array[0] = array[0], array[i]
            min_heapify(i, 0)

        print("\nSorted array is:", array, "\n")
        sys.exit()  # stopt de hele code