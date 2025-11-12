import sys
import random
import time
import matplotlib.pyplot as plt

# Genereer X unieke getallen in willekeurige volgorde
x_as_punten = list(range(1, 1001))
runtime = []
avarage_runtime = []
hoevaak = 10

def min_heapify(array, n, i):
    """Deze functie sorteert dingen met een min-heap"""
    #dit stukje code kijkt wat de children zijn met de som, en maakt de parent "largest" {
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
        min_heapify(array, n, largest)

for each in x_as_punten:
    totale_duur = 0
    for i in range(0, hoevaak):
        cijfers = list(range(1, each + 1)) 
        random.shuffle(cijfers)
        array = cijfers.copy()
        net = time.perf_counter()
        #main loop, dit is wat het programma runt en alle features aanroept
        n = len(array)
        for i in range(n // 2 - 1, -1, -1): #// voor af te ronden naar beneden als N oneven is, loopt alle parents door van onder naar boven
            min_heapify(array, n, i)

        for i in range(n - 1, 0, -1): # Pluk het grootste element eruit en voer de code opnieuw uit
            array[i], array[0] = array[0], array[i]
            min_heapify(array, i, 0)
        nu = time.perf_counter() # time.perf_counter() ipv time.time() want die is nauwkeuriger volgens chat
        runtime = nu - net
        totale_duur += runtime
    totale_duur = totale_duur / hoevaak
    avarage_runtime.append(totale_duur)

plt.plot(x_as_punten, avarage_runtime)
plt.xlabel('Aantal elementen in array')
plt.ylabel('Gemiddelde runtime (seconden)')
plt.title('Gemiddelde runtime van heap sort voor verschillende array groottes') 
plt.grid(True) # Voeg een raster toe aan de grafiek
plt.savefig('Heap_sort_runtime.png') # Sla de grafiek op als een PNG-bestand
plt.show()
