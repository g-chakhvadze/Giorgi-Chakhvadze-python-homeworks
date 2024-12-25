def calculate_score(cards):
    # Mapping the face cards to their values
    value_map = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 20}
    score = 0

    # Iterate over each card in the player's hand
    for card in cards:
        card_value = card.split()[0]  # Extract the value part of the card (e.g., 'Jack', '10', 'King')

        # Check if the card is a face card or Ace
        if card_value in value_map:
            score += value_map[card_value]
        else:
            # If it's not a face card, it should be a numeric value
            try:
                score += int(card_value)  # Add the numeric value of the card to the score
            except ValueError:
                # If the card value is not numeric or face card, we skip it (shouldn't happen)
                continue

    return score


def determine_winner(players):
    # Calculate scores for each player
    scores = {player['name']: calculate_score(player['cards']) for player in players}

    # Find the player with the maximum score
    highest_score = max(scores.values())

    # Get the player(s) with the highest score (handling tie situation)
    winner_players = [player for player in players if calculate_score(player['cards']) == highest_score]

    if len(winner_players) == 1:
        return winner_players[0]  # Single winner
    else:
        return winner_players  # Multiple players in case of tie


def remove_loser(players):
    # Eliminate the player with the lowest score
    scores = {player['name']: calculate_score(player['cards']) for player in players}
    loser_name = min(scores, key=scores.get)
    loser = next(player for player in players if player['name'] == loser_name)
    players = [player for player in players if player['name'] != loser_name]
    print(f"Player {loser['name']} has been eliminated.")
    return players

