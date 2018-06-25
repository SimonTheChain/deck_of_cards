Classes and Methods
====================

class deck_of_cards.Card(suit_rank_tup)
-----------------------------------------------
.. code-block:: python

    self.suit = suit_rank_tup[0]
    self.rank = suit_rank_tup[1]
    self.value = self.rank
    self.name = self._translate_card()
    self.image_path = ""


class deck_of_cards.DeckOfCards
---------------------------------------
.. code-block:: python

    add_deck()

Adds another deck of cards to the existing deck
:return: deck attribute

.. code-block:: python

    add_jokers()

Adds jokers to the deck
:return: deck objects

.. code-block:: python

    give_first_card()

Gives the first card in the deck
:return: card object

.. code-block:: python

    give_last_card()

Gives the last card in the deck
:return: card object

.. code-block:: python

    give_random_card()

Gives a random card from the deck
:return: card object

.. code-block:: python

    order_deck()

Orders the cards in the deck by value and rank
:return: deck object

.. code-block:: python

    print_deck()

Prints the name of the cards in the deck
:return: print statement

.. code-block:: python

    reset_deck()

Resets the deck object
:return: deck object

.. code-block:: python

    shuffle_deck()

Shuffles the cards in the deck
:return: deck object

.. code-block:: python

    take_card(card)

Adds a card to the deck :param card: card object
:return: deck object