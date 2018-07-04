
class Node:
    def __init__(self,key,data):
        self.key=key
        self.left=None
        self.right=None
        self.p=None
        self.data=data

def RotateLeft(x,T):
    y=x.right
    if x.p==None:
        T.root=y
    elif x.p.left==x:
        x.p.left=y
    else:
        x.p.right=y
    y.p=x.p
    x.right=y.left
    if x.right!=None:
        x.right.p=x
    y.left=x
    x.p=y

def RotateRight(x,T):
    y=x.left

    if x.p==None:
        T.root=y
    elif x.p.right==x:
        x.p.right=y
    else:
        x.p.left=y

    y.p=x.p
    x.left=y.right
    if x.left!=None:
        x.left.p=x
    y.right=x
    x.p=y


def SplayingStep(x,T):
    i=0
    if x.p==None:
        return 0
    elif x.p.p==None and x==x.p.left:
        RotateRight(x.p,T)
        i+=1
    elif x.p.p==None and x==x.p.right:
        RotateLeft(x.p,T)
        i+=1
    elif x==x.p.left and x.p==x.p.p.left:
        RotateRight(x.p.p,T)
        RotateRight(x.p,T)
        i+=2
    elif x==x.p.right and x.p==x.p.p.right:

        RotateLeft(x.p.p,T)
        RotateLeft(x.p,T)
        i+=2
    elif x==x.p.left and x.p==x.p.p.right:
        RotateRight(x.p,T)

        RotateLeft(x.p,T)
        i+=2
    else:

        RotateLeft(x.p,T)
        RotateRight(x.p,T)
        i+=2
    return i


def help1(x):
    f=0
    d=0
    s=0
    if x!=None:
        d=help1(x.left)
        liste.append(d)
        f=help1(x.right)
        liste.append(f)
        s=1
    return f+d+s

def Splay(x,T):
    s=0
    global liste
    liste=[]
    potvor=help1(T.root)
    for el in liste:
        if el!=0:
            potvor*=el
    v=help1(x)
    while x.p!=None:
        s+=SplayingStep(x,T)

    liste=[]
    potnach1=help1(T.root)
    potnach=potnach1
    for el in liste:
        if el!=0:
            potnach*=el
    xk=x.key
    twoR=2**s
    print("Splay an Knoten:"+str(xk))
    print("2^Rotationen:"+str(twoR))
    print("2^Potential vorher:"+str(potvor))
    print("2^Potential nachher:"+str(potnach))
    print("2^amortisierte Rotationen:"+str(twoR*potnach)+"/"+str(potvor))
    print("2^obere Schranke:"+str(2*(potnach1**3))+"/"+str(v**3))




def TreeMinimum(T,x):
    while x.left!=None:
        x=x.left
    return x

def Transplant(T,u,v):
    if u.p==None:
        T.root=v
    elif u==u.p.left:
        u.p.left=v
    else:
        u.p.right=v
    if v!=None:
        v.p=u.p

def height(T):
    import math
    global liste
    liste=[]
    return (2*(math.log(help1(T.root),2))+1)//1

from tkinter import *

class SplayTree:

    def __init__(self,key,data):
        self.root=Node(key,data)

    def search(self,key):
        x=self.root
        while x!=None and key!=x.key:
            x2=x
            if key<x.key:
                x=x.left

            else:
                x=x.right

        if x!=None:

            Splay(x,self)

            return x
        else:

            Splay(x2,self)
            return None

    def insert(self,key,data):
        z=Node(key,data)
        y=None
        x=self.root
        while x!=None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        if y==None:
            self.root=z
        elif z.key<y.key:
            y.left=z
        else:
            y.right=z
        Splay(z,self)

    def delete(self,key):
        if self.root.left==None and self.root.right==None:
            return
        z=self.search(key)
        if z!=None:
            if z.left==None:
                Transplant(self,z,z.right)
            elif z.right==None:
                Transplant(self,z,z.left)
            else:
                y=TreeMinimum(self,z.right)
                if y.p!=z:
                    Transplant(self,y,y.right)
                    y.right=z.right
                    y.right.p=y
                Transplant(self,z,y)
                y.left=z.left
                y.left.p=y
        else:
            return

    def draw(self,w):


        w=w
        root=w.master

        """w=Canvas(root, width=1000, height=1000)"""
        height1=height(self)

        w.pack()
        z=w.winfo_reqwidth()
        k=w.winfo_reqheight()
        s=(z/((2**height1)))
        q=(k/(height1+2))
        boxseite=10

        def walkdraw(w,x,z,mittelbreite,mitteltiefe,boxseite,i):
                w.create_rectangle(mittelbreite-boxseite,mitteltiefe-boxseite,mittelbreite+boxseite,mitteltiefe+boxseite,fill="white")
                w.create_text(mittelbreite,mitteltiefe,text=str(x.key))
                if x.left!=None:
                    sch=z/(2**i)
                    w.create_line(mittelbreite,mitteltiefe+boxseite,mittelbreite-sch,mitteltiefe+q-boxseite)
                    walkdraw(w,x.left,z,mittelbreite-sch,mitteltiefe+q,boxseite,i+1)
                if x.right!=None:
                    sch=z/(2**i)
                    w.create_line(mittelbreite,mitteltiefe+boxseite,mittelbreite+sch,mitteltiefe+q-boxseite)
                    walkdraw(w,x.right,z,mittelbreite+sch,mitteltiefe+q,boxseite,i+1)
        walkdraw(w,self.root,z,z/2,boxseite+5,boxseite,2)




class TreeVisualizer:
    def __init__(self,tk):

        self.root=tk
        self.root.title("SplayTree Visualization")

        self.entryframe = Frame(self.root)
        self.buttonframe = Frame(self.root)
        self.canvasframe = Frame(self.root)

        self.entryframe.grid(row=0)
        self.buttonframe.grid(row=1)
        self.canvasframe.grid(row=2)

        self.keylab=Label(self.entryframe,text="key")

        self.datalab=Label(self.entryframe,text="data")
        self.e1=Entry(self.entryframe)
        self.e2=Entry(self.entryframe)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.d=Button(self.buttonframe,text="construct",command=lambda:self.construct(int(self.e1.get()),self.e2.get()))
        self.d.grid(row=0)
        self.keylab.grid(row=0)
        self.datalab.grid(row=1)

    def construct(self,key,data):

        self.d.destroy()
        self.T=SplayTree(key,data)
        self.w=Canvas(self.canvasframe,width=1000,height=1000)
        self.w.grid(row=0)
        self.T.draw(self.w)
        self.inser=Button(self.buttonframe,text="insert",command=lambda:self.insert(int(self.e1.get()),self.e2.get()))
        self.inser.grid(row=0,column=0)
        self.sear=Button(self.buttonframe,text="search",command=lambda:self.search(int(self.e1.get())))
        self.sear.grid(row=0,column=1)
        self.dele=Button(self.buttonframe,text="delete",command=lambda:self.delete(int(self.e1.get())))
        self.dele.grid(row=0,column=2)

    def insert(self,key,data):
        self.T.insert(key,data)
        self.w.destroy()
        self.w=Canvas(self.canvasframe,width=1000,height=1000)
        self.w.grid(row=0)
        self.T.draw(self.w)

    def search(self,key):
        a=self.T.search(key)
        if a==None:
            print("None")
        else:
            print((a.key,a.data))
    def delete(self,key):
        self.T.delete(key)
        self.w.destroy()
        self.w=Canvas(self.canvasframe,width=1000,height=1000)
        self.w.grid(row=0)
        self.T.draw(self.w)


