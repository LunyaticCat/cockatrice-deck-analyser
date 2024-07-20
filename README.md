# Description
Display the color distribution of your Cockatrice deck.
# Example
If you have Spark Trooper in your deck [1RRW], it will add 1 to C, 1 to R and 1 to W like so :<br>
```
Colors in your deck:
W: 1
U: 0
B: 0
R: 1
G: 0
C: 1
Total number of cards: 1
```
# Usage
``python analyze_deck.py --sets pathToSet/set1.xml pathToSet/set2.xml --deck pathToDeck/yourDeck.cod``
## arguments
- `sets` Path to each of your data sets. You can get cards.xml containing regular MTG cards from your cockatrice folder. Your custom sets should be in your `customsets` folder.<br>
- `deck` Path to the deck you want to analyse. It should be in your cockatrice folder in `decks`.
