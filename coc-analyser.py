import xml.etree.ElementTree as ET
from collections import defaultdict


# Function to extract colors from mana cost and count each type once per card
def extract_colors(mana_cost):
    colors = {"W": 0, "U": 0, "B": 0, "R": 0, "G": 0, "C": 0}
    if mana_cost:
        # Count each color mana symbol once if it appears
        if 'W' in mana_cost:
            colors["W"] = 1
        if 'U' in mana_cost:
            colors["U"] = 1
        if 'B' in mana_cost:
            colors["B"] = 1
        if 'R' in mana_cost:
            colors["R"] = 1
        if 'G' in mana_cost:
            colors["G"] = 1
        # Count colorless mana (numbers)
        if any(char.isdigit() for char in mana_cost):
            colors["C"] = 1
        # Count the 'C' symbol for colorless mana
        if 'C' in mana_cost:
            colors["C"] = 1
    return colors


# Function to parse a card data XML file and return a dictionary of card names and their mana costs
def parse_card_data(file_paths):
    mana_costs = defaultdict(str)
    for file_path in file_paths:
        card_data_tree = ET.parse(file_path)
        card_data_root = card_data_tree.getroot()
        for card_element in card_data_root.findall('.//card'):
            name = card_element.find('name').text
            mana_cost = card_element.find('prop/manacost').text \
                if card_element.find('prop/manacost') is not None else ""
            # Combine mana costs if the card appears in multiple sets
            mana_costs[name] = mana_cost
    return mana_costs


# Load the card data from multiple files
card_data_files = ['sets/cards.xml', 'sets/01.fchon.xml']  # Add paths to all card data files
card_mana_costs = parse_card_data(card_data_files)

# Load the decklist XML
deck_tree = ET.parse('decks/Flame-Chasers.cod')
deck_root = deck_tree.getroot()

# Initialize a dictionary to count colors in the deck and a counter for total cards
deck_colors = {"W": 0, "U": 0, "B": 0, "R": 0, "G": 0, "C": 0}
total_cards = 0

# Iterate through each card in the deck and count colors
for card in deck_root.findall('.//zone[@name="main"]/card'):
    card_name = card.get('name')
    card_number = int(card.get('number'))
    total_cards += card_number
    if card_name in card_mana_costs:
        card_colors = extract_colors(card_mana_costs[card_name])
        for color in deck_colors.keys():
            deck_colors[color] += card_colors[color] * card_number

# Print the result
print("Colors in your deck:")
for color, count in deck_colors.items():
    print(f"{color}: {count}")

print(f"Total number of cards: {total_cards}")

# Example usage
# Save the script as analyze_deck.py and run it with the correct file paths
# python analyze_deck.py
