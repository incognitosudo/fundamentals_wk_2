import random

pips = random.randint(1, 6)  #range of 1 to 6
print("Dice rolls: ", pips)


prizes = ["company", "mansion", "lamborghini"]

prize_won = random.choice(prizes)

print("You won", prize_won)


cards = [1,2,3,4,5,6,7,8,9]
random.shuffle(cards)
print("You reshuffle cards to:", cards)
