#3. Programmieraufgabe der Computerorientierten Mathematik 2

Der Bellman-Ford-Algorithmus und der Kürzeste-Pfade-Algorithmus für azyklische gerichtete
Graphen sind zwei Spezialisierungen des (generischen) Algorithmus von Ford, die genauer spezifizieren,
welche Kante (mit verletzter Potentialbedingung) in jedem Schritt ausgewählt wird.
In dieser Aufgabe soll eine Funktion ford(G, r) geschrieben werden, die beide Spezialisierungen
realisieren kann, indem sie zur Auswahl der nächsten zu prüfenden Kante auf eine Methode
next_edge() des übergebenen Graphen G zurückgreift. Dieser kann dabei entweder eine Instanz
der Klasse DirectedGraph oder eine Instanz der Klasse DAG sein, die beide von der unten stehenden
Klasse AbstractGraph abgeleitet sind. Beide Klassen überschreiben die Methode next_edge(),
so dass sie in jedem Schritt die nächste im Algorithmus von Bellman-Ford bzw. im KürzestePfade-Algorithmus
für azyklische gerichtete Graphen betrachtete Kante zurückgibt.
Die Graphenklassen verwenden zur Speicherung der Knoten und Kanten Objekte der Klassen Node
und Edge (siehe unten). Jedes Node-Objekt hat die Attribute y, p und eine Liste outgoing aller
ausgehenden Kanten. Jede Kante hat als Attribute den Startknoten start, den Endknoten target
sowie ihre Länge c. Die Klassen AbstractGraph, Node und Edge sollen nicht verändert werden.
Aufrufparameter der Funktion ford(G, r) Ein gewichteter einfacher gerichteter Graph G ohne
negative Kreise als Objekt der Klasse DirectedGraph oder ein gewichteter einfacher gerichteter
azyklischer Graph als Objekt der Klasse DAG.

##Nachbedingung nach Ausführung von ford(G, r):
Für jeden Knoten v des Graphen enthält das
y-Attribut des ihn repräsentierenden Node-Objekts die Länge eines kürzesten r-v-Pfades und das
p-Attribut den Vorgänger auf einem kürzesten r-v-Pfad, falls ein solcher Pfad existiert. Andernfalls
enthält y den Wert inf und p den Wert None. Für r enthält das p-Attribut ebenfalls den Wert None.
Klasse DirectedGraph
Die Klasse speichert einen einfachen gerichteten Graphen G = (V, E) mit Kantenlängen c ∈ R
ohne negative Kreise.

Rückgabewert der Methode next_edge():
Die nächste Kante aus der Sequenz S1, . . . , S|V |−1
,
wobei S1, . . . , S|V |−1 beliebige Sortierungen von E sind. Ist die Sequenz zu Ende, wird None
zurückgegeben.

##Klasse DAG:
Die Klasse speichert einen einfachen gerichteten Graphen G = (V, E) mit Kantenlängen c ∈ R
ohne gerichtete Kreise.

###Rückgabewert der Methode next_edge():
Die nächste Kante aus einer Sortierung S von E mit
der Eigenschaft, dass es eine topologische Sortierung v1, . . . , v|V | von V gibt, so dass für jedes Paar
(vi
, vj ),(vk, v`) von Kanten gilt: Falls i < k, so kommt (vi
, vj ) in S vor (vk, v`). Ist die Sortierung
zu Ende, wird None zurückgegeben.

Hinweise: Die Klassen Node und Edge erlauben das Hinzufügen neuer Attribute. Damit können Sie
den Graphen in das Eingabeformat der ersten Programmieraufgabe überführen und Ihre Funktion
topologische_sortierung(G) von dort für die Klasse DAG wiederverwenden. Sie müssen die
Funktion lediglich so abwandeln, dass sie die Liste der Knoten anstatt der Liste der Namen
zurückgibt. Der Test, ob die Potentialbedingung verletzt ist, muss in der Funktion ford geschehen;
die Methoden next_edge() Ihrer beiden Klassen müssen alle Kanten gemäß einer Sequenz
mit den jeweils oben beschriebenen Eigenschaften zurückgeben, unabhängig davon, ob sie die
Potentialbedingung erfüllen, denn der Comajudge testet, ob Ihre Rückgabereihenfolge die oben
genannten Bedingungen erfüllt. Für ein Graphenobjekt lässt sich der Ford-Algorithmus nur einmal
ausführen, da danach die next_edge()-Methode nur noch den Wert None zurückgibt. (Wenn
Sie möchten, können Sie eine reset()-Methode hinzufügen. Dies ist aber nicht gefordert.) Sie
müssen aber dennoch zu Beginn des Algorithmus die y- und p-Attribute der Knoten initialisieren,
da der Algorithmus nacheinander für unterschiedliche Graphenobjekte mit denselben Knotenund
Kantenobjekten ausgeführt werden kann (siehe Beispielaufrufe).
