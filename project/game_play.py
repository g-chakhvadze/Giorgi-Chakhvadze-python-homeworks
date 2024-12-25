from setup_role1.setup import get_player_names, generate_deck, deal_cards, display_initial_cards
from game_logic_role2.game_logic import calculate_score, determine_winner, remove_loser

def replace_card(player, deck):
    print(f"{player['name']}, your cards: {', '.join(player['cards'])}")
    replace = input("Do you want to replace a card? (yes/no): ").strip().lower()

    if replace == 'yes':
        card_to_replace = input("Enter the card you want to replace: ").strip()
        if card_to_replace in player['cards']:
            player['cards'].remove(card_to_replace)
            new_card = deck.pop()  # Replace card from the deck
            player['cards'].append(new_card)
            print(f"{player['name']}, your new card is: {new_card}")
        else:
            print("Card not in hand. No replacement made.")
    else:
        print(f"{player['name']} did not replace any card.")
    return deck

def play_round(players, deck):
    # Allow players to replace cards
    for player in players:
        deck = replace_card(player, deck)  # Only modifies the deck if a card is replaced

    # Calculate scores after all players have finished
    scores = {player['name']: calculate_score(player['cards']) for player in players}
    print("Scores after this round:")
    for player in players:
        print(f"{player['name']} - {calculate_score(player['cards'])} points")

    winner = determine_winner(players)

    # If there is a winner, announce and eliminate the loser
    if isinstance(winner, list):
        print("It's a tie! Multiple winners.")
    else:
        print(f"The winner of this round is {winner['name']} with cards: {', '.join(winner['cards'])}")

    players = remove_loser(players)  # Eliminate the player with the lowest score after each round
    return players, deck

def display_updated_cards(players):
    print("\nUpdated Cards for Each Player:")
    for player in players:
        print(f"{player['name']}'s updated cards: {', '.join(player['cards'])}")

def announce_winner(players):
    if len(players) == 1:
        print(f"The final winner is {players[0]['name']}!")
    else:
        print("It's a tie!")

def deal_new_cards(players, deck):
    # Deal new cards to all players at the start of each round
    for player in players:
        new_hand = [deck.pop() for _ in range(5)]  # Deal 5 new cards to each player
        player['cards'] = new_hand
    return players, deck

def play_game():
    players = [{'name': name, 'cards': []} for name in get_player_names()]
    player_names = [player['name'] for player in players]  # Extract only names
    deck = generate_deck()
    players, deck = deal_new_cards(players, deck)  # Deal initial cards

    display_initial_cards({player['name']: player['cards'] for player in players})

    round_number = 1
    while len(players) > 1:
        print(f"\n--- Round {round_number} ---")
        players, deck = play_round(players, deck)
        players, deck = deal_new_cards(players, deck)  # Deal new cards at the start of each round
        if len(players) > 1:  # Only display updated cards if more than 1 player remains
            display_updated_cards(players)
        if len(players) == 1:
            print(f"{players[0]['name']} is the last remaining player!")
            break
        round_number += 1

    announce_winner(players)

