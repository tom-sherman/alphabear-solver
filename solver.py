__author__ = "Tom Sherman"

"""
    This script uses the hashmap (dict) generated in hashdict.py and uses it to
    find all valid matched of letters inputted to words.

"""
import hashdict
import itertools
import re
from collections import defaultdict
import copy


def main():
    dmap = hashdict.readjson("map.json")
    turns = False
    s = ""

    while s not in ("y", "Y", "n", "N"):
        s = input("Input turns? (y/n)")
        if s in ("y", "Y"):
            turns = True
        else:
            turns = False

    # Loops until user enters the character "0"
    while True:
        letters = getletters(turns)

        if "0" in letters:
            break
        else:

            # Print letters so user can check the inputs
            print("\nYour letters are")
            for L in letters:
                print(L, end=" ")
            print()

            if turns:
                parseturnes(letters, dmap)
            else:
                signatures = getsignatures(letters)
                matches = getmatches(dmap, signatures)
                printmatches(matches)


def getletters(turns=False):
    """
        Returns a sanitised, sorted list of letters.

    :param turns: (bool) Whether the user should input them amount of turns.
    :return letters:
    """

    if turns:
        print("Syntax: [1];[2];[3];...[n] \n"
              "Where [1], [2] ... [n] are a list of letters (no spaces) with "
              "that amount of turns left.")
        arg = input("Input letters: ")

        letterssorted = []
        if validsyntax(arg):
            # Gets a list of letter groups
            lettergroups = arg.split(";")
            # Each letter group is sorted

            # Sort the groups
            for letters in lettergroups:
                letterssorted.append(sorted(letters))

            return letterssorted
        else:
            letterssorted.append("0")
            return letterssorted

    else:
        s = input("Input letters (no spaces): ")

        letters = []
        for letter in sorted(s):
            letters.append(letter)

        return letters


def getmatches(dmap, signatures):
    """

    :param dmap:
    :param signatures:
    :return matches:
    """

    matches = []

    for signature in signatures:
        try:
            matches = matches + dmap[signature]
        except KeyError:
            pass

    return matches


def printmatches(matches):
    """
    :param matches:
    """

    print()
    print("Length | Words")
    print("-------|------")

    for match in matches:
        print("{0:6} | {1}".format(len(match), match))


def getsignatures(letters):
    """
        Generates all possible unique combination of the list of letters
        provided.

    :param letters:
    :return signatures:
    """

    signatures = []

    for i in range(1, len(letters)):

        # Generates all sets k
        k = list(itertools.combinations(range(0, len(letters)), i))

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

    return removedupes(signatures)


def removedupes(lst):
    """
        Returns all duplicates from a list

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


def validsyntax(arg):
    """
        Validates syntax used in parseturns.

    :param arg: String to be checked.
    :return bool: True if valid syntax
    """
    arg = "<" + arg + ">"
    r = re.compile(r"<(([a-z]+|\s?);)+[a-z]*>")

    if r.search(arg) is None:
        return False
    else:
        return True


def parseturnes(lsletters, dmap):
    """
        Used when you want to use the 'turns' syntax.

        Prints the top 3 words to play, calculates using getscore.

    :param lsletters:
    """
    letters = []
    turnmap = getturnmap(lsletters)

    for ls in lsletters:
        for l in ls:
            letters.append(l)

    letters = sorted(letters)
    signatures = getsignatures(letters)

    matches = getmatches(dmap, signatures)
    printmatches(matches)

    scoredict = defaultdict(list)
    for match in matches:
        score = getscore(turnmap, match)

        scoredict[score].append(match)

    print("Top 3 words:")

    counter = 0
    for score in reversed(sorted(scoredict)):
        if counter == 3:
            break
        print("{0}. {1}".format(counter, scoredict[score]))
        counter += 1


def getturnmap(lsletters):
    """
        Returns a map with the score as the key, and the words with that score
        as the corresponding values.

    :param lsletters:
    :return turnmap:
    """
    index = 1

    turnmap = defaultdict(list)
    for ls in lsletters:
        for letter in ls:
            if letter != " ":
                turnmap[index].append(letter)
        index += 1

    return turnmap


def getscore(turnmap, match):
    """
        Gets the score of each word.
        This isn't the actual game score, just a number used to rank the words.

    :param turnmap:
    :param match:
    :return score:
    """
    score = 0
    tm = copy.deepcopy(turnmap)  # Create copy.

    for c in match:
        for k in tm:
            if c in tm[k]:
                # Removes first character
                match = match[1:]
                tm[k].remove(c)

                if k == 1:
                    score += 100
                elif k == 2:
                    score += 6
                elif k == 3:
                    score += 5
                else:
                    score += 1

    return score


if __name__ == '__main__':
    main()
