__author__ = "Tom Sherman"
__version__ = "1.0"

"""
    This script uses the hashmap (dict) generated in hashdict.py and uses it to find all valid matched of letters inputted to words.
"""


def getwords():
    """
        Stores words from dictionary.txt in a dict with keys of letters (sorted alphabetically) and values of a list
    :return words:
    """

    print("Getting words from file...")
    print()

    with open("dictionary.txt") as f:
        words = f.read().splitlines()

    return words


def getletters():
    """
        Get letters to be used. Character '0' signals that the input of letters has ended.

        Also prints the inputted letters so user can check the inputs.

    :return letters:
    """

    letters = []

    letter = input("Input letters (key 0 to signal end of inputs: ")

    while letter != "0":
        letters.append(letter)
        letter = input("Input letter: ")

    # Print letters so user can check the inputs
    print("\nYour letters are")
    for L in letters:
        print(L, end=" ")
    print()

    return letters



