import random

high_score = 0


def dice_game():
    global high_score
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print("You roll a:", roll1)
        print("You roll a:", roll2)
        
        total_roll = roll1 + roll2

        print("You have rolled a total of:", total_roll)


        if total_roll > high_score:
            print("New high score!")
            high_score = total_roll
            
        print("Current High_score", high_score)
        return dice_game()

    elif choice == "2":
        print("Goodbye!")
        return
                
    else:
        print("Invalid choice, choose 1 or 2")
        return dice_game()

dice_game()
