__author__ = "Tom Sherman"

"""
    This script uses the hashmap (dict) generated in hashdict.py and uses it to
    find all valid matched of letters inputted to words.

"""
import hashdict
import itertools


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
        Returns a sanitised, sorted list of letters.

    :return letters:
    """

    letters = []

    s = input("Input letters (no spaces): ")

    for letter in sorted(s):
        letters.append(letter)

    return letters


def printmatches(dmap, signatures):
    """
        Actually finds and prints the matches.


    :param dmap:
    :param signatures:
    """

    print()
    print("Length | Words")
    print("--------------")

    for signature in signatures:
        try:
            matches = dmap[signature]

            print("{0:6} | ".format(len(matches[0])), end="")

            for match in matches:
                print(match, end=" ")
            print()

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
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> origin/master
