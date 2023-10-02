from random import *
import math 
import time

class  prout:
    score =0
    couleur =0
    speed =1
    time = 1
    play = True
    
    def __init__(self):
        self.couleur : "red"
        self.score : 0
        self.speed : 1
        self.time : 1
        self.play : True

def taisuu(caca):
    caca.speed = caca.speed * math.log((caca.score))
    caca.time *= 1/caca.speed
    return(caca)

def next(caca, liste):
    a = liste[caca.score]
    if a:
        if a == "+" : 
            caca = taisuu(caca)
            suite(caca, liste, couleur)
        elif a != caca.couleur:
            caca.play = False
            caca.score-= 1
    caca.score+= 1
    return(caca)

def seg(liste, couleur):
    i = 10 + randint(1,10)
    c = choice(couleur)
    for i in range(i): 
        liste.append("")
    i = randint(1,10)
    for i in range(i):
        liste.append(c)
    liste.append("+")
    return(liste)

def seque(liste, caca):
    for i in range(10 * caca.speed):
        liste.append("")
    return(liste)

def suite(caca, liste, couleur):
    n = (math.log((1 + caca.score * caca.speed)) +1) * 30
    print(n, caca.speed)
    l= []
    for i in range(int(n)):
        liste = seg(liste, couleur)
    return(liste)
    
def test(liste, caca):
    if caca.couleur in (couleur) :
        print(caca.couleur, " prout", caca.score)
    else :
        print("caca - ", caca.score)
    caca.couleur = liste[caca.score]
    return(caca)

def start(couleur):
    caca = prout()
    print(caca.play)
    bite = []
    bite = seque(bite, caca)
    bite = suite(caca, bite, couleur)
    print(bite, " prout")
    while caca.play == True:
        caca = test(bite, caca)
        time.sleep(caca.time/2)
        print(caca.time)
        caca = next(caca, bite)
        
        

couleur = ["blue", "red", "green"]

start(couleur)
