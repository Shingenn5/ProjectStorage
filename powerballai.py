import random

# --- Function to generate the winning numbers ---
def generate_winning_numbers():
    """Generates a random set of winning Powerball numbers."""
    white_balls = sorted(random.sample(range(1, 70), 5))
    powerball = random.randint(1, 26)
    return white_balls, powerball

# --- Function to get the user's ticket numbers ---
def get_user_ticket():
    """Prompts the user to enter their Powerball numbers."""
    print("Welcome to Python Powerball!")
    print("Please enter your 5 white ball numbers (1-69), separated by spaces.")
    
    while True:
        try:
            user_input = input("Your numbers: ")
            user_balls = [int(num) for num in user_input.split()]
            
            # --- Input validation ---
            if len(user_balls) != 5:
                print("Please enter exactly 5 numbers.")
                continue
            if not all(1 <= num <= 69 for num in user_balls):
                print("All numbers must be between 1 and 69.")
                continue
            if len(user_balls) != len(set(user_balls)):
                print("All numbers must be unique.")
                continue
            
            user_balls.sort()
            break
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

    while True:
        try:
            user_powerball = int(input("Now, enter your Powerball number (1-26): "))
            if not 1 <= user_powerball <= 26:
                print("The Powerball number must be between 1 and 26.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    return user_balls, user_powerball

# --- Function to check the ticket and determine the prize ---
def check_ticket(user_white_balls, user_powerball, winning_white_balls, winning_powerball):
    """Compares the user's ticket to the winning numbers and determines the prize."""
    matches_white = len(set(user_white_balls) & set(winning_white_balls))
    matches_powerball = (user_powerball == winning_powerball)
    
    prizes = {
        (5, True): "Grand Prize! $1 Billion! 🤑",
        (5, False): "$1 Million 💰",
        (4, True): "$50,000 💵",
        (4, False): "$100 💸",
        (3, True): "$100 💸",
        (3, False): "$7 🪙",
        (2, True): "$7 🪙",
        (1, True): "$4 🪙",
        (0, True): "$4 🪙"
    }

    if (matches_white, matches_powerball) in prizes:
        return prizes[(matches_white, matches_powerball)]
    else:
        return "Sorry, no prize this time. 😔"

# --- Main game loop ---
def main():
    """Runs the main Powerball game."""
    winning_white_balls, winning_powerball = generate_winning_numbers()
    user_white_balls, user_powerball = get_user_ticket()
    
    print("\nDrawing the numbers...")
    print(f"Winning white balls: {winning_white_balls}")
    print(f"Winning Powerball: {winning_powerball}")
    print(f"Your ticket: {user_white_balls}, Powerball: {user_powerball}")

    result = check_ticket(user_white_balls, user_powerball, winning_white_balls, winning_powerball)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
    