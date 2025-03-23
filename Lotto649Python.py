import random

# Generate 6 unique winning numbers between 1 and 49
winning_numbers = set(random.sample(range(1, 50), 6))

# Print the winning numbers
print("Winning Numbers:")
for i, num in enumerate(winning_numbers, start=1):
    print(f"Pick {i}: {num}")

# Generate 6 unique player numbers between 1 and 49
player_numbers = set(random.sample(range(1, 50), 6))
# Keep track of how many attepmts the player needs win the jackpot
attempt = 1
# Loop the ticket generation for player until player ticket number match winning numbers
while player_numbers != winning_numbers:
    # Generate 6 unique player numbers between 1 and 49
    player_numbers = set(random.sample(range(1, 50), 6))
    attempt += 1

# Player has finally won!
print("\nPlayer has won jackpot!")

# Print the player's numbers
print("\nPlayer's Numbers:")
for i, num in enumerate(player_numbers, start=1):
    print(f"Pick {i}: {num}")

# Print the number of attempts taken to win the jackpot
print("\nTotal number of Attempts: ", attempt)