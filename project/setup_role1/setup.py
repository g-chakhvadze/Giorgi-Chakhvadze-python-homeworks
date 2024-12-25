import random

def get_player_names():
    players = []
    print("Enter the names of three players: ")
    for i in range(3):
        name = input(f"Player {i + 1} Name: ").strip()
        players.append(name)  # Just append the name as a string
    return players

def generate_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def deal_cards(deck, players):
    player_hands = {player: [] for player in players}  # Initialize player hands using player names
    for _ in range(5):  # Deal 5 cards to each player
        for player in players:
            card = deck.pop(0)  # Take the top card
            player_hands[player].append(card)  # Add the card to the player's hand
    return player_hands

def display_initial_cards(player_hands):
    print("\nInitial Cards for Each Player: ")
    for player, cards in player_hands.items():
        print(f"{player}: {', '.join(cards)}")
