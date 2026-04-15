import random

# Define suits and ranks
suits = ['Hearts ♥', 'Diamonds ♦', 'Clubs ♣', 'Spades ♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create the deck
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Print original deck
print("\n🃏 Welcome to the Python Card Shuffler! 🃏")
print("Here's the original ordered deck:\n")

for i, card in enumerate(deck, 1):
    print(f"{card:20}", end='  ')
    if i % 4 == 0:
        print()  # New line after every 4 cards

# Shuffle the deck
random.shuffle(deck)

# Print shuffled deck
print("\n🔀 Deck has been shuffled! Here's the new order:\n")

for i, card in enumerate(deck, 1):
    print(f"{card:20}", end='  ')
    if i % 4 == 0:
        print()
