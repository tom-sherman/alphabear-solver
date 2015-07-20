__author__ = "Tom Sherman"
__version__ = "0.1"


def main():
    words = getwords()
    letters = getletters()

    matches = getmatches(words, letters)

    print("Here are your matching words: ")
    for match in matches:
        print(match)


def getwords():
    """
        Reads, line by line, each word in dictionary.txt and stores them in a list.
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
    for c in letters:
        print(c, end=" ")
    print()

    return letters


def getmatches(words, letters):
    """
        Takes two string lists as parameters, words and letters.

        Returns a list of matches. A match is a word in 'words' that contains
        some letters in 'letters'. Each letter can be used 0 or 1 times.


    :param words:
    :param letters:
    :return matches:
    """

    matches = []

    return matches


main()
