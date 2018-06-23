# DeckOfCards
A module to create a deck of cards object with which you can interact.

### Example usage
**create an instance of DeckOfCards**
`deck_obj = DeckOfCards()`

**add jokers**
`deck_obj.add_jokers()`

**sort the deck by card value**
```
deck_obj.order_deck()
print("\nDeck sorted\n")
deck_obj.print_deck()
```

**give out a random card**
`card = deck_obj.give_random_card()`

**shuffle the deck**
```
deck_obj.shuffle_deck()
print("\nDeck shuffled\n")
deck_obj.print_deck()
```

**insert a new card into the deck**
```
print(len(deck_obj.deck))
card = Card((0, 0))
deck_obj.take_card(card)
print(len(deck_obj.deck))
```

**add a second deck of cards to the first one**
```
print(len(deck_obj.deck))
deck_obj.add_deck()
print(len(deck_obj.deck))
```

### Test coverage
```
============================= test session starts =============================
platform win32 -- Python 3.5.3, pytest-3.6.2, py-1.5.3, pluggy-0.6.0
rootdir: C:\Users\Smoky05\PycharmProjects\DeckOfCards, inifile:
plugins: cov-2.5.1
collected 14 items

test_deck_of_cards.py ..............                                     [100%]

----------- coverage: platform win32, python 3.5.3-final-0 -----------
Name               Stmts   Miss  Cover
--------------------------------------
deck_of_cards.py     135     27    80%


========================== 14 passed in 0.13 seconds ==========================
```