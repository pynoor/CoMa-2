#1. Programmieraufgabe der Computerorientierten Mathematik 2

Eine topologische Sortierung eines gerichteten Graphen G = (V, E) ist eine Sortierung v1, v2, . . . , v|V |
von V mit i < j für alle (vi
, vj ) ∈ E.

In dieser Aufgabe sollen Sie eine Funktion topologische_sortierung(G) schreiben, die mittels
Tiefensuche eine topologischen Sortierung eines einfachen gerichteten Graphen bestimmt, falls
eine existiert. Der Graph soll dabei als Liste von Objekten vom Typ Node gegeben sein. Jedes
Node-Objekt hat als Attribute eine Liste successors aller von diesem Knoten aus erreichbaren
Knoten, eine Zeichenkette name sowie eine Zeichenkette color, die zu Beginn den Wert white
enthält und vom Algorithmus verwendet werden kann. Es kann davon ausgegangen werden, dass
alle Knoten unterschiedliche Namen haben.

Aufrufparameter:
Liste von Objekten der Klasse Node, die die Knoten eines gerichteten Graphen
G repräsentieren
Rückgabewert:
Besitzt G eine topologische Sortierung, so werden die name-Werte der Knoten
topologisch sortiert als Liste [v1,. . . ,vn] zurückgegeben. Andernfalls wird die Liste [-1] zurückgegeben.

Hinweis: Der Graph muss nicht zusammenhängend sein. Ist n = 0, so wird eine leere Liste zurückgegeben.
Verwenden Sie zum Testen Ihrer Funktion eine Klasse Node mit den oben angegebenen
Attributen. Außerdem bietet es sich zum Ausprobieren mehrerer Beispiele an, eine Funktion
zu schreiben, die anhand einer einfachen Datenstruktur für Graphen (Adjazenz-/Inzidenzliste/-
matrix) eine Liste von Knotenobjekten mit den korrekten successors-Listen erstellt.