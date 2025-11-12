import time
import os
import sys 
import random
# Visualisatie imports
try:
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib import animation
except ImportError:
    print("FOUT: matplotlib en networkx zijn vereist voor deze visualisatie!")
    print("Installeer met: pip install matplotlib networkx")
    exit()

#doe het 2e cijfer een **hoger** dan wat je echt wil
array = list(range(1, 16))  # Pas hier de lengte van de array aan
random.shuffle(array) # Schud de array willekeurig

LOG_FILE = "heapsortarray.txt"

# Momentopnames voor grafische visualisatie
momentopnames = []
# Functie om stappen te loggen
def registreer(arr, heap_grootte, actief=None):
    """Sla een kopie op van de huidige toestand voor animatie."""
    momentopnames.append({ # 'array': [...], 'heap_grootte': int, 'actief': (int, int) }
        'array': arr.copy(), # huidige array toestand
        'heap_grootte': heap_grootte, # huidige grootte van de heap
        'actief': actief # welke indexen zijn actief (vergelijkd, gewisseld)
    })
# Min-heapify functie
def min_heapify(n, i):
    links = 2 * i + 1
    rechts = 2 * i + 2
# Controleer of kinderen binnen bereik zijn
    if links >= n and rechts >= n: # beide kinderen buiten bereik
        return
# Bepaal welke van de kinderen groter is
    if links < n and rechts < n: #  links < n and rechts < n
        registreer(array, n, actief=(links, rechts))
        gekozen = links if array[links] > array[rechts] else rechts
    elif links < n: # links < n
        registreer(array, n, actief=(links,))
        gekozen = links
    else: # rechts < n
        registreer(array, n, actief=(rechts,))
        gekozen = rechts
# Vergelijk en wissel indien nodig
    registreer(array, n, actief=(i, gekozen))
    if array[gekozen] > array[i]:
        array[i], array[gekozen] = array[gekozen], array[i]
        registreer(array, n, actief=(i, gekozen))
        min_heapify(n, gekozen)
# Max-heapify functie # voor sorteren van groot naar klein
def max_heapify(n, i):
    links = 2 * i + 1
    rechts = 2 * i + 2

    if links >= n and rechts >= n: # beide kinderen buiten bereik
        return

    if links < n and rechts < n: # links < n and rechts < n
        registreer(array, n, actief=(links, rechts))
        gekozen = links if array[links] < array[rechts] else rechts
    elif links < n: # links < n
        registreer(array, n, actief=(links,))
        gekozen = links
    else: # rechts < n
        registreer(array, n, actief=(rechts,))
        gekozen = rechts
# Vergelijk en wissel indien nodig
    registreer(array, n, actief=(i, gekozen))
    if array[gekozen] < array[i]: #wijziging hier voor max-heap
        array[i], array[gekozen] = array[gekozen], array[i]
        registreer(array, n, actief=(i, gekozen))
        max_heapify(n, gekozen)
# Bereken posities voor visualisatie
def bereken_posities(n):
    """Bereken waar elke node in de boom moet komen."""
    posities = {}
    niveau = 0
    index = 0
    # Totale niveaus in de boom
    # Ga door elk niveau van de boom
    while index < n:
        aantal_op_niveau = 2 ** niveau  # Niveau 0: 1 node, niveau 1: 2 nodes, niveau 2: 4 nodes, etc.
        nodes_op_dit_niveau = list(range(index, min(n, index + aantal_op_niveau)))
        breedte = len(nodes_op_dit_niveau)
        
        # Verdeel de nodes gelijk over de breedte
        for i, node in enumerate(nodes_op_dit_niveau):
            x_positie = (i + 0.5) / breedte
            y_positie = -niveau
            posities[node] = (x_positie, y_positie)
        
        index += aantal_op_niveau
        niveau += 1
    # Geef de berekende posities terug
    return posities

