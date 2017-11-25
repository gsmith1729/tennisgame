import random
# simulates a game in tennis where a player has the probability of winning
# a point p
p=0.4
hwins=0
awins=0
# games to simulate
games=1000000
for i in range(0,games):
    hscore=0
    ascore=0
    while (hscore<4 and ascore<4):
        # deuce
        if (hscore==3 and ascore==3):
            hscore=2
            ascore=2
        if (random.random()<p):
            hscore+=1
        else:
            ascore+=1
    if hscore==4:
        hwins+=1
    else:
        awins+=1

x=hwins/(hwins+awins)
print(x)
