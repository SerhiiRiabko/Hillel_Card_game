from deck import Deck


class Blackjack(Deck):
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        self.player_hand = [self.deck.deal_card(), self.deck.deal_card()]
        self.dealer_hand = [self.deck.deal_card(), self.deck.deal_card()]

    @staticmethod
    def calculate_hand_value(hand):
        total_value = 0
        num_aces = 0

        for card in hand:
            if card.rank in ["J", "Q", "K"]:
                total_value += 10
            elif card.rank == "A":
                total_value += 11
                num_aces += 1
            else:
                total_value += int(card.rank)

        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1

        return total_value

    def play(self):
        print("Welcome to Blackjack!")
        self.deal_initial_cards()

        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        print("Player's hand:", ", ".join(str(card) for card in self.player_hand))
        print("Dealer's hand:", self.dealer_hand[0])

        while True:
            if player_value == 21:
                print("Player wins with a Blackjack!")
                break
            elif player_value > 21:
                print("Player busts. Dealer wins!")
                break

            action = input("Do you want to hit or stand? (h/s): ")

            if action.lower() == "h":
                self.player_hand.append(self.deck.deal_card())
                player_value = self.calculate_hand_value(self.player_hand)
                print("Player's hand:", ", ".join(str(card) for card in self.player_hand))

            if action.lower() == "s":
                print("Player stands.")

                while dealer_value < 17:
                    self.dealer_hand.append(self.deck.deal_card())
                    dealer_value = self.calculate_hand_value(self.dealer_hand)

                print("Dealer's hand:", ", ".join(str(card) for card in self.dealer_hand))

                if dealer_value == 21:
                    print("Dealer wins with a Blackjack!")
                elif dealer_value > 21:
                    print("Dealer busts. Player wins!")
                elif dealer_value > player_value:
                    print("Dealer wins!")
                elif dealer_value < player_value:
                    print("Player wins!")
                else:
                    print("It's a tie!")

                break


if __name__ == "__main__":
    game = Blackjack()
    game.play()
