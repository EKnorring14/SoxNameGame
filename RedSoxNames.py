import random
import time

def get_red_sox_players():
    
    red_sox_players = [
        ("Connor Wong", ["Catcher"]),
        ("Caleb Hamilton", ["Catcher"]),
        ("Jorge Alfaro", ["Catcher"]),
        ("Reese McGuire", ["Catcher"]),
        ("Triston Casas", ["First Base"]),
        ("Bobby Dalbec", ["First Base", "Shortstop"]),
        ("Christian Arroyo", ["Second Base", "Shortstop"]),
        ("David Hamilton", ["Second Base"]),
        ("Luis Urias", ["Second Base"]),
        ("Enmanuel Valdez", ["Second Base"]),
        ("Rafael Devers", ["Third Base"]),
        ("Trevor Story", ["Shortstop"]),
        ("Kike Hernandez", ["Second Base", "Center Field", "Shortstop"]),
        ("Pablo Reyes", ["Second Base", "Shortstop"]),
        ("Yu Chang", ["Second Base", "Third Base", "Shortstop"]),
        ("Masataka Yoshida", ["Left Field", "Designated Hitter"]),
        ("Rob Refsnyder", ["Utility Outfield"]),
        ("Ramiel Tapia", ["Utility Outfield"]),
        ("Ceddanne Rafaela", ["Center Field"]),
        ("Jarren Duran", ["Center Field"]),
        ("Adam Duvall", ["Center Field"]),
        ("Alex Verdugo", ["Right Field"]),
        ("Wilyer Abreu", ["Right Field"]),
        ("Justin Turner", ["First Base", "Third Base", "Designated Hitter"]),
        ("Tanner Houck", ["Starting Pitcher"]),
        ("Matt Dermody", ["Starting Pitcher"]),
        ("Chris Sale", ["Starting Pitcher"]),
        ("James Paxton", ["Starting Pitcher"]),
        ("Brayan Bello", ["Starting Pitcher"]),
        ("Garrett Whitlock", ["Starting Pitcher", "Relief Pitcher"]),
        ("Kutter Crawford", ["Starting Pitcher", "Relief Pitcher"]),
        ("Corey Kluber", ["Starting Pitcher", "Relief Pitcher"]),
        ("Nick Pivetta", ["Starting Pitcher", "Relief Pitcher"]),
        ("Ryan Sherriff", ["Relief Pitcher"]),
        ("Ryan Brasier", ["Relief Pitcher"]),
        ("Nick Robertson", ["Relief Pitcher"]),
        ("Brandon Walter", ["Relief Pitcher"]),
        ("Joe Jacques", ["Relief Pitcher"]),
        ("Zack Weiss", ["Relief Pitcher"]),
        ("Taylor Scott", ["Relief Pitcher"]),
        ("Jake Faria", ["Relief Pitcher"]),
        ("John Schreiber", ["Relief Pitcher"]),
        ("Mauricio Llovera", ["Relief Pitcher"]),
        ("Justin Garza", ["Relief Pitcher"]),
        ("Kyle Barraclough", ["Relief Pitcher"]),
        ("Chris Murphy", ["Relief Pitcher"]),
        ("Joely Rodriguez", ["Relief Pitcher"]),
        ("Richard Bleier", ["Relief Pitcher"]),
        ("Josh Wincowski", ["Relief Pitcher"]),
        ("Kenley Jansen", ["Relief Pitcher"]),
        ("Chris Martin", ["Relief Pitcher"]),
        ("Kaleb Ort", ["Relief Pitcher"]),
        ("Zack Littell", ["Relief Pitcher"]),
        ("Zack Kelley", ["Relief Pitcher"]),
        ("Brennan Bernardino", ["Relief Pitcher"]),
       
    ]
    return red_sox_players

def play_game():
    red_sox_players = get_red_sox_players()
    random.shuffle(red_sox_players)

    correct_guesses = 0
    total_players = len(red_sox_players)
    score = 0
    start_time = time.time()

    print("Welcome to the 2023 Red Sox Player Naming Game!")
    print("Try to name every player on the team.")
    print("Enter 'exit' at any time to end the game.\n")

    for i in range(total_players):
        current_player, possible_positions = red_sox_players[i]

        user_guess = input(f"Who is one of the players at {', '.join(possible_positions)}? ").strip()

        correct_names = [name for name, positions in red_sox_players if set(possible_positions).intersection(positions)]
        
        if user_guess.lower() == current_player.lower() or user_guess.lower() in [name.lower() for name in correct_names if user_guess.lower() != current_player.lower()]:
            print("Correct!")
            correct_guesses += 1
            score += 10
        elif user_guess.lower() == 'exit':
            break
        else:
            print(f"Wrong! The correct answer(s) is/are {', '.join(correct_names)}.\n")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nGame Over!")
    print(f"You named {correct_guesses} out of {total_players} players.")
    print(f"Your score is {score}.")
    print(f"Elapsed time: {elapsed_time:.2f} seconds.\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()