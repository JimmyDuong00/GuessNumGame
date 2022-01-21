import random #This code uses the built in module for random numbers.

def main(): #This code defines the main() function and determines if the user wants to start or continue playing the game.
        display_title() #Calls the display_title function and displays the game title.
        begin_game = input("Type 'yes' to begin the game. Type 'no' to end the program. ")
        while begin_game == "yes": #If the user enters 'yes' it begins the game.
            play_game()
            #The code below asks the user if they want to continue playing. If they type 'no' then the program ends. If not, it will continue running the code. 
            continue_playing = input("Would you like to continue playing? Type 'yes' to continue or 'no' to end the program. ")
            if continue_playing == "no":
               return

def display_title(): #The function displays the title of the game.
    print("Guess the Number Game'n/'")
    print("This game makes you guess between 1 and 10.")

#The function function below runs the number guesser and user input to guess the number.
#If the number is correct, then the function breaks, if not, it will prompt the user to try again.

def play_game(): 
    target_num = random.randint(1,10) #Assigns a random number from 1-10 to target_num.

    user_input = None
    while user_input != target_num:
        user_input = int(input("Please enter a number between 1 and 10. "))

        if target_num < user_input:
            print("Sorry, guess again. The number you guessed was too high.")
        elif target_num > user_input:
            print("Guess again, the number you guessed was too low.")
    print("You guessed the number correctly!")
    return

main()
