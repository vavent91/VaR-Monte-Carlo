import random as rd
deck_raw = []
deck = []
rand = []
player1=[]
player2=[]
player3=[]
player4=[]
for i in range (1,52):
    deck_raw.append(i)
strCardNames = ["A", "K", "Q","J","T","9","8","7","6","5","4","3","2"]
for i in range(0,52):
    deck.append(0)
    rand.append(0)
for i in range(0,13):
    player1.append(0)
    player2.append(0)
    player3.append(0)
    player4.append(0)
for i in range(0,13):
    deck[i] = "S"+ strCardNames[i]
    deck[i+13] = "H"+ strCardNames[i]
    deck[i+26]= "D"+ strCardNames[i]
    deck[i+39]= "C"+ strCardNames[i]
for i in range(0,52):
    rand[i] = rd.choice(deck)
    deck.remove(rand[i])
for i in range (0,13):
    player1[i]=rand[i]
    player2[i]=rand[i+13]
    player3[i]=rand[i+26]
    player4[i]=rand[i+39]
