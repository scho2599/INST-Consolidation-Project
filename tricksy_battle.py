#Consolidation Project Shua Cho

import random

#Here we define cards and the values as well
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
VALUES = list(range(1, 13))  # 1 to 12 (Ace to queen, King is removed)

#We are building and shuffling the deck 
deck = [(suit, value) for suit in SUITS for value in VALUES]
random.shuffle(deck)

#Dealing 8 cards to each players hand 
player1_hand = [deck.pop() for _ in range(8)]
player2_hand = [deck.pop() for _ in range(8)]

player1_points = 0
player2_points = 0

#This will cause the starting turn to be chosen at random
player_turn = random.choice([1, 2])

round_number = 1
reshuffle_count = 0

#We are able to convert the card value into a readable string 
def card_str(card):
    value_names = {1: "Ace", 11: "Jack", 12: "Queen"}
    return f"{value_names.get(card[1], str(card[1]))} of {card[0]}"

#Comparing cards of the players to see who wins 
def determine_round_winner(card1, card2, lead_suit):
    if card1[0] == card2[0]:
        return 1 if card1[1] > card2[1] else 2
    elif card1[0] == lead_suit:
        return 1
    elif card2[0] == lead_suit:
        return 2
    else:
        return 1  #If none of past conditions are met

#Here is the body of the main game loop
while round_number <= 16 and player1_points < 9 and player2_points < 9:
    print(f"\nRound {round_number}")
    print("Player 1:", [card_str(c) for c in player1_hand])
    print("Player 2:", [card_str(c) for c in player2_hand])

    #Chosing cards based on tirn
    if player_turn == 1:
        lead_card = player1_hand.pop(0)
        follow_card = None
        for card in player2_hand:
            if card[0] == lead_card[0]:
                follow_card = card
                break
        if follow_card:
            player2_hand.remove(follow_card)
        else:
            follow_card = player2_hand.pop(0)
    else:
        lead_card = player2_hand.pop(0)
        follow_card = None
        for card in player1_hand:
            if card[0] == lead_card[0]:
                follow_card = card
                break
        if follow_card:
            player1_hand.remove(follow_card)
        else:
            follow_card = player1_hand.pop(0)

    print(f"Player {player_turn} plays: {card_str(lead_card)}")
    print(f"Player {3 - player_turn} plays: {card_str(follow_card)}")

    #This is determing the winner however note to self that there is a bug in this portrion causing wrong round outcomes MAKE SURE TO INCLUDE THIS IN README
    if player_turn == 1:
        winner = determine_round_winner(lead_card, follow_card, follow_card[0])  
    else:
        winner = determine_round_winner(follow_card, lead_card, follow_card[0])  

    if winner == 1:
        player1_points += 1
        player_turn = 1
        print("Player 1 wins the round!")
    else:
        player2_points += 1
        player_turn = 2
        print("Player 2 wins the round!")

    #The public card which isnt used but just shown
    if deck:
        public_card = deck.pop()
        print("Public card shown:", card_str(public_card))

    #Redeal 4 cards each to palayer if needed
    if len(player1_hand) == 4 and len(player2_hand) == 4 and reshuffle_count < 2:
        for _ in range(4):
            if deck: player1_hand.append(deck.pop())
            if deck: player2_hand.append(deck.pop())
        reshuffle_count += 1

    round_number += 1

#Ending functions for the game
print("\nGame Over!!!")
print("Player 1 points:", player1_points)
print("Player 2 points:", player2_points)

if player1_points == 16:
    print("Player 1 shoots the moon!")
elif player2_points == 16:
    print("Player 2 shoots the moon!")
elif player1_points >= 9:
    print("Player 1 wins!")
elif player2_points >= 9:
    print("Player 2 wins!")
else:
    print("No winner yet.")
