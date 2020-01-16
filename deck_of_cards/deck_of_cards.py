#!/usr/bin/python
# -*- coding: utf-8 -*-

# Deck of cards
#
# Author: Simon Lachaîne


import logging
from random import shuffle, choice
import operator

# from highest to lowest: WARNING, INFO, DEBUG, NOTSET
logging.basicConfig(level=logging.WARNING)


class DeckError(Exception):
    pass


class Card(object):

    def __init__(self, suit_rank_tup):
        """
        Initializes the card object
        :param suit_rank_tup: a tuple of integers representing suit and rank
        """
        self.suit = suit_rank_tup[0]
        self.rank = suit_rank_tup[1]
        self.value = self.rank
        self.name = self._translate_card()
        self.image_path = ""
        self.image_obj = None

        logging.debug("_Card initialized_")

    def __eq__(self, other):
        """
        Overrides equality comparison to allow sorting of objects
        :param other: other Card instance to compare
        :return:
        """
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        """
        Overrides lower than to allow sorting of objects
        :param other: other Card instance to compare
        :return:
        """
        return self.value < other.value

    def __gt__(self, other):
        """
        Overrides greater than to allow sorting of objects
        :param other: other Card instance to compare
        :return:
        """
        return self.value > other.value

    @staticmethod
    def _assign_names(rank):
        """
        Assigns card names according to rank
        :param rank: rank of the card
        :return: string of the card's name
        """
        if isinstance(rank, int):

            if rank == 1:
                return "Ace"

            elif rank == 11:
                return "Jack"

            elif rank == 12:
                return "Queen"

            elif rank == 13:
                return "King"

            elif rank == 14:
                return "Black and white"

            elif rank == 15:
                return "Color"

            else:
                return str(rank)

        else:
            logging.info("An invalid parameter was passed to '_assign_names'")
            raise TypeError("The argument for the method must be an integer")

    def _translate_card(self):
        """
        Creates a human-readable name for the card
        :return: full name of the card
        """
        if isinstance(self.suit, int):

            if self.suit == 0:
                self.name = "{} of spades".format(self._assign_names(self.rank))

            elif self.suit == 1:
                self.name = "{} of hearts".format(self._assign_names(self.rank))

            elif self.suit == 2:
                self.name = "{} of diamonds".format(self._assign_names(self.rank))

            elif self.suit == 3:
                self.name = "{} of clubs".format(self._assign_names(self.rank))

            elif self.suit == 4:
                self.name = "{} joker".format(self._assign_names(self.rank))

            else:
                logging.info("The instance attribute suit is not between 0 and 4 inclusively")
                raise ValueError("The integer passed to the method must be 0, 1, 2, 3 or 4")

        else:
            logging.info("An invalid parameter was passed to '_translate_card'")
            raise TypeError("The argument for the method must be an integer")

        logging.debug("{}\n".format(self.name))
        return self.name


class DeckOfCards(object):

    SUITS_RANKS = [
        (
            i % 4,  # suit
            13 if i % 13 == 0 else i % 13  # rank
        )
        for i in range(1, 53)
    ]

    def __init__(self):
        """
        Initializes the deck object with a single deck of cards
        """
        self.deck = [
            Card(tup)
            for tup in self.SUITS_RANKS
        ]
        logging.debug("_Deck initialized_")

    def _deck_empty(self):
        """
        Checks if the deck is empty
        :return: True if empty, False if not
        """
        if len(self.deck) < 1:
            return True

        else:
            return False

    def add_deck(self):
        """
        Adds another deck of cards to the existing deck
        :return: deck attribute
        """
        deck = [
            Card(tup)
            for tup in self.SUITS_RANKS
        ]
        self.deck += deck
        logging.debug("Deck of cards added")
        return self.deck

    def order_deck(self):
        """
        Orders the cards in the deck by value and rank
        :return: deck object
        """
        self.deck.sort(key=operator.attrgetter("value", "suit"))
        logging.debug("_Deck sorted_\n{}".format(
            [
                card.name
                for card in self.deck
            ]
        ))
        return self.deck

    def shuffle_deck(self):
        """
        Shuffles the cards in the deck
        :return: deck object
        """
        shuffle(self.deck)
        logging.debug("_Deck shuffled_\n{}".format(
            [
                card.name
                for card in self.deck
            ]
        ))
        return self.deck

    def print_deck(self):
        """
        Prints the name of the cards in the deck
        :return: print statement
        """
        [
            print(card.name)
            for card in self.deck
        ]

    def reset_deck(self):
        """
        Resets the deck object
        :return: deck object
        """
        self.__init__()
        logging.debug("_Object reinitialized_")
        return self.deck

    def _give_card(self, method_name, operation):
        """
        Template for the methods that give a card from the deck
        :return: card object
        """
        if self._deck_empty():
            logging.info(
                "'{method_name}' called while the deck is empty\n".format(
                    method_name=method_name
                )
            )
            raise DeckError("Cannot retrieve a card from an empty deck")

        card = operation
        logging.debug("_Card given_\n{}".format(card.name))
        return card

    def give_random_card(self):
        """
        Gives a random card from the deck
        :return: card object
        """
        card = self._give_card(
            method_name="give_random_card",
            operation=choice(self.deck)
        )

        for card_obj in self.deck:
            if card_obj.name == card.name:
                self.deck.remove(card_obj)
        return card

    def give_first_card(self):
        """
        Gives the first card in the deck
        :return: card object
        """
        card = self._give_card(
            method_name="give_first_card",
            operation=self.deck.pop(0)
        )
        return card

    def give_last_card(self):
        """
        Gives the last card in the deck
        :return: card object
        """
        card = self._give_card(
            method_name="give_last_card",
            operation=self.deck.pop()
        )
        return card

    def take_card(self, card):
        """
        Adds a card to the deck
        :param card: card object
        :return: deck object
        """
        if isinstance(card, Card):
            logging.debug("_Card taken_\n{}\n".format(card.name))
            return self.deck.append(card)

        else:
            logging.info("An invalid parameter was passed to 'take_card'")
            raise DeckError("The parameter for the take_card method must be a Card object")

    def add_jokers(self):
        """
        Adds jokers to the deck
        :return: deck objects
        """
        joker_bw = Card((4, 14))
        joker_color = Card((4, 15))
        self.deck.append(joker_bw)
        self.deck.append(joker_color)
        return self.deck


def main():
    """
    Example usage
    :return: None
    """
    # create an instance of DeckOfCards
    deck_obj = DeckOfCards()

    # add jokers
    deck_obj.add_jokers()

    # sort the deck by value
    deck_obj.order_deck()
    print("\nDeck sorted\n")
    deck_obj.print_deck()

    # give out a random card
    print("\nTaking a random card")
    card = deck_obj.give_random_card()
    print(card.name)

    # shuffle the deck
    deck_obj.shuffle_deck()
    print("\nDeck shuffled\n")
    deck_obj.print_deck()

    print("\nLength of deck\n")
    # add a second deck of cards to the first one
    deck_obj.add_deck()
    print(len(deck_obj.deck))

    # insert a new card into the deck
    card = Card((2, 4))
    deck_obj.take_card(card)
    print(len(deck_obj.deck))


if __name__ == "__main__":
    main()
