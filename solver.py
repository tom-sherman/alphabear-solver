__author__ = "Tom Sherman"
__version__ = "1.0"

"""
    This script uses the hashmap (dict) generated in hashdict.py and uses it to find all valid
    matched of letters inputted to words.
"""
import hashdict
import itertools
from collections import defaultdict


def main():
    dmap = defaultdict(list)
    dmap = hashdict.readjson("map.json")

    letters = getletters()

    printmatches(dmap, letters)


def getletters():
    """
        Returns a sanitised, sorted list of letters. Character '0' signals that the input of letters
        has ended.

        Also prints the inputted letters so user can check the inputs.

    :return letters:
    """

    letters = []

    s = input("Input letters (no spaces): ")

    s = sorted(s)   # Sorts letters alphabetically

    for letter in s:
        letters.append(letter)

    # Print letters so user can check the inputs
    print("\nYour letters are")
    for L in letters:
        print(L, end=" ")
    print()

    return letters


def printmatches(dmap, letters):
    """
        Actually finds and prints the matches.


    :param dmap:
    :param letters:
    """
    
    for i in range(1, len(letters)):
        k = list(itertools.combinations(range(0, len(letters)), i))  # Generates all sets k

        for kSet in k:
            signature = ""
            for pointer in kSet:
                signature = signature + letters[pointer]

            try:
                print(dmap[signature])
            except KeyError:
                pass

    signature = ""
    for letter in letters:  # Finally check if raw letters are a valid signature
        signature += letter
    try:
        print(dmap[signature])
    except KeyError:
        pass



main()
