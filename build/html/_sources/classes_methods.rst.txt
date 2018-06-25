Classes: Attributes and Methods
===============================

class deck_of_cards.Card(suit_rank_tup)
---------------------------------------
**Attributes**

.. code-block:: python

    self.suit = suit_rank_tup[0]
    self.rank = suit_rank_tup[1]
    self.value = self.rank
    self.name = self._translate_card()
    self.image_path = ""


class deck_of_cards.DeckOfCards()
---------------------------------
**Attributes**

.. code-block:: python

    self.deck = [Card(tup) for tup in self.SUITS_RANKS]

**Methods**

.. code-block:: python

    add_deck()
    :return: deck object

Adds another deck of cards to the existing deck

.. code-block:: python

    add_jokers()
    :return: deck object

Adds jokers to the deck

.. code-block:: python

    give_first_card()
    :return: card object

Gives the first card in the deck

.. code-block:: python

    give_last_card()
    :return: card object

Gives the last card in the deck

.. code-block:: python

    give_random_card()
    :return: card object

Gives a random card from the deck

.. code-block:: python

    order_deck()
    :return: deck object

Sorts the cards in the deck by value and suit

.. code-block:: python

    print_deck()
    :return: print statement

Prints the name of the cards in the deck

.. code-block:: python

    reset_deck()
    :return: deck object

Resets the deck object

.. code-block:: python

    shuffle_deck()
    :return: deck object

Shuffles the cards in the deck

.. code-block:: python

    take_card(card)
    :param card: card object
    :return: deck object

Adds a card to the deck