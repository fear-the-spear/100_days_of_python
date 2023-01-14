# my solution
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    random_card = cards[random.randint(0, len(cards) - 1)]
    return random_card


user_hand = []
computer_hand = []
user_hand.append(deal_card())
user_hand.append(deal_card())
computer_hand.append(deal_card())
computer_hand.append(deal_card())
print(user_hand)
print(computer_hand)


def calculate_score(hand):
    if sum(hand) == 21:
        return 0
    if sum(hand) > 21:
        for card in hand:
            if card == 11:
                hand.remove(11)
                hand.append(1)
    return sum(hand)


user_score = calculate_score(user_hand)
computer_score = calculate_score(computer_hand)
# print("User Total:", user_score)
# print("CPU Total:", computer_score)

# Flags
still_playing = True
user_turn = True

if user_score == 0:
    if computer_score == 0:
        print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
        print("Game Over! Dealer wins.")
    print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
    print("Blackjack! You win.")
    still_playing = False
if computer_score == 0:
    print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
    print("Game Over! Dealer wins.")
if user_score > 21:
    print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
    print("Game Over! Dealer wins.")
    still_playing = False

while user_turn:
    draw_again = input("Draw another card? Tyoe 'y' to draw or 'n' to pass: ")

    if draw_again == 'y':
        user_hand.append(deal_card())
        print(user_hand)
        user_score = calculate_score(user_hand)
        print(user_score)
        if user_score == 0:
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("Blackjack! You win.")
        if user_score > 21:
            still_playing = False
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("Game Over! Dealer wins.")
            user_turn = False
    else:
        user_turn = False

while still_playing:
    if computer_score < 17:
        print("It's the computer's turn to draw.")
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
        print(computer_score)
    if computer_score >= 17:
        still_playing = False
        if computer_score == 0:
            still_playing == False
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("Game Over! Dealer wins.")

    def compare(user_score, computer_score):
        if computer_score == user_score:
            print("It's a draw.")
        elif computer_score == 0:
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("Game Over! Dealer wins.")
        elif user_score == 0:
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("Blackjack! You win.")
        elif computer_score > 21:
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("The computer went over 21! You win.")
        elif user_score > 21:
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("You went over 21! You lose.")
        elif user_score > computer_score:
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("You have the high score! You win.")
        elif computer_score > user_score:
            print(f"User Hand: {user_hand}\nDealer Hand: {computer_hand}")
            print("The computer has the high score! You lose.")

    compare(user_score, computer_score)
    still_playing = False
# instructor solution


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and calculate the score from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    # import clear
    play_game()
# htmi = "poopy" butthole
# HTML = "doggy style"
# else:
#    "pp"
#    print(f"i likey do da cha cha")
