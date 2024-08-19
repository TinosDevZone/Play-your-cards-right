import random

print("Welcome to the Play your cards right game!")
def play_your_cards_right():
    ranks = list(range(1, 14)) 
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


    deck = [(rank, suit) for rank in ranks for suit in suits]


    random.shuffle(deck)
    player_hand = deck[:5]

    current_card = deck.pop()
    score = 0
    game_active = True

    while game_active and deck:

        guess = input("Will the next card be higher or lower? (h/l): ").lower()


        next_card = deck.pop()
        print(f"Next card is: {next_card[0]} of {next_card[1]}")


        if (guess == 'h' and next_card[0] > current_card[0]) or (guess == 'l' and next_card[0] < current_card[0]):
            score += 1
            print("Correct! Your score is now", score)
            current_card = next_card
        else:
            print("Wrong guess! Game over.")
            game_active = False


        if game_active and not deck:
            if input("Continue playing? (y/n): ").lower() == 'n':
                game_active = False
                print("Your final score was:", score)

    high_score = 0

    if score > high_score:
            high_score = score
    print(f"New high score: (score)") 

play_your_cards_right()



import random

# Welcome message
print("Welcome to the Play Your Cards Right Game!")
print("Can you predict if the next card will be higher or lower?")
print("Let's find out!")

# Define the card ranks and suits
ranks = ['Ace'] + list(map(str, range(2, 11))) + ['Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Initialize variables
current_card = deck.pop()
score = 0
high_score = 0
game_active = True

# Function to print the card in a more readable format
def print_card(card):
    rank, suit = card
    print(f"{rank} of {suit}")

# Game loop
while game_active and deck:
    # Show the current card
    print("Current card:")
    print_card(current_card)

    # Get the player's guess
    guess = input("Will the next card be higher or lower? (h/l): ").lower()

    # Draw the next card
    next_card = deck.pop()
    print("Next card:")
    print_card(next_card)

    # Check the player's guess
    if (guess == 'h' and ranks.index(next_card[0]) > ranks.index(current_card[0])) or \
       (guess == 'l' and ranks.index(next_card[0]) < ranks.index(current_card[0])):
        score += 1
        print("Correct! Your score is now", score)
        current_card = next_card
    else:
        print("Wrong guess! Game over.")
        game_active = False

    # Check if the player wants to continue
    if game_active and not deck:
        print("No more cards in the deck!")
        if input("Would you like to shuffle the deck and continue? (y/n): ").lower() == 'n':
            game_active = False

# Set and print the high score
if score > high_score:
    high_score = score
print(f"Your final score was: {score}")
print(f"The high score is: {high_score}")

# Ask if the player wants to play again
if input("Would you like to play again? (y/n): ").lower() == 'y':
    play_your_cards_right()

def play_your_cards_right():
    # The game code goes here, as before
    pass

# Start the game
play_your_cards_right()