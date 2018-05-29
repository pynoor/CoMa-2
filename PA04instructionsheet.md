#4. Programmieraufgabe der Computerorientierten Mathematik 2

In dieser Aufgabe sollen Sie Kruskals Algorithmus implementieren, um einen kostenminimalen
aufspannenden Baum eines zusammenhängenden Graphen G = (V, E) zu bestimmen, wobei eine
als Wald implementierte Union-Find-Datenstruktur mit Pfadkompression zu verwenden ist. Der
Graph ist dabei als Inzidenzliste IG gegeben, wobei wir annehmen, dass V = {0, . . . , |V | − 1}
durchnummeriert ist; für jedes i ∈ {0, . . . , |V |−1} ist IG[i] die Liste aller zum Knoten i inzidenten
Kanten als Objekte der Klasse Edge. Die Klasse Edge hat als Attribute eine (zweielementige)
Menge vertices der inzidenten Knoten und das Gewicht w der Kante.
Schreiben Sie eine Klasse UnionFind mit den Methoden make_set(), find_set(i) und union(i, j)
sowie eine (globale) Funktion kruskal(IG). Ein Objekt der Klasse UnionFind soll zur internen
Speicherung der Mutterknoten und der Größen der Zusammenhangskomponenten eine Liste p
verwenden.
Aufrufparameter der Funktion kruskal(IG) Inzidenzliste eines zusammenhängenden ungerichteten
Graphen mit nichtnegativen reellen Kantengewichten als Liste von Listen von EdgeObjekten.
Rückgabewert der Funktion kruskal(IG) Die Menge aller Kanten (Edge-Objekte) eines kostenminimalen
aufspannenden Baumes des Graphen G.

##Klasse UnionFind
Eine Instanz der Klasse UnionFind speichert den aktuellen Zustand des Union-Find-Waldes in
einer Liste p, wobei für i ∈ {0, . . . , |V | − 1} der Wert von p[i] folgendermaßen definiert ist:
- Ist der Knoten i Wurzel seines Union-Find-Baumes, so ist p[i] = −s(i), wobei s(i) die
Größe des Union-Find-Baumes mit Wurzel i ist.
- Ist der Knoten i nicht die Wurzel seines Union-Find-Baumes, so enthält p[i] die Nummer
des Mutterknotens von i.
Initialisator __init__(self) Initialisiert p mit einer leeren Liste.

##Methode make_set(self) :
Hängt eine −1 an die Liste p an, die einen neuen aus einem Knoten
bestehenden Union-Find-Baum repräsentiert.
Methode find_set(self, i) Setzt die p-Werte aller Knoten auf dem Weg vom Knoten i zur
Wurzel r des i enthaltenden Union-Find-Baumes (außer der Wurzel selbst) auf r (Pfadkompression)
und gibt r zurück.

##Methode union(self, i, j) :
Ruft die Funktion find_set für i und j auf und hängt danach den
kleineren Baum an den größeren, d. h. der p-Wert der Wurzel des kleineren Baumes wird auf die
Wurzel des größeren Baumes gesetzt und der p-Wert der Wurzel des größeren Baumes wird auf
die Größe des vereinigten Baumes gesetzt. Bei Gleichstand wird irgendeiner der Bäume an den
anderen gehängt.
Bemerkung: Ist vor der Ausführung von union(i, j) der Knoten i in dem kleineren Baum (und
nicht die Wurzel), so geben die p-Werte der Knoten auf dem Weg von i zur Wurzel des kleineren
Baumes nach der union-Operation immer noch die Nummer der Wurzel des ursprünglichen
Baumes und nicht des neuen Teilbaums an.
Hinweis: Obwohl der Algorithmus von Kruskal nur über die bereitgestellten Methoden auf die von
der Union-Find-Datenstruktur verwendete Liste zugreift, muss diese in dieser Aufgabe in einem
(öffentlichen) Attribut mit dem Namen p gespeichert sein, damit der Comajudge testen kann, ob
Sie wirklich wie gefordert eine als Wald implementierte Union-Find-Datenstruktur mit Pfadkompression
verwenden. In Anwendungen ohne Comajudge wäre es besser, ein privates Attribut zu
verwenden, um den direkten Zugriff zu verhindern. Die Klasse Edge soll nicht verändert werden.