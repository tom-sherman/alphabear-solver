__author__ = "Tom Sherman"

"""
    This script reads from a file (dictionary.txt), generates a hashmap (dict) and dumps it to a json file.
    Only needs to be run once, unless the dictionary changes.

    It's quite slow, but once completed lookup of valid matches is blazing fast.
"""

from collections import defaultdict
import json


dictFileName = "dictionary.txt"
mapFileName = "map.json"


def main():
    dictmap = createdict(dictFileName)
    storejson(dictmap)
    print("JSON file generated from " + dictFileName)
    d = readjson(mapFileName)
    print(d)


def createdict(filename):
    """
        Reads a txt file of words, one word per line, and stores that in a map (dict).

        Keys are unique signatures of one or more words - an ordered list of letters
        that can make up each word in the dictionary. The values are the words the
        signature can make.

    :return dmap:
    :param filename: A text file, one word per line
    """
    # the "signature" of a word is the ordered list of its letters

    dictfile = open(filename)   # open the wordlist
    dmap = defaultdict(list)    # associate to each signature the words that have that signature

    for word in dictfile.readlines():
        word = word.lower()
        signature = "".join(sorted(word.strip()))  # get the word signature
        dmap[signature].append(word.strip())

    dictfile.close()

    return dmap


def storejson(dmap):
    """
        Stores the map as a json txt file.

        :param dmap:
    """

    jsoncontent = json.dumps(dmap)

    with open(mapFileName, "w") as f:
        f.write(jsoncontent)


def readjson(filename):
    """
        Reads a json file and returns it as a dict (map)
    :param filename:
    :return json dict:
    """

    with open(filename) as f:

        data = json.loads(f.read())

    return data


if __name__ == '__main__':
    main()
