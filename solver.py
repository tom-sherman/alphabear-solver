__author__ = "Tom Sherman"

"""
    This script uses the hashmap (dict) generated in hashdict.py and uses it to find all valid
    matched of letters inputted to words.
"""
import hashdict
import itertools
from collections import defaultdict


def main():
    dmap = hashdict.readjson("map.json")

    # Loops until user enters the character "0"
    while True:
        letters = getletters()
        if "0" in letters:
            break
        else:
            # Print letters so user can check the inputs
            print("\nYour letters are")
            for L in letters:
                print(L, end=" ")
            print()

            signatures = getsignatures(letters)
            printmatches(dmap, signatures)


def getletters():
    """
        Returns a sanitised, sorted list of letters. Character '0' signals that the input of letters
        has ended.

    :return letters:
    """

    letters = []

    s = input("Input letters (no spaces): ")
    s = sorted(s)   # Sorts letters alphabetically

    for letter in s:
        letters.append(letter)

    return letters


def printmatches(dmap, signatures):
    """
        Actually finds and prints the matches.


    :param dmap:
    :param signatures:
    """

    for signature in signatures:
        try:
            print(dmap[signature])
        except KeyError:
            pass


def getsignatures(letters):
    """
        Generates all possible unique combination of the list of letters
        provided.

    :param letters:
    :return signatures:
    """

    signatures = []

    for i in range(1, len(letters)):
        k = list(itertools.combinations(range(0, len(letters)), i))  # Generates all sets k

        for kSet in k:
            signature = ""
            for pointer in kSet:
                signature = signature + letters[pointer]

            signature = "".join(sorted(signature))
            signatures.append(signature)

    # Finally check if raw letters are a valid signature
    signature = ""
    for letter in letters:  #
        signature += letter
    signature = "".join(sorted(signature))
    signatures.append(signature)

    #print(signatures)
    return removedupes(signatures)


def removedupes(lst):
    """
        Removes all duplicates from a list

    :param lst:
    :return unique_list:
    """

    output = []
    seen = set()
    for value in lst:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


if __name__ == '__main__':
    main()