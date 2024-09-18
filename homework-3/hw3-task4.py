import random
random_card_type = random.choice(("clubs (♣)", "diamonds (♦)", "hearts (♥)" , "spades (♠)"))
random_card_rank = random.choice(("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"))
print(random_card_rank,random_card_type)