# Schoolproject **Heapsort**
## Gemaakt door: Yannis, Selton en Maurits.

## Wat wij allemaal gemaakt hebben
Wij hebben 3 verschillende scripts gemaakt, eentje om allemaal verschillende dingen met heap-sort te doen, een om een hele snelle sort te maken, en de laatste is om te visualiseren met Matplotlib en NetworkX. deze kan je [hier](#de-drie-branches) vinden

### De drie branches
Er zijn drie branches in deze repository, eentje om te visualiseren, eentje om snel te zijn, en de laatste om interactief te zijn


[Snelle sort](https://github.com/Bakker-Ei/Sorting-algorithms/tree/Sprintje)
[Interactive sort](https://github.com/Bakker-Ei/Sorting-algorithms/tree/Geen-Visualizer)
[Visuele sort](https://github.com/Bakker-Ei/Sorting-algorithms/tree/main)

## Logboek
Dit project hebben wij een ogboek bijgehouden om te zien wat we wanneer gedaan hebben
Lees het volledige logboek [hier](./Logboek.txt).

# Hoe het project verliep
wij begonnen met het idee om een hele simpele heap-sort code te maken waarin je een array gaf via de input en deze daarna gesorteerd werdt of in een min of in een max heap. nadat we deze gemaakt hadden (in de branch [Geen visualuzer](https://github.com/Bakker-Ei/Sorting-algorithms/tree/Geen-Visualizer)) hadden we door dat het ook slim zou zijn om een HEEL simpele code te hebben die alleen maar het sorteren doet, zodat we hier sneller klaar mee zijn. dit hadden we net op tijd bedacht, want dit project gaat natuurlijk ook over complexiteit, en dan is het heel fijn om niet al die andere stappen mee te moeten rekenen. We wilden ook een visualisatie van de heap sort hebben, zodat we ook beter konden leren **zelf** te heap-sorten. hier kwamen we wel *behoorlijk* wat problemen in tegen. Om te beginnen, had ***Selton*** een code geshcreven (in main... vandaar dat we aftakten daarna) die bij iedere stap de integers printte. het probleem hiermee is dat ze nooit echt gecentreerd werden in een binaire boom, en er stonden geen slashes. **Yannis** ***dacht*** dat hij het beter zou weten en probeerde deze code te "fixen". hoewel Yannis de slashes toegevoegd heeft, werd het centreerprobleem nog erger, en iedereen in ons groepje wou eigenlijk opgeven, want dit leek ons geen realistische taak. Uiteindelijk kreeg de oh zo eigenwijze Yannis het idee om dit te visualizeren, maar toen liepen wij een ander probleem tegenmoet ***HOE CODEREN WE DIT?!?!?*** na wat brainstormen, kwamen we op het idee om matplotlib te gebruiken om nodes erin te zetten, en Yannis kreeg daarna het idee om met NetworkX deze nodes met elkaar te verbinden. dit was een heel pittig taakje, en na 7 uur lang hieraan te werken *in een sitting* (leertijd meegeteld) deed hij het eindelijk.


## Uitleg van het algoritme (zonder code)
Heap sort bestaat uit twee hoofddelen:
1. Het opbouwen van een heap (binaire boom waarbij elke ouder groter is dan zijn kinderen bij een max-heap).
2. Het telkens verwijderen van het grootste element (de wortel van de heap) en het verplaatsen naar het einde van de lijst.

In woorden:
- Eerst wordt de invoerlijst omgevormd tot een max-heap met de heapify functie.
- Dan wissel je steeds het eerste (grootste) element met het laatste ongesorteerde element.
- Vervolgens verklein je de heap om het laatste element eruit te halen en pas je heapify opnieuw toe.
- Dit proces herhaal je tot de lijst volledig gesorteerd is.

De pseudocode hiervan vind je [hier](https://github.com/Bakker-Ei/Sorting-algorithms/blob/main/pseudocode.md)

## Best case en worst case uitleg
**Best case:**  
Bij heap sort maakt het niet uit of de lijst al gesorteerd is, want de heap wordt altijd opnieuw opgebouwd.  
De best case heeft dus **geen verschil** in het aantal stappen vergeleken met andere gevallen.

**Worst case:**  
Zoals hierboven al benoemd, de volgorde van de lijst maakt niet uit. Zelfs als de lijst volledig omgekeerd is of willekeurig staat, gaat het algoritme net zo snel als bij een bijna gesorteerde lijst. Dat komt omdat het altijd de heap opbouwt en steeds de wortel verplaatst en opnieuw heapify uitvoert. Hierdoor blijft de tijdscomplexiteit altijd O(n log n).

## Complexiteit - in theorie
**Best case complexiteit:** O(n log n)  
**Worst case complexiteit:** O(n log n)

**Waarom:**  
- Het opbouwen van de heap kost O(n).
- Elke extractie van het grootste element kost O(log n) (om de heap opnieuw te herstellen).
- Omdat dit n keer gebeurt, krijg je n * log n = O(n log n).
Heap sort heeft dus een stabiele tijdscomplexiteit, ongeacht de invoer.

## Complexiteit - in praktijk
we hebben met behulp van time.perf_counter gemeten hoe lang het duurde voor ons programma om een reeks getallen te sorteren, door dit heel vaak te herhalen kregen we de volgende grafiek
![Onze grafiek](https://github.com/Bakker-Ei/Sorting-algorithms/blob/main/Kloppende%20l-ei-n%20na%20poging%2023%20.png)

hier kunnen we duidelijk een O(n log n) grafiek zien