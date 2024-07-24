#Assignment-3 #Question-2

class CardHand:
    def __init__(self):
        # Initialize an empty list to store cards and set up the "fingers" list with None for each suit
        self.cards = []
        self.fingers = [None] * 4

    def add_card(self, r, s):
        # Add a new card with rank r and suit s to the hand
        card = (r, s)
        suit_index = self._get_suit_index(s)
        if suit_index is None:
            # If this is the first card of this suit, update the "finger" for that suit
            self.fingers[self._suit_to_index(s)] = len(self.cards)
        self.cards.append(card)

    def play(self, s):
        # Remove and return a card of suit s from the player's hand, or an arbitrary card if not found
        suit_index = self._get_suit_index(s)
        if suit_index is None:
            return self.cards.pop()
        else:
            return self.cards.pop(self.fingers[suit_index])

    def __iter__(self):
        # Enable iteration through all cards currently in the hand
        return iter(self.cards)

    def all_of_suit(self, s):
        # Iterate through all cards of suit s that are currently in the hand
        suit_index = self._get_suit_index(s)
        if suit_index is None:
            # If the suit is not found, return an empty iterator
            return iter([])
        else:
            return iter(self.cards[self.fingers[suit_index]:self.fingers[suit_index+1]])

    def _get_suit_index(self, s):
        # Helper method to get the index of the first card of a given suit in the "fingers" list
        try:
            return self.fingers[self._suit_to_index(s)]
        except TypeError:
            # If the suit is not valid, return None
            return None

    @staticmethod
    def _suit_to_index(s):
        # Helper method to convert the suit name to its corresponding index
        suits = {'hearts': 0, 'clubs': 1, 'spades': 2, 'diamonds': 3}
        return suits.get(s.lower(), None)


def main():
    # Main function to test the CardHand class

    hand = CardHand()

    # Add cards to the hand
    hand.add_card('9', 'hearts')
    hand.add_card('K', 'clubs')
    hand.add_card('7', 'spades')
    hand.add_card('4', 'hearts')

    # Iterate through and print all cards in the hand
    for card in hand:
        print(f"{card[0]} of {card[1]}")

    # Play cards from the hand and print the result
    print("Playing a spade:", hand.play('spades'))
    print("Playing a diamond:", hand.play('diamonds'))

    # Print the remaining cards in the hand after playing
    print("\nRemaining cards in the hand:")
    for card in hand:
        print(f"{card[0]} of {card[1]}")

    # Print all cards of hearts in the hand
    print("\nAll cards of hearts:")
    for card in hand.all_of_suit('hearts'):
        print(f"{card[0]} of {card[1]}")

# Call the main function to run the test
if __name__ == "__main__":
    main()
