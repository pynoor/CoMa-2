#2. Programmieraufgabe der Computerorientierten Mathematik 2

In dieser Aufgabe soll eine Liste L paarweise verschiedener Elemente bzgl. einer totalen Ordnung 
mit Heapsort sortiert werden. Dabei solen die zu sortierenden Elemente Instanzen einer Kasse E
sein, auf der die Funktion str und die Vergleichsoperaton <= definiert sind. Ferner soll die Liste L
ein Objekt einer Klasse L sein, für die die Funktionen len und str, Indizierung mittels eckiger
Klammern sowie eine Methode swp(i, j) zum Vertauschen zweier Elemente definiert sind. Die
Elemente von L sind dabei von 1 bis len(L) durchnummeriert.
Schreiben Sie eine (globale) Funktion heapsort(L), die ein Objekt einer beliebigen Klasse L
mit den oben beschriebenen Eigenschaften übergeben bekommt und mittels Heapsort vermöge
der swp-Methode in-place sortiert. Die Funktion hat keinen Rückgabewert. Definieren Sie au-
ßerdem eine konkrete Listenklasse Liste, die die oben beschriebene Funktionalität sowie einen
Konstruktor __init__(self, `) bereitstellt, dem eine python-list ` zur Initialisierung übergeben
wird. Definieren Sie ferner zwei Elementklassen DIN5007_1 und DIN5007_2, deren Instanzen
Zeichenketten repräsentieren, die anhand der DIN-Norm 5007-1 bzw. der DIN-Norm 5007-2 miteinander
verglichen werden. Die Klasse soll neben der Vergleichsoperation einen Konstruktor
__init__(self, s) bereitstellen, mit dem ein Objekt mit dem python-str s initialisiert werden
kann.

##Funktion heapsort(L):
Aufrufparameter Ein Objekt L einer Listenklasse L mit der oben beschriebenen Funktionalität.
Dabei sind die Elemente L[i] für i = 1, . . . ,len(L) Objekte einer Elementklasse E, für die die
Vergleichsoperation <= definiert ist.
Klasse Liste
Die Klasse Liste soll beliebige Listen speichern können. Zur internen Speicherung kann eine
python-list verwendet werden.

###Konstruktor __init__(self, `)
Aufrufparameter:
Eine beliebige python-list `.

###Methode __getitem__(self, i)
Aufrufparameter:
Eine Zahl i ∈ {1, . . . ,len(`)}.
Rückgabewert:
Das i-te Element der Liste. Achtung: Der Indizes beginnen mit 1!

##Methode swp(self, i, j):
Aufrufparameter:
Zwei Zahlen i, j ∈ {1, . . . ,len(`)}. Achtung: Die Indizes beginnen mit
1!
##Methode __len__(self):
Rückgabewert:
Die Länge der Liste.

##Methode __str__(self):
Rückgabewert:
str-Repräsentation der python-list [s1, s2, · · · , sn], wobei s1, . . . , sn die
str-Repräsentationen der in der Liste enthaltenen

##Klassen DIN5007_1 und DIN5007_2:
Die Klassen sollen Zeichenketten speichern. Zur internen Speicherung kann ein python-str verwendet
werden.

###Konstruktor __init__(self, s):

Aufrufparameter:
python-str, den das erstellte Objekt repräsentiert.

###Methode __le__(self, f):

Aufrufparameter:
Objekt derselben Klasse, mit dem das aktuelle Objekt verglichen werden soll.
Rückgabewert:
True, wenn das aktuelle Element bzgl. der entsprechenden Ordnung vor dem
verglichenen Element kommt oder als gleich behandelt werden. Andernfalls False. (Beispielsweise
werden Götz und Goetz bzgl. DIN 5007-2 als gleich behandelt.)

###Methode __str__(self):
Rückgabewert:
Die repräsentierte Zeichenkette als python-str

Hinweise: Die Vergleichsfunktionen für Zeichenketten anhand der DIN-Norm 5007 wurden in den
Beispielen zur 9. Programmieraufgabe aus CoMa I definiert. Das Kopieren der Umlaute aus der
pdf-Datei funktioniert nicht. Speichern Sie Ihr Programm in der UTF-8-Kodierung. Der Comajudge
testet Ihre Funktion heapsort für irgendwelche Klassen L und E, die die oben beschriebenen
Eigenschaften haben; nicht bloß für die von Ihnen erstellten Klassen Liste, DIN5007_1 und
DIN5007_2. Achten Sie also darauf, dass Ihre Funktion nur die im Text beschriebene Funktionalität
verwendet. Genauso testet der Comajudge Ihre Listenklasse auch für Listen mit anderen
Objekten als Instanzen der von Ihnen geschriebenen Klassen DIN5007_1 und DIN5007_2. Der ComaJudge
prüft, ob Sie in der Funktion heapsort die Elemente in der durch den in der Vorlesung
beschriebenen Heapsort-Algorithmus vorgegebenen Reihenfolge miteinander vertauschen.
