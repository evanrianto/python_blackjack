from gc import callbacks
import random
from tabnanny import check


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate(list):
    '''Check sum of a list'''
    if sum(list) == 21 and len(list) == 2:
        return 0
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)


def check_both_cards(user, computer):
    '''Compare both user's and dealer's deck'''
    if user > 21 and computer > 21:
        return "You went over. You lose"

    if user == computer:
        return "Draw 🙃"
    elif computer == 0:
        return "Lose, opponent has Blackjack"
    elif user == 0:
        return "Win with a Blackjack"
    elif user > 21:
        return "You went over. You lose"
    elif computer > 21:
        return "Opponent went over. You win"
    elif user > computer:
        return "You win"
    else:
        return "You lose"


def play_blackjack():
    '''Start a game of blackjack'''

    user_card = []
    computer_card = []
    game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:

        user_score = calculate(user_card)
        computer_score = calculate(computer_card)

        print(
            f"Your cards : {user_card}, current score : {user_score}")
        print(f"Computer's first card : {computer_card[0]}")

        if(user_score == 0 or computer_score == 0 or user_score > 21):
            game_over = True
        else:
            user_input = input(
                "Type 'y' to get another card, type 'n' to pass: ")

            if user_input == 'y':
                user_card.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate(computer_card)

    print(f"Your hand : {user_card}, final score : {user_score}")
    print(
        f"Computer's final hand : {computer_card}, final score : {computer_score}")
    print(check_both_cards(user_score, computer_score))


while input("Do you want to play a round of blackjack ? (y / n) : ") == 'y':
    deal_card()
    play_blackjack()
