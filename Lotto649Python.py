import random

# Generate 6 unique winning numbers between 1 and 49
winning_numbers = random.sample(range(1, 50), 6)

# Generate 6 unique player numbers between 1 and 49
player_numbers = random.sample(range(1, 50), 6)

# Print the winning numbers
print("Winning Numbers:")
for i, num in enumerate(winning_numbers, start=1):
    print(f"Pick {i}: {num}")

# Print the player's numbers
print("\nPlayer's Numbers:")
for i, num in enumerate(player_numbers, start=1):
    print(f"Pick {i}: {num}")