import random

def player_selection():
    """
    Prompts the player to pick a number between 1 and 3. Compares the player's choice with
    a randomly generated number from the computer and displays the result. Allows the player
    to play again or quit.
    """
    while True:
        # Get player's choice
        player_choice = input("Here we go! Pick a number between 1 and 3 (or type 'q' to quit): ")
        
        # Handle quit case
        if player_choice.lower() == 'q':
            print("I guess you changed your mind. Maybe next time!")
            break
        
        if player_choice:
            try:
                # Convert player's choice to an integer
                player_one = int(player_choice)
                
                # Check if the player's choice is valid
                if 1 <= player_one <= 3:
                    # Generate a random number for the computer
                    computer_choice = random.randint(1, 3)
                    
                    # Determine the result of the game
                    result = f"PlayerOne: {player_one}\nComputer: {computer_choice}\n\n"
                    if player_one == computer_choice:
                        result += "Tie Game!"
                    else:
                        result += "Computer Wins!"
                    
                    print(result)
                    
                    # Ask if the player wants to play again
                    play_again = input("Play Again? (yes/no): ").lower()
                    if play_again == 'yes':
                        # Restart the game
                        player_selection()
                    else:
                        print("Thanks for playing. Goodbye!")
                    break
                
                else:
                    print("You did not enter a valid number. Select a number between 1 and 3!")
            
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3 or 'q' to quit.")
        
        else:
            print("I guess you changed your mind. Maybe next time!")
            break

def main():
    """
    Main function to start the game. Asks the user if they want to play the game and
    initiates the game or exits based on the user's response.
    """
    play_game = input("Shall we play a random number guess game? (yes/no): ").lower()
    if play_game == 'yes':
        player_selection()
    else:
        print("Alright. Maybe next time!")

#restricts module from running automatically when imported
if __name__ == "__main__":
    main()