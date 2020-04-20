import random

# Class: alle lapjes krijgen een vorm, een draaimogelijkheid, knoopjeskost, tijdkost en knoopjesopbrengst, één lapje wordt het startlapje.
class Lapje():
    def __init__(self, vorm, kkost, tkost, kopbrengst = 0, start_fiche = False):
        self.vorm = vorm
        self.kkost = kkost
        self.tkost = tkost
        self.kopbrengst = kopbrengst
        self.start_fiche = start_fiche
    def draai(self):
        pass


# het lapjesveld wordt gemaakt
lapje1 = Lapje([[1,1,1,1], [1,0,0,0]], 3, 10, 2)
lapje2 = Lapje([[1,1,1,1], [0,1,1,0]], 4, 7, 2)
lapje3 = Lapje([[0,1,1], [1,1,0]], 6, 7, 3)
lapje4 = Lapje([[0,0,1,0,0], [1,1,1,1,1], [0,0,1,0,0]], 4, 1, 1)
lapje5 = Lapje([[0,1,1,0], [1,1,1,1], [0,1,1,0]], 3, 5, 1)
lapje6 = Lapje([[1,1,1], [0,0,1]], 6, 4, 2)
lapje7 = Lapje([[1,1], [1,1]], 5, 6, 2)
lapje8 = Lapje([[1,1,1], [0,0,1]], 2, 4, 1)
lapje9 = Lapje([[1,1,1, 0], [0, 0, 1,1]], 3,2,1)
lapje10 = Lapje([[1,1], [1,0]], 3, 1)
lapje11 = Lapje([[1,1,1,1], [1,0,0,1]], 5,1,1)
lapje12 = Lapje([[1,1,1], [1,0,1]], 2,1)
lapje13 = Lapje([[1,1,1,1], [0,0,1,0]], 4, 3, 1)
lapje14 = Lapje([[1,1,1,1], [1,1,0,0]], 5,10,3)
lapje15 = Lapje([[1,1,1,0], [0,1,1,1]], 2,4)
lapje16 = Lapje([[1,1], [1,0]], 1,3)
lapje17 = Lapje([[1,1,1], [0,1,0]],2,2)
lapje18 = Lapje([[1,1,0], [0,1,1]], 2,3,1)
lapje19 = Lapje([[1,1]], 1, 2,0,True)
lapje20 = Lapje([[1, 1, 1]], 2, 2)
lapje21 = Lapje([[1,1,1,1]],3,3,1 )
lapje22 = Lapje([[1,1,1,1,1]],1,7,1)
lapje23 = Lapje([[1,1,0], [1,1,1], [0,0,1]], 6,8,3)
lapje24 = Lapje([[0,0,1,0], [1,1,1,1], [0,0,1,0]],3,0,1)
lapje25 = Lapje([[1,0,0,0], [1,1,1,1], [1,0,0,0]],2,7,2 )
lapje26 = Lapje([[0,0,1,0], [1,1,1,1], [0,1,0,0]],1,2 )
lapje27 = Lapje([[1,1,1], [0,1,0], [0,1,0]],5,5,2 )
lapje28 = Lapje([[1,1,1], [0,1,0], [1,1,1]],3,2 )
lapje29 = Lapje([[1,1,0], [0,1,1], [0,0,1]],4,10,3 )
lapje30 = Lapje([[0,1,0], [1,1,1], [0,1,0]],4,5,2 )
lapje31 = Lapje([[0,1,0], [1,1,1], [1,0,1]],6,3,2 )
lapje32 = Lapje([[0,0,0,1], [1,1,1,1], [1,0,0,0]],2,1 )

# de lapjes komen in een list en deze wordt geschud.
list_van_lapjes = [lapje1, lapje10,lapje11,lapje12,lapje13,lapje14,lapje15,lapje16,lapje17,lapje18,lapje2,lapje20,lapje21,lapje23,lapje22,lapje24,lapje25,lapje26,
                   lapje27,lapje28,lapje29,lapje3,lapje30,lapje31,lapje32,lapje4,lapje5,lapje6,lapje7,lapje8,lapje9]
random.shuffle(list_van_lapjes)
list_van_lapjes.append(lapje19)
print(list_van_lapjes)
print(list_van_lapjes[0].vorm)

# het speelveld wordt gemaakt met een lengte, een plek voor de spelers en grenswaarden voor wanneer de spelers er knoopjes bij krijgen.


# Class: de spelers worden gemaakt met hun plek op het speelveld, hun knoopjes en hun lapjesveld

# het spel begint totdat beide spelers het einde van het speelveld bereikt hebben.
    # 1. het speelbord, 2. de beide spelers, 3. de beschikbare lapjes en 4. het lapjesveld van de speler die aan de beurt is worden weergegeven.


    # een speler kiest een lapje, draait deze eventueel en plaatst deze op het speelveld.
    # de speler wordt verplaatst op het speelveld en het aantal knoopjes


    # Als de ene speler de ander voorbij is, is de ander aan de beurt.

# beide spelers hebben het einde van het speelveld bereikt. van hun aantal knoopjes worden 2 knoopjes per leeg veld op hun bord afgehaald.

# de speler met de meeste knoopjes wint.