def maak_grafische_visualisatie():
    """Maak en toon de grafische animatie."""
    if len(momentopnames) == 0:
        return
    
    print("\n=== Maak grafische visualisatie ===")
    
    n = len(array)
    
    # Maak een graph (netwerk van nodes en verbindingen)
    graph = nx.Graph()
    graph.add_nodes_from(range(n))  # Voeg alle nodes toe (0 tot n-1)
    
    # Voeg verbindingen toe tussen ouders en kinderen
    for i in range(n):
        linkerkind = 2 * i + 1
        rechterkind = 2 * i + 2
        if linkerkind < n:
            graph.add_edge(i, linkerkind)
        if rechterkind < n:
            graph.add_edge(i, rechterkind)
    
    # Bereken waar elke node moet staan in de visualisatie
    posities = bereken_posities(n)
    
    # Maak een figuur (venster) voor de animatie
    figuur, tekengebied = plt.subplots(figsize=(12, 7))
    tekengebied.set_axis_off()  # Verberg de assen
    
    def teken_frame(frame_nummer):
        """Teken één frame van de animatie."""
        tekengebied.clear()
        # Haal de snapshot op voor dit frame
        snapshot = momentopnames[frame_nummer]
        waardes = snapshot['array']
        actieve_nodes = snapshot.get('actief', None)
        heap_grootte = snapshot.get('heap_grootte', n)  # terugval op n
        
        tekengebied.set_title(f"Heap Sort Visualisatie - Stap {frame_nummer + 1} van {len(momentopnames)}", fontsize=14, fontweight='bold')
        
        # Bepaal de grootte en kleur van elke node
        node_groottes = []
        node_kleuren = []
        basis_grootte = 800
        
        for i in range(n):
            if actieve_nodes and i in actieve_nodes:
                # Actieve nodes zijn groot en geel
                node_groottes.append(basis_grootte * 1.2)
                node_kleuren.append('yellow')
            elif i >= heap_grootte:
                # Gesorteerde nodes zijn groen
                node_groottes.append(basis_grootte)
                node_kleuren.append('lightgreen')
            else:
                # Normale nodes zijn blauw
                node_groottes.append(basis_grootte)
                node_kleuren.append('skyblue')
        
        # Teken de verbindingen tussen nodes
        nx.draw_networkx_edges(graph, pos=posities, ax=tekengebied, width=2)
        
        # Teken de nodes zelf
        nx.draw_networkx_nodes(graph, pos=posities, ax=tekengebied, 
        node_size=node_groottes, 
        node_color=node_kleuren,
        linewidths=2)
        
        # Teken de waardes in de nodes
        labels = {i: str(waardes[i]) for i in range(n)}
        nx.draw_networkx_labels(graph, pos=posities, labels=labels, 
        font_size=12, font_weight='bold')
        
    # Maak de animatie
    print("Bezig met animeren...")
    animatie = animation.FuncAnimation(figuur, teken_frame,
    frames=len(momentopnames), 
    repeat=False)
    #functie die snelheid baseert op array lengt, in mm/frame
    if len(array) < 17:
        interval=400, 
    else: 
        interval=150, 
    # Toon de animatie direct in een venster
    print("Animatie wordt getoond...")
    print("Sluit het venster om door te gaan.")
    plt.show()
    # Eindbericht
    print("Animatie voltooid!\n")
    sys.exit()

# Hoofdlus - hier worden alle functies aangeroepen
while True:
    # Bepaal de lengte van de array
    n = len(array)
    # Controleer of de array leeg is
    if n == 0:
        print("Array is leeg, voeg eerst elementen toe.")
        break
    # Maak het logbestand leeg
    momentopnames.clear()
    # Vraag de gebruiker om de sorteervolgorde
    min_max = input("Typ < om van klein naar groot te sorteren, en > om van groot naar klein te sorteren: ")
    # Voer de juiste heapsort uit op basis van de keuze
    if min_max == "<":
        ()
        ("Start min-heap sort")
        ("Initiële array: " + str(array))
        # Bouw de min-heap
        registreer(array, n)
        
        for i in range(n // 2 - 1, -1, -1):
            min_heapify(n, i)
        # Registreer de bouw van de heap
        registreer(array, n)
        # Sorteer de array
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            registreer(array, i, actief=(0, i))
            min_heapify(i, 0)
        # Registreer de voltooiing van de sortering
        registreer(array, 0)
        # Toon het resultaat
        ("Gesorteerde array is: " + str(array))
        print("Gesorteerde array is:", array)
        
        maak_grafische_visualisatie()
    # Max-heap sort
    elif min_max == ">":
        ()
        ("Start max-heap sort")
        ("Initiële array: " + str(array))
        # Bouw de max-heap
        registreer(array, n)
        
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(n, i)
        # Registreer de bouw van de heap
        registreer(array, n)
        # Sorteer de array
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            registreer(array, i, actief=(0, i))
            max_heapify(i, 0)
        # Registreer de voltooiing van de sortering
        registreer(array, 0)
        # Toon het resultaat
        ("Gesorteerde array is: " + str(array))
        print("Gesorteerde array is:", array)
        
        maak_grafische_visualisatie()