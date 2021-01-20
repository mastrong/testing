"""
Flashcard App

To Do:
    - Add categories to questions
    - Add counter for point tracking
    - Add attributes to class for tracking how many are known
    - Fix broad except clauses
"""


from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import csv


# Initiate counter object to keep track of where we are in the list index
counter = 0

# Initiate card_list to make it available to all functions
card_list = []


class Flashcard:
    """
    Flashcards have a front (question) and back (answer).
    """

    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __str__(self):
        return f"{self.front}:\n{self.back}"


def gen_cards():
    """
    Generates a card using the input csv file.
    :return: Flashcard list (card_list)
    """

    global card_list
    global counter

    # Start at beginning of list index
    counter = 0

    # Open file selector dialogue box limited to .csv
    source_doc = askopenfilename(filetypes=[("csv files", "*.csv")])

    # Change top label to display current filename
    if source_doc != "":
        label1["text"] = source_doc.split("/")[-1]

    # Clear old cards
    card_list = []
    try:
        with open(source_doc) as f:
            cards = csv.reader(f)
            for row in cards:
                card = Flashcard(row[0], row[1])
                card_list.append(card)
    except:
        pass

    # Show first question after creating cards
    # b1 text changed to trigger condition in flip()
    try:
        b1["text"] = "Hide Answer"
        flip()
    except:
        pass


def del_text(text):
    """
    Streamline adding/removing labels
    :param text: text field to be deleted
    """

    text.delete("1.0", END)

def flip():
    """
    Show and hide answer for current question.
    Also changes button text for showing/hiding answer.
    """

    global counter

    try:
        del_text(front)
        front.insert(END, card_list[counter].front)

        # Change button text
        if b1["text"] == "Show Answer":
            b1["text"] = "Hide Answer"
            back.insert(END, card_list[counter].back)
        else:
            b1["text"] = "Show Answer"
            del_text(back)

        # Change progress indicator text
        # current/max (%)
        label2["text"] = f"{counter+1} / {len(card_list)} ({round((counter+1)/len(card_list), 2)*100}%)"

    except:
        pass


def next_card():
    """
    Increments counter by 1 so that flip() will have next index.
    If next index is out of range for the provided list, counter will return to zero (start over).
    Changes button text so that when flip() is called, the answer is hidden.
    :return:
    """

    global counter
    counter += 1

    try:
        if counter == len(card_list):
            counter = 0

        if len(card_list) == 0:
            b1["text"] = "Show Answer"
        else:
            b1["text"] = "Hide Answer"

        flip()
    except:
        pass


window = Tk()

# Gets h and w info of app
win_width = window.winfo_reqwidth()
win_height = window.winfo_reqheight()

# Window size
window.geometry("450x550")

window.title("Flashcard App")

# Displays current filename
label1 = Label(window, text="")
label1.grid(row=0, column=0, columnspan=3)

# Displays current/total progress through list
label2 = Label(window, text="Progress")
label2.grid(row=0, column=3, columnspan=3, sticky=W)

# Buttons
b1 = Button(window, text="Show Answer", command=flip)
b1.grid(row=1, column=3)

b2 = Button(window, text="Generate Cards", command=gen_cards)
b2.grid(row=2, column=3, sticky=S)

b3 = Button(window, text="Next", command=next_card)
b3.grid(row=2, column=3, sticky=N)


# Question Label
front_label = Label(window, text="Question: ")
front_label.grid(row=1, column=0)
# Question Box
front = Text(window, height=2, width=35)
front.grid(row=1, column=1, columnspan=2)

# Answer Label
back_label = Label(window, text="Answer: ")
back_label.grid(row=2, column=0)
# Answer Box
back = Text(window, height=25, width=35)
back.grid(row=2, column=1, columnspan=2)


if __name__ == "__main__":
    window.mainloop()
