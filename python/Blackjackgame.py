import random

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class deck:
    def __init__(self):
        self.cards = []   # FIX 1: cards initialized

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = [
            {"rank": "Ace", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "Jack", "value": 10},
            {"rank": "Queen", "value": 10},
            {"rank": "King", "value": 10}
        ]

        for suit in suits:          # FIX 2: variable naming
            for rank in ranks:
                self.cards.append(card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:     # FIX 3: cars → cards
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for _ in range(number):
            if len(self.cards) > 0:
                cards_dealt.append(self.cards.pop())
        return cards_dealt


class hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, cards_list):
        self.cards.extend(cards_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for c in self.cards:
            self.value += c.rank["value"]
            if c.rank["rank"] == "Ace":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print(f"{'Dealer' if self.dealer else 'Player'} Hand:")
        for index, c in enumerate(self.cards):
            if self.dealer and index == 0 and not show_all_dealer_cards:
                print("Hidden")
            else:
                print(c)
        if not self.dealer:
            print("Value:", self.get_value())
        print()


class game:
    def check_for_blackjack(self, player_hand, dealer_hand):   # FIX 4: function added
        if player_hand.is_blackjack() and dealer_hand.is_blackjack():
            print("Both have Blackjack! Tie.")
            return True
        elif player_hand.is_blackjack():
            print("Player has Blackjack! You win!")
            return True
        elif dealer_hand.is_blackjack():
            print("Dealer has Blackjack! Dealer wins!")
            return True
        return False

    def check_winner(self, player_hand, dealer_hand):
        if player_hand.get_value() > 21:
            print("You busted! Dealer wins!")
        elif dealer_hand.get_value() > 21:
            print("Dealer busted! You win!")
        elif player_hand.get_value() > dealer_hand.get_value():
            print("You win!")
        elif player_hand.get_value() < dealer_hand.get_value():
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        game_number = 0
        game_to_play = 0

        while game_to_play <= 0:
            try:
                game_to_play = int(input("How many games would you like to play? "))
            except:
                print("Please enter a valid number.")

        while game_number < game_to_play:
            game_number += 1

            d = deck()
            d.shuffle()

            player_hand = hand()
            dealer_hand = hand(dealer=True)

            for _ in range(2):
                player_hand.add_card(d.deal(1))
                dealer_hand.add_card(d.deal(1))

            print("*" * 30)
            print(f"Game {game_number} of {game_to_play}")
            print("*" * 30)

            player_hand.display()
            dealer_hand.display()

            if self.check_for_blackjack(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Hit or Stand (h/s): ").lower()
                if choice in ["hit", "h"]:
                    player_hand.add_card(d.deal(1))
                    player_hand.display()

            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(d.deal(1))

            dealer_hand.display(show_all_dealer_cards=True)

            self.check_winner(player_hand, dealer_hand)


g = game()
g.play()
