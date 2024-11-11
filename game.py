import random

def start_adventure():
    print("Welcome to the Cave Adventure!")
    print("You are in a dark cave, searching for treasure.")
    print("There are two paths in front of you. Which one will you choose?")
    choose_path()

def choose_path():
    print("\nChoose your path:")
    print("1. The left path")
    print("2. The right path")
    
    choice = input("Enter the path number (1 or 2): ")
    
    if choice == "1":
        monster_room()
    elif choice == "2":
        treasure_room()
    else:
        print("Please enter a valid option.")
        choose_path()

def monster_room():
    print("\nYou have entered a room with a giant monster!")
    print("The monster is asleep, and you have two options:")
    print("1. Try to sneak out without waking up the monster.")
    print("2. Attack the monster.")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        if random.choice([True, False]):
            print("\nYou successfully snuck out of the room!")
            treasure_room()
        else:
            print("\nThe monster woke up and ate you! You lost.")
            play_again()
    elif choice == "2":
        print("\nYou tried to attack the monster, but it was stronger than you and ate you! You lost.")
        play_again()
    else:
        print("Please enter a valid option.")
        monster_room()

def treasure_room():
    print("\nYou are now in the treasure room!")
    print("You see a large chest filled with gold and jewels.")
    print("Congratulations! You found the treasure!")
    play_again()

def play_again():
    choice = input("\nWould you like to play again? (yes/no): ")
    if choice.lower() == "yes":
        start_adventure()
    elif choice.lower() == "no":
        print("Thank you for playing! See you next time.")
    else:
        print("Please enter a valid option.")
        play_again()

# Start the game
start_adventure()
