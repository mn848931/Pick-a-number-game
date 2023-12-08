import random

def play_game():
    balance = 10.0
    entrance_fee = 0.10
    consecutive_failures = 0

    play_game_response = input("Do you want to play the game? (yes/no): ").lower()

    while play_game_response not in ['yes', 'no']:
        print("Please type only 'yes' or 'no'.")
        play_game_response = input("Do you want to play the game? (yes/no): ").lower()

    if play_game_response == 'no':
        print("Game over!")
        return

    while balance >= entrance_fee:
        print(f"\nCurrent balance: ${balance:.2f}")

        range_choice = int(input("Choose the range of numbers (10, 20, 30, ..., 100): "))
        betting_fee = 0.5 + (range_choice - 20) // 10 * 0.25  # Adjust betting fee based on the chosen range
        max_number = range_choice
        reward = 0.25 + (range_choice - 10) // 10 * 0.25  # Adjust reward based on the chosen range

        target_number = random.randint(1, max_number)

        # Deduct entrance fee for each game
        balance -= entrance_fee

        # Deduct betting fee for each game
        balance -= betting_fee

        guess = int(input(f"Guess a number between 1 and {max_number}: "))

        if guess == target_number:
            balance += reward
            print(f"Congratulations! You guessed it right. You earned ${reward:.2f}.")
            consecutive_failures = 0  # Reset consecutive failures counter
        else:
            print(f"Wrong guess! You lost ${betting_fee:.2f}. The correct number was {target_number}.")
            consecutive_failures += 1

            # If there are 3 consecutive failures, set a 90% chance of winning in the next round
            if consecutive_failures == 3:
                if input("Do you want to play again? (yes/no): ").lower() == 'yes':
                    # 90% chance of winning if playing again after 3 consecutive failures
                    if random.random() < 0.9:
                        balance += reward
                        consecutive_failures = 0  # Reset consecutive failures counter
                else:
                    break

        play_again_response = input("Do you want to play again? (yes/no): ").lower()
        while play_again_response not in ['yes', 'no']:
            print("Please type only 'yes' or 'no'.")

        if play_again_response == 'no':
            break

    print("\nGame over!")
    print(f"Final balance: ${balance:.2f}")

if __name__ == "__main__":
    play_game()