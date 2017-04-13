import random
import time

print("-----------------") #Introduction
print("-MAGE-VS-DUNGEON-")
print("-----------------")
print("")
time.sleep(2)
print("Acceptable commands (north,south,east,west,open,cast,run)")
print("")
time.sleep(2)
print("You awake. No memories of how you got to this place.")
print("You must find a way out")
print("")
time.sleep(2)

op = ""
area = 1
x = 6
y = 4
lvl = 1
exp = 0
hp = 20
dmg = 3
item = False
game = True
typ = True

def Locate(): #Locations
    global op
    global typ
    global x
    global y
    
    if (x == 6 and y == 4): #Locations
        if (typ == True):
            print("You are in a dimly lit room. The only light is coming from the faintly burning torch on the wall.")
            print("Even though your vision is impaired you can make out what seems to be a path to the north.")
    elif (x == 6 and y == 5):
        if (typ == True):
            print("You make your way down a long hallway. The hall has an unpleasant scent of sewage. With your faint vision")
            print("you can see the hall leads to your north and south.")
    elif (x == 6 and y == 6):
        if (typ == True):
            print("You come to a well lit room. Torchs line the wall alowing you to make out the ruins inscribed on the walls.")
            print("You have paths leading to the north, south, east, and west.")
    elif (x == 5 and y == 6):
        if (typ == True):
            print("You walk into a room with chains and shackles scattered on the floor. There are what seems to be tally marks on the walls.")
            print("The only way out of the room is to the east.")
    elif (x == 7 and y == 6):
        if (typ == True):
            print("As you enter the room you get chills as you hear the faint echos of what sounds like screaming. This place feels familiar.")
            print("A door sits to your west.")
    elif (x == 6 and y == 7):
        if (typ == True):
            print("This is a narrow hallway. You struggle to squeeze through it. You wander if you should continue.")
            print("North and south are your only options.")
    elif (x == 6 and y == 8):
        if (typ == True):
            print("The hallway seems to get narrower. As you walk through it you come to a corner.")
            print("You can go south or east.")
    elif (x == 7 and y == 8):
        if (typ == True):
            print("As you walk down the hallway you can see what seems to be bright light off to the east.")
            print("The hall leads to the east and the west.")
    else:
        if (op == "north"): #If location not found
            y = y - 1
            Choice()
        elif (op == "south"):
            y = y + 1
            Choice()
        elif (op == "east"):
            x = x - 1
            Choice()
        elif (op == "west"):
            x = x + 1
            Choice()

def Monster(): #Monster Encounter

    global hp
    global exp
    global dmg
    global lvl

    alive = True
    dlvl = random.randint(1,3) * lvl
    dhp = dlvl * 3
    ddmg = dlvl

    print("A level ", dlvl, " demon has appeared!")
    
    while alive == True:
        run = 0
        op = input(">>")

        if (op == "cast"):
            dhp = dhp - dmg
            print("You cast a spell on the demon dealing ", dmg, " damage.")
            time.sleep(1)
            print("The demon now has ", dhp, " health left.")
            time.sleep(1)
        elif (op == "run"):
            run = random.randint(1, 5)
            if run == 5:
                print("You got away safely.")
                break
            else:
                print("You tried to run but you couldnt get away.")
            
        else:
            continue

        if (dhp <= 0):
            alive = False
            exp = exp + dlvl * 2
            print ("You killed the Demon")
            time.sleep(1)
            print("You gained ", dlvl * 2, " experience.")
            time.sleep(1)
            break
            return

        hp = hp - ddmg
        print ("The demon hits you with it claws for ", ddmg, " damage" )
        time.sleep(1)
        print("You now have ", hp, " health left.")

        if (hp <= 0):
            Death()
            alive = False
        
def Death(): #Players death
    global game
    game = False
    print("You have died")
    time.sleep(1)
    print("game over")

def lvlUp(): #Player level up
    global hp
    global lvl
    global exp
    global dmg

    if (exp >= 10 and lvl == 1):
        lvl = 2
        hp = hp + 7
        dmg = dmg + 3
        print("You leveled up to level 2!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 20 and lvl == 2):
        lvl = 3
        hp = hp + 7
        dmg = dmg + 3
        print("You leveled up to level 3!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 35 and lvl == 3):
        lvl = 4
        hp = hp + 7
        dmg = dmg + 3
        print("You leveled up to level 4!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 50 and lvl == 4):
        lvl = 5
        hp = hp + 10
        dmg = dmg + 7
        print("You leveled up to level 5!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 75 and lvl == 5):
        lvl = 6
        hp = hp + 10
        dmg = dmg + 5
        print("You leveled up to level 6!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 115 and lvl == 6):
        lvl = 7
        hp = hp + 10
        dmg = dmg + 5
        print("You leveled up to level 7!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 150 and lvl == 7):
        lvl = 8
        hp = hp + 10
        dmg = dmg + 5
        print("You leveled up to level 8!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 200 and lvl == 8):
        lvl = 9
        hp = hp + 15
        dmg = dmg + 7
        print("You leveled up to level 8!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    elif (exp >= 300 and lvl == 9):
        lvl = 10
        hp = hp + 15
        dmg = dmg + 7
        print("You leveled up to level 10!")
        print("Health:", hp)
        print("Damage:", dmg)
        time.sleep(2)
    

def Choice(): #Scan players choice

    global x
    global y
    global op
    global hp
    global item
    global lvl
    
    while True:
        op = input (">>")

        if (op == "north"): #All movement choices
            y = y + 1
            Locate()
            return
        elif (op == "south"):
            y = y - 1
            Locate()
            return
        elif (op == "east"):
            x = x + 1
            Locate()
            return
        elif (op == "west"):
            x = x - 1
            Locate()
            return

        


        if (op == "open" and item == True and lvl == 1): #Other commands
            print("You open the chest")
            time.sleep(1)
            print("You obtain a potion of health")
            time.sleep(1)
            hp = hp + 5
            print("You gain 5 health. Your health now is, ", str(hp))
            item = False
        elif (op == "open" and item == True and lvl == 2):
            print("You open the chest")
            time.sleep(1)
            print("You obtain a potion of health")
            time.sleep(1)
            hp = hp + 10
            print("You gain 10 health. Your health now is, ", str(hp))
            item = False
        elif (op == "open" and item == True and lvl >= 3):
            print("You open the chest")
            time.sleep(1)
            print("You obtain a potion of health")
            time.sleep(1)
            hp = hp + 15
            print("You gain 15 health. Your health now is, ", str(hp))
            item = False
        else:
            continue

    
    return


def Chest(): #Treasure handling
    print("A chest has appeared")

while game == True: #Main game loop
    item = False
    print ("")
    lvlUp()

    encounter = random.randint (1,20) #Check for monster attack
    if (encounter >= 18):
        Monster()
        continue
    print("")
    

    print("")
    loot = random.randint (1,20) #Check for treasure
    if (loot <= 3):
        item = True
        Chest()
    typ = True
    Locate()
    typ = False

    Choice()
    
