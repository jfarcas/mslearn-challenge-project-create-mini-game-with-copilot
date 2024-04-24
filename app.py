import random
import json


def ask_to_continue():
    while True:
        user_input = input("\nDo you want to 🎮 Continue the game or 🚀 Start a new one?\nPress 'C' for Continue 🔄 or 'N' for New Game 🆕\n").lower()
        if user_input in ['c', 'n']:
            return 'continue' if user_input == 'c' else 'new'
        else:
            print("Invalid input. Please enter 'C' for Continue or 'N' for New Game.")


def check_previous_game():
    try:
        with open('game_results.txt', 'r') as file:
            score = json.loads(file.read().strip())
            return score if score else False
    except FileNotFoundError:
        return False


def save_results(result, score):
    score[result] += 1
    with open('game_results.txt', 'w') as file:
        file.write(json.dumps(score))
    print("\nScore:")
    print(f"Wins: {score['You win! 🎉']}")
    print(f"Losses: {score['You lose! 😞']}")
    draw_key = 'It\'s a draw! 😐'
    print(f"Draws: {score[draw_key]}")


def play_game():
    score = check_previous_game()
    if score:
        print("\nPrevious Score:")
        print(f"Wins: {score['You win! 🎉']}")
        print(f"Losses: {score['You lose! 😞']}")
        draw_key = 'It\'s a draw! 😐'
        print(f"Draws: {score[draw_key]}")
    if not score or ask_to_continue() == 'new':
        score = {'You win! 🎉': 0, 'You lose! 😞': 0, 'It\'s a draw! 😐': 0}
    allowed_options = ['rock', 'paper', 'scissors']
    allowed_inputs = allowed_options + [option[0] for option in allowed_options]
    input_to_option = {option[0]: option for option in allowed_options}
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    while True:
        print("\n" + "-" * 50)  # print separator
        user_input = input(
            "Enter one of the following options: \nrock (r) 🪨, paper (p) 📄, scissors (s) ✂️ \nor type 'exit' or 'E' to quit\n").lower()
        if user_input in ['exit', 'e']:
            break
        elif user_input not in allowed_inputs:
            print("Invalid input. Please enter one of the allowed options.")
        else:
            if len(user_input) == 1:
                user_input = input_to_option[user_input]
            app_choice = random.choice(allowed_options)
            print(f"\nYou chose {user_input}, I chose {app_choice}")
            if user_input == app_choice:
                result = "It's a draw! 😐"
                print(result)
            elif beats[user_input] == app_choice:
                result = "You win! 🎉"
                print(result)
            else:
                result = "You lose! 😞"
                print(result)
            save_results(result, score)

def main():
    print("Welcome to Rock-paper-scissors!")


if __name__ == "__main__":
    main()
    play_game()
