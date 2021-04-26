#Treasure Island Game
print("Welcome to the Treasure Island.")
print("Your mission is to find the Treasure.")
a = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
    
if a == "left":
    b = input("You\'ve come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower() 
    if b == "wait":
        c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if c == "red":
            print("It\'s a room full of fire. Game over.")
        elif c == "yellow":
            print("You\'ve find the Treasure. You win.")
        elif c == "blue":
            print("You enter a room of beasts. Game over.")    
        else:
            print("You choose a door that doesn\'t exist. tGame over.")        
    else:
        print("You got attacked by a angry trout. Game over.") 
else:
    print("You fell into a hole. Game over.") 

       

    