from sys import exit
from random import randint

# Identify the numeber of players required through prompt and store the same as integer
# Create a list pl for storing the player classes and a list nl for storing the player names
print "Enter number of players: "
pn = int(raw_input())
pl = []
nl= []

# Define a class player to have name and begining score of 0
class player(object):
    def __init__(self, name):
        self.name=name
        self.score = 0

# Create players basis the number of players from line 7
for i in range(1, pn+1):
    plr = 'Player'
    #print plrx
    plr = player(plr+str(i))
    pl.append(player(plr))
    #print plr.name
    nl.append(plr.name)
    #print plr.score

#print pl

# Create a dictionary of ladders ll and snakes sl
ll = {2:38,4:14,9:31,21:42,28:84,51:67,72:91,80:98}
sl = {17:7, 54:34, 63:19, 64:60, 87:36, 93:73, 95:75, 97:79}


def roll():
    i=0
    while i < pn:
    #for i in range(0, pn):
        print "%s please roll the dice." %nl[i]
        raw_input('> ')
        ro1 = randint(1,6)
        ro2 = randint(1,6)
        print "Dice1 : %i & Dice2 : %i" %(ro1, ro2)
        ro = ro1 + ro2
        pl[i].score += ro
        if pl[i].score <= 100:
            print "Now %s is in %i." %(nl[i], pl[i].score)
            if pl[i].score == 100:
                print "Congratulations %s!!!, You are the winner." % nl[i]
                exit(1)
            for j in ll:
                if pl[i].score == j:
                    pl[i].score = ll[j]
                    print "Wow! A ladder %s you are up in %i" % (nl[i], pl[i].score)
            for k in sl:
                if pl[i].score == k:
                    pl[i].score = sl[k]
                    print "Shuks! A snake %s you are down in %i" % (nl[i], pl[i].score)
            if ro1 == ro2:
                print "DOUBLES!!!! %s Roll again" %nl[i]
                i -= 1
        else:
            pl[i].score -= ro
            print "Oh.. %s you lose your turn cause you need %i to make it to 100 from %i." %(nl[i], 100-pl[i].score, pl[i].score)
        i += 1

while 1 == 1:
    roll()
