heap sort

input: array a
output: array a (sorted)

1. vraag user om een aantal getallen en zet die in een array (array a)
    11. vraag naar getal
    12. kijk of de input een intiger is of een ander commando
    13. als het een ander commando is, voer het uit
    14. zet getal in array
    15. ga terug naar stap 11, bahalve wanneer de input 'stop' of "enter" is. in dat geval is stap 1 klaar

2. sort de array met behulp van een binary tree
    21. begint onderin de tree
    22. vergelijkt de twee onderste waardes met elkaar
    23. vergelijkt de hoogste met de parent van die 2 waarden
    24. als de parent kleiner is wisselt hij die om, anders niks
    25. ga terug naar 21
    26. als niks aangepast wordt, stop.

3. print/export de binary tree stappen
    31. maak een binary tree aan met de array in de startvolgorde
        311. print dit in een txt bestnd
    32. kijk of er iets aanpast in de binary tree nadat hij 2 een keer gedaan heeft
        321. print de nieuwe binary tree in de txt (op arrayvolgorde)
    33. kijk of 2 herhaalt, zo ja ga terug naar 32

4. print/export de gesorteede array naar een .txt bestand en print in console
    41. print de gesorteerde array in console
    42. export de array naar het .txt
