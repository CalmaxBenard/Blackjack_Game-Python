import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    played_cards = []
    dealer_cards = []

    card1 = random.choice(cards)
    played_cards.append(card1)
    card2 = random.choice(cards)
    played_cards.append(card2)
    dealer_card1 = random.choice(cards)
    dealer_cards.append(dealer_card1)
    score = card1 + card2

    def player():
        player_card = random.choice(cards)
        played_cards.append(player_card)

    def computer():
        dealer_card = random.choice(cards)
        dealer_cards.append(dealer_card)

    start = input("Do you want to play a game of Blackjack? 'y' or 'n'?: ").lower()
    if start == 'y':
        print(f"Your cards are {played_cards}, a score of {score}")
        print(f"Dealer card {dealer_card1}")
    else:
        blackjack()

    play = True

    while play:
        total = sum(played_cards)
        restart = input("Type 'y' to pick another card or 'n' to pass: ").lower()
        if restart == "y":
            player()
            total = sum(played_cards)
            print(f"Your cards are {played_cards}, a score of {total}")
            if total > 21:
                print("Burst \n You Lose!")
                play = False
                print()
            elif total == 21:
                print("You win with a blackjack.")
                play = False
        else:
            computer()
            dealer_total = sum(dealer_cards)
            if dealer_total > score and dealer_total > total:
                print(f"The dealer cards are {dealer_cards}, a score of {dealer_total}")
                print("You Lose!")
                blackjack()
            else:
                computer()
                dealer_total = sum(dealer_cards)
                if dealer_total == total:
                    print(f"The dealer cards are {dealer_cards}, a score of {dealer_total}")
                    print("Draw")
                    blackjack()
                elif 21 >= dealer_total > total:
                    print(f"The dealer cards are {dealer_cards}, a score of {dealer_total}")
                    print("You Lose!")
                    blackjack()
                else:
                    print(f"The dealer cards are {dealer_cards}, a score of {dealer_total}")
                    print("You Win!")
            play = False
            blackjack()


blackjack()
