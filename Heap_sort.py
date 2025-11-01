import time
import os
import sys 
# Visualisatie imports
try:
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib import animation
except ImportError:
    print("FOUT: matplotlib en networkx zijn vereist voor deze visualisatie!")
    print("Installeer met: pip install matplotlib networkx")
    exit()

array = []
LOG_FILE = "heapsortarray.txt"

# Momentopnames voor grafische visualisatie
momentopnames = []

def wis_log():
    """Start met een lege log file."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("Heapsort stappen log\n\n")

def voeg_log_toe(tekst):
    """Voeg tekst toe aan de log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(tekst + "\n")

def txt_export():
    """Deze functie export txt wanneer je hem roept"""
    wis_log()
    voeg_log_toe("Initiële array: " + str(array))

def array_invoer():
    """Deze functie vraagt wat de array moet zijn"""
    while True:
        print(array)
        array_getal = input("voeg elementen toe aan de array en druk op enter om door te gaan, druk twee keer op enter om de array op te slaan: ")
        if array_getal == "":
            txt_export()
            break
        elif array_getal == "stop":
            break
        elif array_getal.startswith("remove "):
            try:
                num_te_verwijderen = int(array_getal[len("remove "):])
                if num_te_verwijderen in array:
                    array.remove(num_te_verwijderen)
                else:
                    print(f"{num_te_verwijderen} zit niet in de array.")
            except ValueError:
                print("Voer een geldig getal in om te verwijderen.")
        else:
            try:
                int(array_getal)
                array.append(int(array_getal))
            except ValueError:
                print("Voer een geldig getal in, 'stop' om te stoppen of 'remove ...' om een getal te verwijderen.")
    time.sleep(1)
    print("Array opgeslagen in heapsortarray.txt")

def registreer(arr, heap_grootte, actief=None):
    """Sla een kopie op van de huidige toestand voor animatie."""
    momentopnames.append({
        'array': arr.copy(),
        'heap_grootte': heap_grootte,
        'actief': actief
    })

def min_heapify(n, i):
    links = 2 * i + 1
    rechts = 2 * i + 2

    if links >= n and rechts >= n:
        return

    if links < n and rechts < n:
        registreer(array, n, actief=(links, rechts))
        gekozen = links if array[links] > array[rechts] else rechts
    elif links < n:
        registreer(array, n, actief=(links,))
        gekozen = links
    else:
        registreer(array, n, actief=(rechts,))
        gekozen = rechts

    registreer(array, n, actief=(i, gekozen))
    if array[gekozen] > array[i]:
        array[i], array[gekozen] = array[gekozen], array[i]
        registreer(array, n, actief=(i, gekozen))
        min_heapify(n, gekozen)

def max_heapify(n, i):
    links = 2 * i + 1
    rechts = 2 * i + 2

    if links >= n and rechts >= n:
        return

    if links < n and rechts < n:
        registreer(array, n, actief=(links, rechts))
        gekozen = links if array[links] < array[rechts] else rechts
    elif links < n:
        registreer(array, n, actief=(links,))
        gekozen = links
    else:
        registreer(array, n, actief=(rechts,))
        gekozen = rechts

    registreer(array, n, actief=(i, gekozen))
    if array[gekozen] < array[i]:
        array[i], array[gekozen] = array[gekozen], array[i]
        registreer(array, n, actief=(i, gekozen))
        max_heapify(n, gekozen)

def bereken_posities(n):
    """Bereken waar elke node in de boom moet komen."""
    posities = {}
    niveau = 0
    index = 0
    
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
    
    return posities

def maak_grafische_visualisatie():
    """Maak en toon de grafische animatie."""
    if len(momentopnames) == 0:
        return
    
    print("\n=== Maak grafische visualisatie ===")
    
    n = len(array)
    
    # Maak een graaf (netwerk van nodes en verbindingen)
    graaf = nx.Graph()
    graaf.add_nodes_from(range(n))  # Voeg alle nodes toe (0 tot n-1)
    
    # Voeg verbindingen toe tussen ouders en kinderen
    for i in range(n):
        linkerkind = 2 * i + 1
        rechterkind = 2 * i + 2
        if linkerkind < n:
            graaf.add_edge(i, linkerkind)
        if rechterkind < n:
            graaf.add_edge(i, rechterkind)
    
    # Bereken waar elke node moet staan in de visualisatie
    posities = bereken_posities(n)
    
    # Maak een figuur (venster) voor de animatie
    figuur, tekengebied = plt.subplots(figsize=(12, 7))
    tekengebied.set_axis_off()  # Verberg de assen
    
    def teken_frame(frame_nummer):
        """Teken één frame van de animatie."""
        tekengebied.clear()
        
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
        nx.draw_networkx_edges(graaf, pos=posities, ax=tekengebied, width=2)
        
        # Teken de nodes zelf
        nx.draw_networkx_nodes(graaf, pos=posities, ax=tekengebied, 
        node_size=node_groottes, 
        node_color=node_kleuren,
        linewidths=2)
        
        # Teken de waardes in de nodes
        labels = {i: str(waardes[i]) for i in range(n)}
        nx.draw_networkx_labels(graaf, pos=posities, labels=labels, 
        font_size=12, font_weight='bold')
        
    # Maak de animatie
    print("Bezig met animeren...")
    animatie = animation.FuncAnimation(figuur, teken_frame, 
    frames=len(momentopnames), 
    interval=600,  # 600ms per frame
    repeat=False)
    
    # Toon de animatie direct in een venster
    print("Animatie wordt getoond...")
    print("Sluit het venster om door te gaan.")
    plt.show()
    
    print("Animatie voltooid!\n")
    sys.exit()

# Hoofdlus - hier worden alle functies aangeroepen
while True:
    array_invoer()
    n = len(array)
    
    if n == 0:
        print("Array is leeg, voeg eerst elementen toe.")
        continue
    
    momentopnames.clear()
    
    min_max = input("Typ < om van klein naar groot te sorteren, en > om van groot naar klein te sorteren: ")
    
    if min_max == "<":
        wis_log()
        voeg_log_toe("Start min-heap sort")
        voeg_log_toe("Initiële array: " + str(array))
        
        registreer(array, n)
        
        for i in range(n // 2 - 1, -1, -1):
            min_heapify(n, i)
        
        registreer(array, n)
        
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            registreer(array, i, actief=(0, i))
            min_heapify(i, 0)
        
        registreer(array, 0)
        
        voeg_log_toe("Gesorteerde array is: " + str(array))
        print("Gesorteerde array is:", array)
        
        maak_grafische_visualisatie()
        
    elif min_max == ">":
        wis_log()
        voeg_log_toe("Start max-heap sort")
        voeg_log_toe("Initiële array: " + str(array))
        
        registreer(array, n)
        
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(n, i)
        
        registreer(array, n)
        
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            registreer(array, i, actief=(0, i))
            max_heapify(i, 0)
        
        registreer(array, 0)
        
        voeg_log_toe("Gesorteerde array is: " + str(array))
        print("Gesorteerde array is:", array)
        
        maak_grafische_visualisatie()