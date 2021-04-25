Example usage
====================

import the module
-----------------
.. code-block:: python
    :emphasize-lines: 1

    from deck_of_cards import deck_of_cards

create an instance of DeckOfCards
---------------------------------
.. code-block:: python
    :emphasize-lines: 1

    deck_obj = deck_of_cards.DeckOfCards()

add jokers
----------
.. code-block:: python
    :emphasize-lines: 1

    deck_obj.add_jokers()

sort the deck by card value
---------------------------
.. code-block:: python
    :emphasize-lines: 1

    deck_obj.order_deck()
    print("\nDeck sorted\n")
    deck_obj.print_deck()

give out a random card
----------------------
.. code-block:: python
    :emphasize-lines: 1

    card = deck_obj.give_random_card()

card objects have the following attributes
------------------------------------------
.. code-block:: python
    :emphasize-lines: 1,2,3,4,5

    card.suit  # 0=spades, 1=hearts, 2=diamonds, 3=clubs, 4=joker
    card.rank  # 1=Ace, 11=Jack, 12=Queen, 13=King, 14=B&W Joker, 15=Color Joker
    card.value # defaults: same as rank
    card.name  # string representation
    card.image_path  # path to an image file corresponding to the card

insert a new card into the deck
-------------------------------
.. code-block:: python
    :emphasize-lines: 2,4

    print(len(deck_obj.deck))
    card = deck_of_cards.Card((2, 11))
    print(card.name)
    deck_obj.take_card(card)
    print(len(deck_obj.deck))

shuffle the deck
----------------
.. code-block:: python
    :emphasize-lines: 1

    deck_obj.shuffle_deck()
    print("\nDeck shuffled\n")
    deck_obj.print_deck()

add a second deck of cards to the first one
-------------------------------------------
.. code-block:: python
    :emphasize-lines: 2

    print(len(deck_obj.deck))
    deck_obj.add_deck()
    print(len(deck_obj.deck))

index and iterate over a deck object
------------------------------------
.. code-block:: python
    :emphasize-lines: 2

    first_card = deck_obj[0]
    card_names = [card.name for card in deck_obj]
