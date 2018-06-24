#!/usr/bin/python
# -*- coding: utf-8 -*-

# Tests for the DeckOfCards module
#
# Author: Simon Lachaîne

# Usage:
#
# Install pytest-cov: pip install pytest-cov
#
# Run tests: py.test --cov=deck_of_cards.deck_of_cards
#
# Docs: http://pytest-cov.readthedocs.io/en/latest/index.html

import copy

import pytest

from deck_of_cards.deck_of_cards import Card, DeckOfCards


class TestCard:

    def test_init(self):
        """
        Asserts that an object created from Card is of the right type
        """
        card_obj = Card((0, 0))
        assert isinstance(card_obj, Card)
        assert isinstance(card_obj, object)

    def test_assign_names_output(self):
        """
        Asserts that _assign_names returns a string
        """
        card = Card((0, 0))
        assert isinstance(card._assign_names(card.rank), str)

    def test_assign_names_error(self):
        """
        Asserts that _assign_names raises an error upon incorrect input type
        """
        card = Card((0, 0))

        with pytest.raises(TypeError):
            card._assign_names("This is not an integer")

    def test_translate_card_error_type(self):
        """
        Asserts that _translate_card raises an error upon incorrect input type
        """
        card = Card((0, 0))
        card.suit = "This is not an integer"

        with pytest.raises(TypeError):
            card._translate_card()

    def test_translate_card_error_number(self):
        """
        Asserts that _translate_card raises an error upon incorrect input number
        """
        card = Card((0, 0))
        card.suit = 5

        with pytest.raises(ValueError):
            card._translate_card()


class TestDeck:

    def test_init(self):
        """
        Asserts that an object created from DeckOfCards is of the right type
        """
        deck_obj = DeckOfCards()
        assert isinstance(deck_obj, DeckOfCards)
        assert isinstance(deck_obj, object)

    def test_add_deck(self):
        """
        Asserts that adding a deck increases the length of the deck
        """
        deck_obj = DeckOfCards()
        original_deck = len(deck_obj.deck)
        deck_obj.add_deck()
        assert original_deck < len(deck_obj.deck)

    def test_order_deck_rank(self):
        """
        Asserts that the deck is ordered by rank
        """
        deck_obj = DeckOfCards()
        deck_obj.order_deck()
        assert (
            card.value < next(deck_obj.deck).value
            for card in deck_obj.deck
        )

    def test_shuffle_deck_order(self):
        """
        Asserts that the deck order is changed
        """
        deck_obj = DeckOfCards()
        reference_deck = copy.deepcopy(deck_obj.deck)
        deck_obj.shuffle_deck()
        assert not reference_deck == deck_obj.deck

    def test_give_card_output(self):
        """
        Asserts the output type of _give_card is an instance of Card
        """
        deck_obj = DeckOfCards()
        card1 = deck_obj.give_random_card()
        card2 = deck_obj.give_first_card()
        card3 = deck_obj.give_last_card()
        assert isinstance(card1, Card)
        assert isinstance(card1, object)
        assert isinstance(card2, Card)
        assert isinstance(card2, object)
        assert isinstance(card3, Card)
        assert isinstance(card3, object)

    def test_take_card_result(self):
        """
        Asserts that the length of the deck is increased when taking a card
        """
        deck_obj = DeckOfCards()
        original_length = len(deck_obj.deck)
        deck_obj.take_card(Card((0, 0)))
        assert original_length < len(deck_obj.deck)

    def test_add_jokers_result(self):
        """
        Asserts that at least one joker has been added
        """
        deck_obj = DeckOfCards()
        deck_obj.add_jokers()
        assert 4 in [
            card.suit
            for card in deck_obj.deck
        ]
