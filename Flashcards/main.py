"""
Author: Melissa Strong

This is a simple flashcard app using a SQLite3 database.

"""
import csv


source_doc = "ccnp_encor_items.csv"


class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __str__(self):
        return f"{self.front}:\n{self.back}"


def main():
    """
    Displays cards one at a time
    User must press enter to reveal the answer and again to move to next question
    :return:
    """
    card_list = []
    gen_cards(card_list)
    for card in card_list:
        input(f"--Press Enter to reveal the answer.\nQ: {card.front}")
        print(f"A: {card.back}\n\n")
        input("--Press Enter to continue to next card.")
        print("\n" * 4)

def gen_cards(card_list):
    """
    Generates a card using the input csv file
    :return: Flashcard
    """
    with open(source_doc) as f:
        cards = csv.reader(f)
        for row in cards:
            card = Flashcard(row[0], row[1])
            card_list.append(card)


if __name__ == "__main__":
    main()

