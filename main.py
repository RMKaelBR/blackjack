############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import art
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hands = {"computer" : [], "player" : []}

def reset():
    hands["computer"].clear()
    hands["player"].clear()
    
def deal_card(player):
    # cards_in_hand = hands[player]
    # cards_in_hand.append(random.choice(cards))
    # hands [player] = cards_in_hand
    hands[player].append(random.choice(cards))
    
def show_cards():
    clear()
    print (art.logo)
    total_score = 0
    for num in hands["player"]:
        total_score += num
    
    print (f'Player\'s hand: {hands["player"]} Total Score: {total_score}')
    print (f'Computer\'s hand: {hands["computer"]}')

def hand_score(player):
    score = 0
    for card in hands[player]:
        score += card
    return score

def blackjack_win(player):
    if len(hands[player])==2 and hand_score(player) == 21:
        return True
    else:
        return False
        
def check_if_bust(player):
    score = 0
    for num in hands[player]:
        score += num
    if score > 21:
        if 11 in hands[player]:
            while 11 in hands[player]:
                # look for instances of integer 11 in hands[player], fetches its index, and saves the value of 1 under that index. Effectively changing all instances of 11 to 1. ez pz
                hands[player][hands[player].index(11)] = 1
                
                # old-style algorithm commented below. Nakasanayan lang. lolz
                # for num in range(0, len(hands[player])):
                #     if hands[player][num] == 11:
                #         hands[player][num] = 1
        else:
            if player == "player":
                return "computer"
            elif player == "computer":
                return "player"
    
    return ""

def compare_score():
    if hand_score("player") == hand_score("computer"):   
        print (f'\nYour hand {hand_score("player")}, is equal to the house\'s hand of {hand_score("computer")}.\n')
        print ("Game is a draw.")
    elif hand_score("player") > hand_score("computer"):
        if blackjack_win("player"):
            print ("You got a Blackjack!\nYou win!")
        else:
            print (f'\nYour hand {hand_score("player")}, is greater than the house\'s hand of {hand_score("computer")}.\n')
            print ("You win!")
    else:
        if blackjack_win("computer"):
            print ("House gets a Blackjack!\nYou lose.")
        else:
            print (f'\nYour hand {hand_score("player")}, is less than the house\'s hand of {hand_score("computer")}.')
            print (f'The house wins. You lose.\n')

def blackjack():
    winner = ""
    while len(hands["player"])<2:
        deal_card("player")
    while len(hands["computer"])<1:
        deal_card("computer")
    play_continues = True
    
    while play_continues:
        show_cards()
        hit_input = input ("\nDo you want to hit or stand? 'h' to hit or 's' to stand.")
        if hit_input == 'h':
            deal_card("player")
            winner = check_if_bust("player")
        elif hit_input == 's':
            while hand_score("computer") < 17:
                deal_card("computer")
                winner = check_if_bust("computer")
            show_cards()
            play_continues = False
        
        if winner == "computer":
            deal_card("computer")
            show_cards()
            print ("You bust. Computer wins.")
            play_continues = False
        elif winner == "player":
            show_cards()
            print ("House busts. You win!")
            play_continues = False
        else:
            compare_score()
            
print (art.logo)
continue_playing = True

while continue_playing:
    play_input = input ("Do you want to play Blackjack? 'y' to play or 'n' to exit.")
    if play_input == 'y':
        continue_playing = True
        reset()
        blackjack()
    elif play_input == 'n':
        continue_playing = False
        clear()
        print (art.logo)
        print ("Thanks for playing!")
    else:
        clear()
        print (art.logo)
